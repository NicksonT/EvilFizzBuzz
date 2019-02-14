import unittest

from evil_fizz_buzz import EvilFizzBuzz


class Divisible_by_five_to_buzz_test(unittest.TestCase):

    def test_five_turns_into_buzz(self):
        fizz = EvilFizzBuzz()
        self.assertEqual("buzz", fizz.compute(5))

    def test_six_does_not_turn_into_buzz(self):
        fizz = EvilFizzBuzz()
        self.assertNotEqual("buzz", fizz.compute(6))

    def test_tes_turns_into_buzz(self):
        fizz = EvilFizzBuzz()
        self.assertEqual("buzz", fizz.compute(10))




if __name__ == "__main__":
    unittest.main()
