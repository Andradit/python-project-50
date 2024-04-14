from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    generate_diff('file1.json', 'file2.json')