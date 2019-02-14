class EvilFizzBuzz:
    def compute(self):
        comma_delimited_string = "1"
        for i in range(2, 100):
            comma_delimited_string += ("," + self.convert(i))

        return comma_delimited_string

    def convert(self, i):
        if i % 5 == 0:
            return "buzz"
        return str(i)
