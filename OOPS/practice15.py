from abc import ABC ,abstractmethod

class Employee (ABC):
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def salary(self):
        pass

class SoftwareEngineer(Employee):
    def work(self):
        print("Coding.....")

    def salary(self):
        print("Salary:50000")

e=SoftwareEngineer()
e.work()
e.salary()