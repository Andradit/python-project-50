import pytest
from gendiff.parser import gendiff

files = [('tests/fixtures/file3.json', 'tests/fixtures/file4.json'),
         ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml')]


@pytest.mark.parametrize('file_1, file_2', files)
@pytest.mark.parametrize("form, expected", [
    ('stylish', 'tests/fixtures/nested_stylish.txt'),
    ('plain', 'tests/fixtures/nested_plain.txt'),
    ('json', 'tests/fixtures/nested_json.txt')
])
def test_gendiff(file_1, file_2, form, expected):
    with (open(expected, 'r')) as exp:
        assert gendiff(file_1, file_2, form) == exp.read()
