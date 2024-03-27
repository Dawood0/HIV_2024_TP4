


import pytest
import unittest
from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

class ClosestIntegerTests(unittest.TestCase):
    @staticmethod
    def almost_equal(val1, val2, precision=1e-10):
      return abs(val1 - val2) < precision

    def test_basic_cases(self):
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("10"), 10), f"Expected {closest_integer('10')} to equal 10.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("14.5"), 15), f"Expected {closest_integer('14.5')} to equal 15.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("15.3"), 15), f"Expected {closest_integer('15.3')} to equal 15.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("-14.5"), -15), f"Expected {closest_integer('-14.5')} to equal -15.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("-15.3"), -15), f"Expected {closest_integer('-15.3')} to equal -15.")

    def test_edge_cases(self):
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer(".1"), 0), f"Expected {closest_integer('.1')} to equal 0.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("-.1"), 0), f"Expected {closest_integer('-.1')} to equal 0.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("1."), 1), f"Expected {closest_integer('1.')} to equal 1.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("-1."), -1), f"Expected {closest_integer('-1.')} to equal -1.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("1.0"), 1), f"Expected {closest_integer('1.0')} to equal 1.")
       self.assertTrue(ClosestIntegerTests.almost_equal(closest_integer("-1.0"), -1), f"Expected {closest_integer('-1.0')} to equal -1.")


@pytest.mark.parametrize("filename", [".txt"])
def test_empty_prefix(filename):
    result = file_name_check(filename)
    expected = "No"
    assert result == expected


class FindClosestElementsTest(unittest.TestCase):

    def test_simple_case(self):
        input_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
        output = (2.0, 2.2)
        self.assertTupleEqual(output, find_closest_elements(input_list))

    def test_duplicates(self):
        input_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
        output = (2.0, 2.0)
        self.assertTupleEqual(output, find_closest_elements(input_list))

    def test_negative_values(self):
        input_list = [-1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
        output = (-1.0, 2.0)
        self.assertTupleEqual(output, find_closest_elements(input_list))

import unittest

class NumericalLetterGradeTest(unittest.TestCase):
    def test_all_grades(self):
        input_gpas = [4.0, 3, 1.7, 2, 3.5]
        actual_results = numerical_letter_grade(input_gpas)
        expected_results = ["A+","B","C-","C","A-"]
        
        self.assertListEqual(actual_results,expected_results,"The results do not match")

    def test_single_result(self):
        input_gpas = [1.2]
        actual_results = numerical_letter_grade(input_gpas)
        expected_results = ["D+"]
        
        self.assertListEqual(actual_results,expected_results,"The results do not match")

    
import pytest
from typing import List

@pytest.mark.parametrize("input_data", ["( ) (( )) (( )( ))"])
def test_separate_paren_groups(input_data):
    expected_output = ['()', '(())', '(()())']
    
    actual_output = separate_paren_groups(input_data)
    
    assert actual_output == expected_output