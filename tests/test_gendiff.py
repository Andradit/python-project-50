import pytest
from gendiff.parser import gendiff

files = [('tests/fixtures/file3.json', 'tests/fixtures/file4.json'),
         ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml')]

with (open('tests/fixtures/nested_stylish.txt', 'r') as nested_stylish,
      open('tests/fixtures/nested_plain.txt', 'r') as nested_plain):
    expected_results = [(nested_stylish.read(), nested_plain.read())]


@pytest.mark.parametrize('file_1, file_2', files)
@pytest.mark.parametrize('expected_1, expected_2', expected_results)
def test_gendiff(file_1, file_2, expected_1, expected_2):
    assert gendiff(file_1, file_2) == expected_1
    assert gendiff(file_1, file_2, 'plain') == expected_2
