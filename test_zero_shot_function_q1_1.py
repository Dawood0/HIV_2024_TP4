import unittest
from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups
from unittest import TestCase




class ClosestIntegerTests(unittest.TestCase):
    def test_closest_intger_with_exact_integers(self):
        self.assertEqual(closest_integer('10'), 10)


class TestFileNameCheck(unittest.TestCase):
    def test_valid_names(self):
        self.assertEqual(file_name_check('example.txt'), 'Yes')
        self.assertEqual(file_name_check('myFile.exe'), 'Yes')
        self.assertEqual(file_name_check('helloWorld.dll'), 'Yes')
        self.assertEqual(file_name_check('abcde1fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.dll'), 'Yes')
    


class FindClosestElementsTests(unittest.TestCase):
    def test_simple_case(self):
        elements = [1., 2., 3.]
        expected = (1., 2.)
        
        actual = find_closest_elements(elements)
        
        self.assertTupleEqual(actual, expected, msg="Expected {} but got {} instead!".format(expected, actual))


class NumericalLetterGradeTests(unittest.TestCase):
    def test_single_student(self):
        grades = [3.5]
        expected = ["A-"]
        
        actual = numerical_letter_grade(grades)
        
        self.assertListEqual(actual, expected, msg=f"Expected {expected}, but got {actual}.")


class ParenthesisSeparatorTests(unittest.TestCase):
    def test_empty_input(self):
        s = ""
        expected = []
        
        actual = separate_paren_groups(s)
        
        self.assertListEqual(actual, expected, msg="Empty input resulted in non-empty output.")







