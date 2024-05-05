import json
import yaml

data_1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

data_2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}

with open("file1.json", "w") as write_file:
    json.dump(data_1, write_file)

with open("file2.json", "w") as write_file:
    json.dump(data_2, write_file)

json_string_1 = json.dumps(data_1)
json_string_2 = json.dumps(data_2)

dict_1 = json.loads(json_string_1)
dict_2 = json.loads(json_string_2)

data_3 = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {
            "key": "value",
            "doge": {
                "wow": ""
            }
        }
    },
    "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value"
        }
    },
    "group2": {
        "abc": 12345,
        "deep": {
            "id": 45
        }
    }
}

data_4 = {
    "common": {
        "follow": False,
        "setting1": "Value 1",
        "setting3": None,
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5"
        },
        "setting6": {
            "key": "value",
            "ops": "vops",
            "doge": {
                "wow": "so much"
            }
        }
    },
    "group1": {
        "foo": "bar",
        "baz": "bars",
        "nest": "str"
    },
    "group3": {
        "deep": {
            "id": {
                "number": 45
            }
        },
        "fee": 100500
    }
}

with open("file3.json", "w") as write_file:
    json.dump(data_3, write_file)

with open("file4.json", "w") as write_file:
    json.dump(data_4, write_file)

json_string_3 = json.dumps(data_3)
json_string_4 = json.dumps(data_4)

dict_3 = json.loads(json_string_3)
dict_4 = json.loads(json_string_4)


def read_data(path):
    if path.endswith('.json'):
        with open(path, 'r') as json_file:
            return json.loads(json_file.read())
    elif path.endswith('.yaml') or path.endswith('.yml'):
        with open(path, 'r') as yaml_file:
            return yaml.load(yaml_file.read(), Loader=yaml.Loader)


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
