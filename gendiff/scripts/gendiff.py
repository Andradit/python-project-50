#!/usr/bin/env python3
import argparse
import json
import yaml

from gendiff.formatters.stylish_formatter import format_stylish
from gendiff.formatters.json_formatter import format_json
from gendiff.formatters.plain_formatter import format_plain

def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        type=str,
                        default='stylish',
                        choices=['json', 'stylish', 'plain'])
    return parser.parse_args()


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

# 1. Прочитать содержимое файлов (2 переменных) - весь файл в одной
# переменной (одна строка)

json_string_1 = json.dumps(data_1)
# print(json_string_1)
json_string_2 = json.dumps(data_2)
# print(json_string_2)

# print(open('file1.json', 'r').read())
# print(open('file2.json', 'r').read())

# 2. Эту строку передать в json.loads и полученный словарь вывести на экран
dict_1 = json.loads(json_string_1)
# print(dict_1)
dict_2 = json.loads(json_string_2)
# print(dict_2)

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
        "setting3": 0,
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

# 1. Прочитать содержимое файлов (2 переменных) - весь файл в одной
# переменной (одна строка)

json_string_3 = json.dumps(data_3)
# print(json_string_1)
json_string_4 = json.dumps(data_4)
# print(json_string_2)

# print(open('file1.json', 'r').read())
# print(open('file2.json', 'r').read())

# 2. Эту строку передать в json.loads и полученный словарь вывести на экран
dict_3 = json.loads(json_string_3)
# print(dict_1)
dict_4 = json.loads(json_string_4)
# print(dict_2)



def read_data(path):
    if path.endswith('.json'):
        with open(path, 'r') as json_file:
            return json.loads(json_file.read())
    elif path.endswith('.yaml') or path.endswith('.yml'):
        with open(path, 'r') as yaml_file:
            return yaml.load(yaml_file.read(), Loader=yaml.Loader)


def build_diff(dict_1, dict_2):
    list_res = []
    for key in set(list(dict_1.keys()) + list(dict_2.keys())):
        if dict_1.get(key) == 0 and not dict_1.get(key) is False:
            dict_1[key] = 'null'
        if dict_2.get(key) == 0 and not dict_2.get(key) is False:
            dict_2[key] = 'null'
        if key not in dict_2:
            list_res.append({"key": key, "action": "deleted", "old_value": dict_1[key]})
        elif key in dict_2 and dict_1.get(key) != dict_2[key] and isinstance(dict_1.get(key), dict) and isinstance(
                dict_2.get(key), dict):
            list_res.append({"key": key, "action": "nested", "children": build_diff(dict_1.get(key), dict_2.get(key))})
        elif key not in dict_1:
            list_res.append({"key": key, "action": "added", "new_value": dict_2[key]})
        elif key in dict_2 and dict_1.get(key) != dict_2[key]:
            list_res.append({"key": key, "action": "changed", "old_value": dict_1.get(key), "new_value": dict_2[key]})
        elif key in dict_2 and dict_1.get(key) == dict_2[key]:
            list_res.append({"key": key, "action": "unchanged", "value": dict_1.get(key)})

        list_res.sort(key=lambda x: x.get("key"))
    return list_res


def generate_diff(file_path1, file_path2):
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)
    return build_diff(data1, data2)


def main():
    args = parse_args()
    if args.format == 'json':
        print(format_json(generate_diff(args.first_file, args.second_file)))
    if args.format == 'stylish':
        print(format_stylish(generate_diff(args.first_file, args.second_file)))
    if args.format == 'plain':
        print(format_plain(generate_diff(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()
