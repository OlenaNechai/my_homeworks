# 2. Create a class with a description of the worker. Any worker. employees.
# I will evaluate the completeness of the described class and will withdraw points for everything unnecessary.
# I want to see clean code. I expect to see clean code with annotations.
# So far, no first-class connections with the second.
# In all methods, I expect to see docstrings with a sane description.

from random import randint


class Worker:

    def __init__(self, name: str, surname: str, position: str, salary: float):
        self.__name = name
        self.__surname = surname
        self.__position = position
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position: str):
        if new_position in ('Employee', 'Lead', 'Manager'):
            self.__position = new_position
        else:
            raise ValueError

    def calculate_new_salary(self):
        performance = randint(1, 100)
        self.__salary *= 1 + performance / 100
        return self.__salary, performance

    def calculate_annual_bonus(self):
        if self.__position == 'Employee':
            return 1000
        elif self.__position == 'Lead':
            return 2000
        else:
            return 3000

    def write_salary_message(self):
        salary, performance = self.calculate_new_salary()
        return f'Dear {self.__name} {self.__surname}!\n' \
               f'Thank you for your hard work in this volatile environment!\n' \
               f'We are happy to inform you, that considering you performance of {performance} ' \
               f'your new salary is increased to be {salary}$\n' \
               f'Your annual bonus is {self.calculate_annual_bonus()}'


if __name__ == '__main__':
    employee = Worker('Harry', 'Potter', 'Employee', 1000)
    print(employee.write_salary_message())
