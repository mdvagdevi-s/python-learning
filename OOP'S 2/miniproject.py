from abc import ABC,abstractmethod

class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.__price=price
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
    def get_price(self):
        print("Price:",self.__price)

    @staticmethod
    def is_expensive(__price): 
        if __price>500:
            return "Expensive"
        else:
            return "Affordable" 
class library(ABC):
        @abstractmethod
        def issue_book(self):
            pass

class college_library(library):
    def issue_book(self):
        print("Book is issued")

        
b=book("Practice Quetions","Vagdevi",1000)
b.display()  
b.get_price()

print(book.is_expensive(1000))

l=college_library()
l.issue_book()



