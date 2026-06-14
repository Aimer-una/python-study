from abc import ABC, abstractmethod
import json
class Book:
    def __init__(self, book_id, title, author,total_num):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    # 借书
    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    # 还书
    def return_book(self):
        self.__available_num += 1

    # 获取可借阅数量
    def get_available_num(self):
        return self.__available_num



class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.__password = password
        self.__borrowed_books = []


    # 借书
    def borrow_book(self, book):
        # 判断当前会员是否已经借阅了最大数量的图书
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败，你的借阅数量已经到达最大限制")
            return False
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"借阅成功，你已经借阅{book.title}这本书")
            return True
        else:
            print(f"借阅失败，这本书{book.title}已经没有了")
            return False

    # 还书
    def return_book(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
            print(f"还书成功，你已经还了{book.title}这本书")
            return True
        else:
            print(f"还书失败，你没有借阅过这本书{book.title}")
            return False

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books
     
    # 获取最大借阅数量(该方法由子类重写)
    @abstractmethod
    def get_max_books(self) -> int:
        pass
    
    
# 普通会员类
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3


class VipMember(Member):
    def __init__(self, member_id, name, password,vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level


    def get_max_books(self) -> int:
        return 6 + self.vip_level


# 图书管理系统类
class Library_System:
    def __init__(self):
        self.books = {}
        self.members = {}
        # 当前登录的会员
        self.current_member: Member | None = None
        self.load_books_data()
        self.load_members_data()

    # 加载图书数据
    def load_books_data(self):
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book_data in books_data:
                self.books[book_data["编号"]] = Book(book_data["编号"], book_data["标题"], book_data["作者"], book_data["数量"])
    
    # 加载会员数据
    def load_members_data(self):
        with open("data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member_data in members_data:
                if member_data["卡号"].startswith("N"):
                    self.members[member_data["卡号"]] = NormalMember(member_data["卡号"], member_data["姓名"], member_data["密码"])
                else:
                    self.members[member_data["卡号"]] = VipMember(member_data["卡号"], member_data["姓名"], member_data["密码"], member_data["会员等级"])

    def login(self):
        # 判断会员卡号是否存在
        while True:
            member_id = input("请输入会员卡号：")
            if member_id not in self.members:
                print("登录失败，会员卡号不存在！")
                continue
            password = input("请输入密码：")
            member = self.members[member_id]
            if member.get_password() != password:
                print("登录失败，密码错误！")
                continue
            print(f"登录成功！欢迎{member.name}！")
            self.current_member = member
            return True
if __name__ == "__main__":
    library_system = Library_System()
    print(library_system.books)
    print(library_system.members)
    library_system.login()
