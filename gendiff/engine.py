import json
import yaml
from os.path import splitext


def read_data(path):
    with open(path, 'r') as content_file:
        return parse_content(content_file.read(), get_type(path))


def get_type(path):
    _, ext = splitext(path)
    return ext


def parse_content(content, file_type) -> dict:
    if file_type == '.json':
        return json.loads(content)
    elif file_type == '.yaml' or file_type == '.yml':
        return yaml.load(content, Loader=yaml.Loader)


def build_diff(dictionary_1, dictionary_2):
    list_res = []
    for key in set(list(dictionary_1.keys()) + list(dictionary_2.keys())):
        if key not in dictionary_2:
            list_res.append({"key": key, "action": "deleted",
                             "old_value": dictionary_1[key]})
        elif (key in dictionary_2 and dictionary_1.get(key) != dictionary_2[key]
              and isinstance(dictionary_1.get(key), dict)
              and isinstance(dictionary_2.get(key), dict)):
            list_res.append({"key": key, "action": "nested",
                             "children": build_diff(dictionary_1.get(key),
                                                    dictionary_2.get(key))})
        elif key not in dictionary_1:
            list_res.append(
                {"key": key, "action": "added", "new_value": dictionary_2[key]})
        elif key in dictionary_2 and dictionary_1.get(key) != dictionary_2[key]:
            list_res.append(
                {"key": key, "action": "changed",
                 "old_value": dictionary_1.get(key),
                 "new_value": dictionary_2[key]})
        else:
            list_res.append(
                {"key": key, "action": "unchanged",
                 "value": dictionary_1.get(key)})

        list_res.sort(key=lambda x: x.get("key"))

    return list_res


def generate_diff(file_path1, file_path2):
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)
    return build_diff(data1, data2)
