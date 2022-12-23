from my_fancs.file_workers import read_from_file
import pytest


def create_test_data(test_data):
    with open("tests/test_file.txt", 'a') as f_o:
        f_o.writelines(test_data)

#фикстура - штука которая проганяется в начале каждого теста, пишется в спец. файле


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/test_file.txt")


def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/test_file.txt")
