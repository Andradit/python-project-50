SPACES = '    '
SPACES_DEL = '  - '
SPACES_ADD = '  + '


def str_formatter(value, amount_of_indent):
    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth):
        res_list = ['{']
        for key, v_value in node.items():
            res_list.append(
                f'''{SPACES * depth}{key}: '''
                f'''{walk(v_value, depth + 1)
                if isinstance(v_value, dict) else v_value}'''
            )

        res_list.append(f'{SPACES * (depth - 1)}{"}"}')
        result_string = '\n'.join(res_list)
        return result_string

    return walk(value, depth=amount_of_indent + 2)


def stylish_formatter(func_out_res, depth=0):
    res_list = []

    for dict_list_item in func_out_res:
        for key, value in dict_list_item.items():
            if value == 'deleted':
                res_list.append(
                    f'{SPACES * depth}{SPACES_DEL}{dict_list_item["key"]}:'
                    f' {str_formatter(dict_list_item["old_value"], depth)}')
            elif value == 'nested':
                res_list.append(
                    f'{SPACES * depth}{SPACES}{dict_list_item["key"]}: {"{"}')
                res_list += stylish_formatter(dict_list_item["children"],
                                              depth + 1)
                res_list.append(f'{SPACES * depth}{SPACES}{"}"}')
            elif value == 'changed':
                res_list.append(
                    f'{SPACES * depth}{SPACES_DEL}{dict_list_item["key"]}: '
                    f'{str_formatter(dict_list_item["old_value"], depth)}')
                res_list.append(
                    f'{SPACES * depth}{SPACES_ADD}{dict_list_item["key"]}: '
                    f'{str_formatter(dict_list_item["new_value"], depth)}')
            elif value == 'unchanged':
                res_list.append(
                    f'{SPACES * depth}{SPACES}{dict_list_item["key"]}: '
                    f'{str_formatter(dict_list_item["value"], depth)}')
            elif value == 'added':
                res_list.append(
                    f'{SPACES * depth}{SPACES_ADD}{dict_list_item["key"]}: '
                    f'{str_formatter(dict_list_item["new_value"], depth)}')

    for index, string in enumerate(res_list):
        if 'True' in string:
            new_string = string.replace("True", 'true')
            res_list[index] = new_string
        if 'False' in string:
            new_string = string.replace("False", 'false')
            res_list[index] = new_string

    return res_list


def format_stylish(diff):
    res = stylish_formatter(diff)
    res = ['{'] + res + ['}']
    result_string = '\n'.join(res)
    return result_string
