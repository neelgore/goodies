import unittest
from goodies import *
from datetime import date #to test type_as_str

class Test_Binary_Search(unittest.TestCase):

    def setUp(self):
        self.test_lists = [[], list(range(10)), list(range(1000))]
    
    def test_nonexistent_value(self):
        for test_list in self.test_lists:
            self.assertEqual(-1, binary_search(test_list, -1))

    def test_existing_value(self):
        for test_list in self.test_lists:
            for i in test_list:
                self.assertEqual(i, binary_search(test_list, i))

    def test_exists_more_than_once(self):
        self.assertEqual(2, binary_search([0, 1, 2, 3, 2, 4], 2))
        self.assertEqual(0, binary_search([0, 0, 1, 2, 3, 4, 5], 0))
        self.assertEqual(3, binary_search([0, 1, 2, 3, 3], 3))

class Test_Read_File(unittest.TestCase):
    pass

class Test_Type_As_Str(unittest.TestCase):

    def setUp(self):
        self.answers = {int: "int",
                        float: "float",
                        tuple: "tuple",
                        list: "list",
                        dict: "dict",
                        set: "set",
                        str: "str",
                        bool: "bool"}

    def test_method(self):
        for kind in self.answers:
            self.assertEqual(self.answers[kind], type_as_str(kind()))
        self.assertEqual("datetime.date", type_as_str(date(2020, 6, 4)))


if __name__ == "__main__":
    unittest.main()
