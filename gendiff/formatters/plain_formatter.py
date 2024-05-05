def format_key(key, path=None):
    if path is None:
        return key
    return f'{path}.{key}'


def format_bool(value):
    if value is None:
        value = 'null'
    if value is True:
        value = 'true'
    if not value:
        value = 'false'
    return value


def format_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return format_bool(value)


def format_nested(value, value_summary, dictionary_lists, path_name):
    if value == 'nested':
        value_summary.append(
            format_plain(dictionary_lists["children"], path_name))


def format_deleted(value, value_summary, path_name):
    if value == 'deleted':
        result = f"Property '{path_name}' was removed"
        value_summary.append(result)


def format_changed(value, value_summary, dictionary_lists, path_name):
    if value == 'changed':
        result = (f"Property '{path_name}' was updated. From "
                  f"{format_value(dictionary_lists['old_value'])} to "
                  f"{format_value(dictionary_lists['new_value'])}")
        value_summary.append(result)


def format_added(value, value_summary, dictionary_lists, path_name):
    if value == 'added':
        result = (f"Property '{path_name}' was added with value: "
                  f"{format_value(dictionary_lists['new_value'])}")
        value_summary.append(result)


def format_plain(diff, parent_key=None):
    value_summary = []

    for dictionary_lists in diff:
        for key, value in dictionary_lists.items():
            path_name = format_key(dictionary_lists['key'], parent_key)
            format_nested(value, value_summary, dictionary_lists, path_name)
            format_deleted(value, value_summary, path_name)
            format_changed(value, value_summary, dictionary_lists, path_name)
            format_added(value, value_summary, dictionary_lists, path_name)

    return '\n'.join(value_summary)
