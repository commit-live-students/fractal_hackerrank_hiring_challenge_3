import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from inspect import getfullargspec
from unittest import TestCase
from ..build import q01_chocolates

input_list_1 = [3, 4, 5, 8, 9, 10]
input_list_2 = [2, 5, 8, 11, 4]
list_chocolates_1 = q01_chocolates(input_list_1)
list_chocolates_2 = q01_chocolates(input_list_2)


class Test_chocolates(TestCase):
    def test_chocolates_args(self):  # Input parameters tests
        args = getfullargspec(q01_chocolates)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_chocolates_type(self):  # Return type tests
        self.assertIsInstance(list_chocolates_1, list,
                              "Expected data is list and you are returning %s" % (type(list_chocolates_1)))

    def test_chocolates_values(self):  # Return value tests
        self.assertListEqual(list_chocolates_1, [3, 3, 8, 8, 17, 17],
                             "Return `List` does not match expected list")

    def test_chocolates_values_1(self):  # Return value tests
        self.assertListEqual(list_chocolates_2, [0, 5, 5, 16, 16],
                             "Return `List` does not match expected List")
