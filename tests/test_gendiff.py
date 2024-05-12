import pytest
from gendiff.parser import gendiff

files = [('tests/fixtures/file3.json', 'tests/fixtures/file4.json'),
         ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml')]

formatters = ['stylish', 'plain', 'json']

with (open('tests/fixtures/nested_stylish.txt', 'r') as nested_stylish,
      open('tests/fixtures/nested_plain.txt', 'r') as nested_plain,
      open('tests/fixtures/nested_json.txt', 'r') as nested_json):
    expected_results = [
        nested_stylish.read(), nested_plain.read(), nested_json.read()]


@pytest.mark.parametrize('file_1, file_2', files)
@pytest.mark.parametrize("form, expected", [
    (formatters[0], expected_results[0]),
    (formatters[1], expected_results[1]),
    (formatters[2], expected_results[2])
])
def test_gendiff(file_1, file_2, form, expected):
    assert gendiff(file_1, file_2, form) == expected
