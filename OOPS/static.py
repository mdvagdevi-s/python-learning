class Even:
    @staticmethod
    def is_even(num):
        if num%2==0:
            return True
        else:
            return False
print(Even.is_even(5))