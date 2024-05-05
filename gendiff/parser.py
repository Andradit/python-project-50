import argparse

from gendiff.engine import generate_diff
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


def gendiff(file_1, file_2, format='stylish'):
    if format == 'json':
        formatter = format_json
    if format == 'plain':
        formatter = format_plain
    if format == 'stylish':
        formatter = format_stylish
    return formatter(generate_diff(file_1, file_2))
