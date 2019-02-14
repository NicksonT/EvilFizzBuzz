import unittest

from src.evil_fizz_buzz import EvilFizzBuzz


class EvilFizzBuzzTest(unittest.TestCase):
    def test_that_the_first_number_is_one(self):
        evil_fizz_buzz = EvilFizzBuzz()
        comma_delimited_string = evil_fizz_buzz.compute()
        self.assertEqual("1", comma_delimited_string.split(",")[0])

    def test_that_the_second_number_is_two(self):
        evil_fizz_buzz = EvilFizzBuzz()
        comma_delimited_string = evil_fizz_buzz.compute()
        self.assertEqual("2", comma_delimited_string.split(",")[1])

    def test_that_the_third_number_is_Fizz(self):
        evil_fizz_buzz = EvilFizzBuzz()
        comma_delimited_string = evil_fizz_buzz.compute()
        self.assertEqual("Fizz", comma_delimited_string.split(",")[2])

if __name__ == "__main__":
    unittest.main()
