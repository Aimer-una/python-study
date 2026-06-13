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

if __name__ == "__main__":
    p = Person("张润", 18, "12345678901")
    p.run()
    print(p.get_phone())
