SPACES = '    '
SPACES_DEL = '  - '
SPACES_ADD = '  + '


def format_bool(value):
    if isinstance(value, bool):
        value = str(value).lower()
    return value


def format_str(value, amount_of_indent):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        return format_bool(value)

    def walk(node, depth):
        value_summary = ['{']
        for key, v in node.items():
            value_summary.append(
                f'{SPACES * depth}{key}: '
                f'{walk(v, depth + 1) if isinstance(v, dict) else v}')

        value_summary.append(f'{SPACES * (depth - 1)}{"}"}')
        result = '\n'.join(value_summary)
        return result

    return walk(value, depth=amount_of_indent + 2)


def format_deleted(value, value_summary, depth, dictionary_lists):
    if value == 'deleted':
        value_summary.append(
            f'{SPACES * depth}{SPACES_DEL}{dictionary_lists["key"]}:'
            f' {format_str(dictionary_lists["old_value"], depth)}')


def format_nested(value, value_summary, depth, dictionary_lists):
    if value == 'nested':
        value_summary.append(
            f'{SPACES * depth}{SPACES}{dictionary_lists["key"]}: {"{"}')
        value_summary += stylish_formatter(dictionary_lists["children"],
                                           depth + 1)
        value_summary.append(f'{SPACES * depth}{SPACES}{"}"}')


def format_changed(value, value_summary, depth, dictionary_lists):
    if value == 'changed':
        value_summary.append(
            f'{SPACES * depth}{SPACES_DEL}{dictionary_lists["key"]}: '
            f'{format_str(dictionary_lists["old_value"], depth)}')
        value_summary.append(
            f'{SPACES * depth}{SPACES_ADD}{dictionary_lists["key"]}: '
            f'{format_str(dictionary_lists["new_value"], depth)}')


def format_unchanged(value, value_summary, depth, dictionary_lists):
    if value == 'unchanged':
        value_summary.append(
            f'{SPACES * depth}{SPACES}{dictionary_lists["key"]}: '
            f'{format_str(dictionary_lists["value"], depth)}')


def format_added(value, value_summary, depth, dictionary_lists):
    if value == 'added':
        value_summary.append(
            f'{SPACES * depth}{SPACES_ADD}{dictionary_lists["key"]}: '
            f'{format_str(dictionary_lists["new_value"], depth)}')


def stylish_formatter(func_out_res, depth=0):
    value_summary = []

    for dictionary_lists in func_out_res:
        for key, value in dictionary_lists.items():
            format_deleted(value, value_summary, depth, dictionary_lists)
            format_nested(value, value_summary, depth, dictionary_lists)
            format_changed(value, value_summary, depth, dictionary_lists)
            format_unchanged(value, value_summary, depth, dictionary_lists)
            format_added(value, value_summary, depth, dictionary_lists)

    return value_summary


def format_stylish(diff):
    result = stylish_formatter(diff)
    result = ['{'] + result + ['}']
    return '\n'.join(result)
