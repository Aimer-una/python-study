from 面向对象三大特性_封装 import Person
class Student(Person):
    def action(self):
        print(f"{self.name} is studying")


class Teacher(Person):
    def action(self):
        print(f"{self.name} is teaching")

def handle_action(person):
    person.action()

if __name__ == "__main__":
    s = Student("张润", 18, "12345678901")
    t = Teacher("林忆宁", 18, "12345678901")
    handle_action(s)
    handle_action(t)
