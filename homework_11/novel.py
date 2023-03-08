# Please describe an object as we did with Helicopter. Using all OOP postulates. Add comments where you use postulate.
# For example:
# # Inheritance
# class SomeObject(Other_Object)
# def __init__()....
# # hiding
# self.__parameter ...

# Interface, Abstraction, Inheritance
from books import IMeaningful, IReadable


# Inheritance
class Novel(IMeaningful, IReadable):
    my_wish_list = ['Great Novel', 'Good Poem', 'Fairytale']
    highly_recommended_books = ['Wonderful Novel', 'Cool Poem', 'Funny Fairytale']
    books_i_read = []
    not_interesting_books = []

    def __init__(self, book_name: str, pages: int):
        # Hiding
        self.__book_name = book_name
        self.__pages = pages
        self.__current_page = None

    # Encapsulation
    @property
    def book_name(self):
        return self.__book_name

    # Polymorphism
    def _pick_the_book(self):
        if self.__book_name in Novel.my_wish_list:
            return "I will read this book"
        elif self.__book_name in Novel.highly_recommended_books:
            Novel.my_wish_list.append(self.__book_name)
            return "I will read this book next"
        else:
            return "I don't have time for this book"

    # Polymorphism
    def _enjoying(self):
        answer = input(f'Are you enjoying the {self.__book_name}? \n y/n: ')
        return answer

    # Polymorphism
    def _start_reading(self):
        print(f"I am reading {self.__book_name} which has {self.__pages}")
        self.__current_page = 0
        while self.__current_page < self.__pages // 20:
            self.__current_page += 1
            print("I'm reading")
        return self.__current_page

    # Polymorphism
    def _stop_reading(self):
        Novel.my_wish_list.remove(self.__book_name)
        return f"I\'ve read {self.__current_page} of {self.__pages} pages of the novel {self.__book_name}"

    # Encapsulation
    def read(self):
        self._pick_the_book()
        self._start_reading()
        if self._enjoying() == 'y':
            while self.__current_page != self.__pages:
                self.__current_page += 1
                print("I'm still reading")
            Novel.books_i_read.append(self.__book_name)
        else:
            Novel.not_interesting_books.append(self.__book_name)
        return self._stop_reading()
