from 面向对象三大特性_封装 import Person, Robot
class Student(Person, Robot):
    def __init__(self, name, age, phone, company, name2):
        Person.__init__(self, name, age, phone)
        Robot.__init__(self, company, name2)
    def run(self):
        Person.run(self)
        Robot.run(self)

if __name__ == "__main__":
    s = Student("张润", 18, "12345678901","HUAWEI","TENCENT")
    s.run()
