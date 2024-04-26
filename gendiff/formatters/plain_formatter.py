def format_key(key, path=None):
    if path is None:
        return key
    return f'{path}.{key}'


def format_bool(result_list):
    for index, string in enumerate(result_list):
        if 'None' in string:
            new_string = string.replace("None", 'null')
            result_list[index] = new_string
        if 'True' in string:
            new_string = string.replace("True", 'true')
            result_list[index] = new_string
        elif 'False' in string:
            new_string = string.replace("False", 'false')
            result_list[index] = new_string


def format_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    return value


def format_nested(value, res_list, dict_list_item, path_name):
    if value == 'nested':
        res_list.append(format_plain(dict_list_item["children"], path_name))


def format_deleted(value, res_list, path_name):
    if value == 'deleted':
        string = f"Property '{path_name}' was removed"
        res_list.append(string)


def format_changed(value, res_list, dict_list_item, path_name):
    if value == 'changed':

        string = (f"Property '{path_name}' was updated. From "
                  f"{format_value(dict_list_item['old_value'])} to "
                  f"{format_value(dict_list_item['new_value'])}")
        if isinstance(dict_list_item['old_value'], dict):
            string = (f"Property '{path_name}' was updated. From "
                      f"[complex value] to "
                      f"{format_value(dict_list_item['new_value'])}")
        if isinstance(dict_list_item['new_value'], dict):
            string = (f"Property '{path_name}' was updated. From "
                      f"{format_value(dict_list_item['old_value'])} to "
                      f"[complex value]")
        res_list.append(string)


def format_added(value, res_list, dict_list_item, path_name):
    if value == 'added':
        string = (f"Property '{path_name}' was added with value: "
                  f"{format_value(dict_list_item['new_value'])}")
        if isinstance(dict_list_item['new_value'], dict):
            string = (f"Property '{path_name}' was added with value: "
                      f"[complex value]")
        res_list.append(string)


def format_plain(func_out_res, parent_key=None):
    res_list = []

    for dict_list_item in func_out_res:
        for key, value in dict_list_item.items():
            path_name = format_key(dict_list_item['key'], parent_key)
            format_nested(value, res_list, dict_list_item, path_name)
            format_deleted(value, res_list, path_name)
            format_changed(value, res_list, dict_list_item, path_name)
            format_added(value, res_list, dict_list_item, path_name)

    format_bool(res_list)

    return '\n'.join(res_list)
