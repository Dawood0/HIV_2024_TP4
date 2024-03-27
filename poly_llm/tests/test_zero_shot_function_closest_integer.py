import unittest
from poly_llm.to_test.closest_integer import closest_integer

class ClosestIntegerTests(unittest.TestCase):
    def test_closest_intger_with_exact_integers(self):
        self.assertEqual(closest_integer('10'), 10)



