#!/usr/bin/env python3
import argparse

from gendiff.scripts.generate_diff import generate_diff
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


def gendiff(file_1, file_2, formatter=format_stylish):
    if parse_args().format == 'json':
        formatter = format_json
    if parse_args().format == 'plain':
        formatter = format_plain
    return formatter(generate_diff(file_1, file_2))


def main():
    return gendiff(parse_args().first_file, parse_args().second_file)


if __name__ == '__main__':
    main()
