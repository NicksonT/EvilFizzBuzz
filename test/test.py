import unittest

from src.evil_fizz_buzz import EvilFizzBuzz


class EvilFizzBuzzTest(unittest.TestCase):
    def test_that_the_first_number_is_one(self):
        evil_fizz_buzz = EvilFizzBuzz()
        comma_delimited_string = evil_fizz_buzz.compute()
        self.assertEqual("1", comma_delimited_string[0])

    def test_that_the_second_number_is_two(self):
        evil_fizz_buzz = EvilFizzBuzz()
        comma_delimited_string = evil_fizz_buzz.compute()
        self.assertEqual("1,2", comma_delimited_string[:3])

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
