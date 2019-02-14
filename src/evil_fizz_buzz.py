class EvilFizzBuzz:
    def compute(self):
        comma_delimited_string = "1"
        for i in range(2, 101):
            comma_delimited_string += ("," + self.convert(i))

        return comma_delimited_string

    def convert(self, i):
        if i % 15 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "buzz"
        return str(i)

    def print(self):
        print(self.compute())
