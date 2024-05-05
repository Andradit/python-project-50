#!/usr/bin/env python3
from gendiff.parser import gendiff
from gendiff.parser import parse_args


def main():
    args = parse_args()
    form = args.format
    print(gendiff(args.first_file, args.second_file, form))
    return 0


if __name__ == '__main__':
    main()
