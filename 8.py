from datetime import datetime


class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.is_available = True

    def show_info(self):
        status = "Mavjud" if self.is_available else "Band"
        print(f"Kitob: {self.title}")
        print(f"Muallif: {self.author}")
        print(f"Yil: {self.year}")
        print(f"Sahifalar: {self.pages}")
        print(f"Holati: {status}")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print("Kitob muvaffaqiyatli olindi.")
        else:
            print("Bu kitob hozir mavjud emas.")

    def return_book(self):
        self.is_available = True
        print("Kitob muvaffaqiyatli qaytarildi.")

    def check_status(self):
        if self.is_available:
            print("Kitob mavjud")
        else:
            print("Kitob band")

    def is_old_book(self):
        current_year = datetime.now().year
        if current_year - self.year > 10:
            print("Eski kitob")
        else:
            print("Yangi kitob")


book1 = Book("Python asoslari", "Ali Valiyev", 2025, 350)
book2 = Book("O'tkan kunlar", "Abdulla Qodiriy", 1926, 400)
book3 = Book("Clean Code", "Robert C. Martin", 2008, 464)
book4 = Book("Algoritmlar", "Sardor Karimov", 2022, 280)

book1.show_info()
book1.borrow_book()
book1.borrow_book()
book1.check_status()
book1.return_book()
book1.check_status()
book1.is_old_book()

print()

book2.show_info()
book2.is_old_book()

print()

book3.show_info()
book3.borrow_book()
book3.check_status()
book3.is_old_book()

print()

book4.show_info()
book4.is_old_book()