
# DEL_STRING = 'Property "path_name" was removed'
# UPD_STRING = 'Property "path_name" was updated. From "old_value" to "new_value"'
# ADD_STRING = 'Property "path_name" was added with value: "new_value"'

def format_key(key, path=None):
    if path is None:
        return key
    return f'{path}.{key}'


def format_plain(func_out_res, parent_key=None):
    res_list = []
    for dict_list_item in func_out_res:
        for key, value in dict_list_item.items():
            path_name = format_key(dict_list_item['key'], parent_key)
            if value == 'nested':
                res_list.append(format_plain(dict_list_item["children"], path_name))
            if value == 'deleted':
                # string = DEL_STRING.replace('path_name', path_name)
                string = f"Property '{path_name}' was removed"
                res_list.append(string)
            if value == 'changed':
                # string = UPD_STRING.replace('path_name', path_name)
                # string = UPD_STRING.replace('old_value',
                #                             f"{dict_list_item['old_value']}")
                # string = UPD_STRING.replace('new_value',
                #                             f"{dict_list_item['new_value']}")
                string = (
                    f"Property '{path_name}' was updated. From '{dict_list_item['old_value']}' to '"
                    f"{dict_list_item['new_value']}'")
                if isinstance(dict_list_item['old_value'], dict):
                    # string = UPD_STRING.replace(f"{dict_list_item['old_value']}", '[complex value]')
                    string = (
                        f"Property '{path_name}' was updated. From [complex value] to '"
                        f"{dict_list_item['new_value']}'")
                if isinstance(dict_list_item['new_value'], dict):
                    # string = UPD_STRING.replace(
                    #     f"{dict_list_item['new_value']}", '[complex value]')
                    string = (
                        f"Property '{path_name}' was updated. From '{dict_list_item['old_value']}' to "
                        f"[complex value]")
                res_list.append(string)
            if value == 'added':
                # string = ADD_STRING.replace('path_name', f'{path_name}')
                # string = ADD_STRING.replace('new_value', f"{dict_list_item['new_value']}")
                # print(string)
                string = f"Property '{path_name}' was added with value: '{dict_list_item['new_value']}'"
                if isinstance(dict_list_item['new_value'], dict):
                    # string = ADD_STRING.replace('path_name', f'{path_name}')
                    # string = ADD_STRING.replace('new_value',
                    #                             '[complex value]')
                    string = f"Property '{path_name}' was added with value: [complex value]"
                res_list.append(string)
    for index, string in enumerate(res_list):
        if 'null' in string:
            new_string = string.replace("'null'", 'null')
            res_list[index] = new_string
        if 'True' in string:
            new_string = string.replace("'True'", 'true')
            res_list[index] = new_string
        elif 'False' in string:
            new_string = string.replace("'False'", 'false')
            res_list[index] = new_string
    return '\n'.join(res_list)
