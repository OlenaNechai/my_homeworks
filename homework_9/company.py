# 1. Create a class describing any company. For example, Toshiba or Apple

from random import choice


class Company:
    APPLE_REVENUE_2022 = 387.53
    AVERAGE_STADIUM_CAPACITY = 100000

    def __init__(self, name: str, revenue: float, key_people: list, total_employees: int, products: list = None,
                 services: list = None,
                 ):
        self.__name = name
        self.__revenue = revenue
        self.__products = products
        self.__services = services
        self.__key_people = key_people
        self.__total_employees = total_employees

    @property
    def name(self):
        return self.__name

    @property
    def revenue(self):
        return self.__revenue

    @property
    def key_people(self):
        return self.__key_people

    @property
    def total_employees(self):
        return self.__total_employees

    @total_employees.setter
    def total_employees(self, new_total: int):
        self.__total_employees = new_total

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, new_product: str):
        self.__products.append(new_product)

    @property
    def services(self):
        return self.__services

    @services.setter
    def services(self, new_service: str):
        self.__services.append(new_service)

    def return_one_of_key_people(self):
        key_person = choice(self.__key_people)
        return key_person

    def compare_by_revenue(self):
        if self.__revenue < Company.APPLE_REVENUE_2022:
            difference = round((Company.APPLE_REVENUE_2022 - self.__revenue), 2)
            return f'Revenue of {self.__name} is less than the Apple\'s revenue by ${difference}B!'
        elif self.__revenue == Company.APPLE_REVENUE_2022:
            return f'Are you from Apple?'
        else:
            difference = round((self.__revenue - Company.APPLE_REVENUE_2022), 2)
            key_person = self.return_one_of_key_people()
            return f'Revenue of {self.__name} is more than the Apple\'s revenue by ${difference}B! ' \
                   f'Kudos to {key_person}'

    def calculate_number_of_stadiums(self):
        stadiums_needed = round(self.total_employees / Company.AVERAGE_STADIUM_CAPACITY, 2)
        return f'To have a great all-hands party you need {stadiums_needed} stadium(s)'


if __name__ == '__main__':
    apple = Company(name="Apple", revenue=387.53, key_people=["Tim Cook"], products=['iPhone', 'iPad'],
                    services=['App Store', 'Apple Music'],
                    total_employees=149000)
    result = apple.compare_by_revenue()
    apple.products = 'Mac'
    apple.services = 'Apple TV'

