class number:
    @staticmethod
    def is_positive(num):
        if num>0:
            return "Positive"
        else:
            return "Not positive"

print(number.is_positive(-5))