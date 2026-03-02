class Student:
    def __init__(self, name, chinese,english,math):
        self.name = name
        self.chinese = chinese
        self.english = english
        self.math = math

    def __str__(self):
        return f"姓名:{self.name} | 语文：{self.chinese} | 数学:{self.math} | 英语:{self.english} | 总分：{self.chinese + self.math + self.english}"

    def update_score(self,chinese = None,english = None,math = None):
        if chinese is not None:
            self.chinese = chinese
        if english is not None:
            self.english = english
        if math is not None:
            self.math = math


if __name__ == '__main__':
    s = Student("张润",99,97,96)
    print(s)
    s.update_score(english=100)
    print(s)


class EduManagement:
    def __init__(self):
        self.students = []

    # 添加学生
    def add_student(self):
        name = input("请输入学生姓名")
        math = int(input("请输入学生数学成绩"))
        chinese = int(input("请输入学生语文成绩"))
        english = int(input("请输入学生英语成绩"))
        # 判断添加的学生是否存在于学生列表中
        for student in self.students:
            if student.name == name:
                print("该学生已经存在请不要重复添加")
                return
        # 判断添加的成绩是否有效
        if 0 <= math <= 100 and 0 <= english <= 100 and 0 <= chinese <= 100:
            self.students.append(Student(name,chinese,english,math))
            print("添加成功")
        else:
            print("传入的成绩不合法")
            return

    def update_student_score(self):
        name = input("请输入学生姓名:")
        # 查询该学生是否存在于学生表中
        for student in self.students:
            if student.name == name:
                print(f"修改前学生成绩:{student}")
                # 修改学生成绩
                math = int(input("请输入学生数学成绩"))
                chinese = int(input("请输入学生语文成绩"))
                english = int(input("请输入学生英语成绩"))
                if 0 <= math <= 100 and 0 <= english <= 100 and 0 <= chinese <= 100:
                    student.update_score(chinese,english,math)
                    print(f"修改后学生成绩:{student}")
                else:
                    print("输入的成绩不合法")
        print("没有查询到该学生")

    def del_student(self):
        name = input("请输入学生姓名:")
        # 查询该学生是否存在于学生表中
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("删除成功")
        print("该学生不存在")

    def get_student(self):
        name = input("请输入学生姓名:")
        # 查询该学生是否存在于学生表中
        for student in self.students:
            if student.name == name:
                print(student)
        print("查询的学生不存在")

    def get_students(self):
        for student in self.students:
            print(student)
if __name__ == '__main__':
    e = EduManagement()
    while True:
        print("""
        1.添加学生成绩
        2.修改学生成绩
        3.删除学生成绩
        4.获取特定学生成绩
        5.获取全部学生成绩
        """)
        choice = input("请选择你要进行的操作1-5:")
        match choice:
            case "1":
                e.add_student()
            case "2":
                e.update_student_score()
            case "3":
                e.del_student()
            case "4":
                e.get_student()
            case "5":
                e.get_students()
            case "_":
                print("操作不合法")

