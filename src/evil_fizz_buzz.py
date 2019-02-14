class EvilFizzBuzz:
    def compute(self, number):
        if number % 5 == 0:
            return "buzz"
        return str(number)
