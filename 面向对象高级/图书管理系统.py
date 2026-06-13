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
    