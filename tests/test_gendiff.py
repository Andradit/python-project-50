from gendiff.scripts.gendiff import gendiff


# file_1 = open('file1.txt', 'r')

# file = open('flat_stylish.txt', 'r')

# @pytest.mark.parametrize()
# def coll():
#     return {'a': {'b': {'c': 3}}}

# @pytest.mark.parametrize('file1.json, file2.json', open('flat_stylish.txt', 'r'))
def test_gendiff():
    assert gendiff('file3.json', 'file4.json') == open(
        'tests/fixtures/nested_stylish.txt', 'r').read()
    assert gendiff('file3.json', 'file4.json', 'plain') == open(
        'tests/fixtures/nested_plain.txt', 'r').read()
