SPACES = '    '
SPACES_DEL = '  - '
SPACES_ADD = '  + '


def str_formatter(value, amount_of_indent):
    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth):
        res_list = ['{']
        for key, v in node.items():
            res_list.append(
                f'{SPACES * depth}{key}: '
                f'{walk(v, depth + 1) if isinstance(v, dict) else v}')

        res_list.append(f'{SPACES * (depth - 1)}{"}"}')
        result_string = '\n'.join(res_list)
        return result_string

    return walk(value, depth=amount_of_indent + 2)


def format_bool(result_list):
    for index, string in enumerate(result_list):
        if 'None' in string:
            new_string = string.replace("None", 'null')
            result_list[index] = new_string
        if 'True' in string:
            new_string = string.replace("True", 'true')
            result_list[index] = new_string
        if 'False' in string:
            new_string = string.replace("False", 'false')
            result_list[index] = new_string


def format_deleted(value, res_list, depth, dict_list_item):
    if value == 'deleted':
        res_list.append(
            f'{SPACES * depth}{SPACES_DEL}{dict_list_item["key"]}:'
            f' {str_formatter(dict_list_item["old_value"], depth)}')


def format_nested(value, res_list, depth, dict_list_item):
    if value == 'nested':
        res_list.append(
            f'{SPACES * depth}{SPACES}{dict_list_item["key"]}: {"{"}')
        res_list += stylish_formatter(dict_list_item["children"], depth + 1)
        res_list.append(f'{SPACES * depth}{SPACES}{"}"}')


def format_changed(value, res_list, depth, dict_list_item):
    if value == 'changed':
        res_list.append(
            f'{SPACES * depth}{SPACES_DEL}{dict_list_item["key"]}: '
            f'{str_formatter(dict_list_item["old_value"], depth)}')
        res_list.append(
            f'{SPACES * depth}{SPACES_ADD}{dict_list_item["key"]}: '
            f'{str_formatter(dict_list_item["new_value"], depth)}')


def format_unchanged(value, res_list, depth, dict_list_item):
    if value == 'unchanged':
        res_list.append(
            f'{SPACES * depth}{SPACES}{dict_list_item["key"]}: '
            f'{str_formatter(dict_list_item["value"], depth)}')


def format_added(value, res_list, depth, dict_list_item):
    if value == 'added':
        res_list.append(
            f'{SPACES * depth}{SPACES_ADD}{dict_list_item["key"]}: '
            f'{str_formatter(dict_list_item["new_value"], depth)}')


def stylish_formatter(func_out_res, depth=0):
    res_list = []

    for dict_list_item in func_out_res:
        for key, value in dict_list_item.items():
            format_deleted(value, res_list, depth, dict_list_item)
            format_nested(value, res_list, depth, dict_list_item)
            format_changed(value, res_list, depth, dict_list_item)
            format_unchanged(value, res_list, depth, dict_list_item)
            format_added(value, res_list, depth, dict_list_item)

    format_bool(res_list)

    return res_list


def format_stylish(diff):
    res = stylish_formatter(diff)
    res = ['{'] + res + ['}']
    result_string = '\n'.join(res)
    return result_string
