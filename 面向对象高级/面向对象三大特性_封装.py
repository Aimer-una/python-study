"""
注意：python中没有真正的封装，但是通过__来实现的，但是这并不是绝对的，python中的__只是起到了一个命名的混淆作用，
"""
class Person:
    def __init__(self, name, age,phone):
        self.name = name
        self.age = age
        self.__phone = phone

    def get_phone(self):
        return self.__phone

    def run(self):
        print(f"{self.name} is running")
        self.__study()

    def __study(self):
        print(f"{self.name} is studying,hers phone is {self.__phone}")

class Robot:
    def __init__(self,company,name):  
        self.company = company
        self.name = name

    def run(self):
        print(f"{self.company} is running {self.name}")
if __name__ == "__main__":
    p = Person("张润", 18, "12345678901")
    p.run()
    print(p.get_phone())
