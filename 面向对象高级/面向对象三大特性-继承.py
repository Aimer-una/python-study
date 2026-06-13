from 面向对象三大特性_封装 import Person

class Student(Person):
    pass

if __name__ == "__main__":
    s = Student("张润", 18, "12345678901")
    s.run()
    print(s.name)

