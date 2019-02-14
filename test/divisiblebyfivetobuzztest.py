import unittest

from src.evil_fizz_buzz import EvilFizzBuzz


class DivisibleByFiveToBuzzTest(unittest.TestCase):

    def test_five_turns_into_buzz(self):
        fizz = EvilFizzBuzz()
        self.assertEqual("buzz", fizz.convert(5))

    def test_six_does_not_turn_into_buzz(self):
        fizz = EvilFizzBuzz()
        self.assertNotEqual("buzz", fizz.convert(6))

    def test_tes_turns_into_buzz(self):
        fizz = EvilFizzBuzz()
        self.assertEqual("buzz", fizz.convert(10))




if __name__ == "__main__":
    unittest.main()
