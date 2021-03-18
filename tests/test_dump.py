from djson.src.djson import DJson
import os


def check(name, value):
    dj = DJson(os.path.join("examples", name))
    assert dj.dump() == value

def test_empty_file():
    check("empty_file", '')

def test_single_file_object():
    check("single_file_object",". name1: value1\n. name2: value2\n. name3: value3\n")

def test_single_file_objarr():
    check("single_file_objarr", ". name1: value1\n. name2: value2\n. name3: value3\n. arr: \n. . #0: element1\n. . #1: element2\n. . #2: element3\n")

def test_single_file_array():
    check("single_file_array", ". #0: element1\n. #1: element2\n. #2: element3\n")

def test_single_file_arrobj():
    check("single_file_arrobj", ". #0: \n. . name: object1\n. . title: Object one\n. #1: \n. . name: object1\n. . title: Object two\n. #2: \n. . name: object3\n. . title: Object three\n")