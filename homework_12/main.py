# 2. Describe the Train object.
# The class must contain fields and a method for adding wagons
# (it is necessary to add objects, instances of the wagon class).
# Describe the class Wagon together with the train.
# The Wagon must contain a list of passengers and allow adding passengers.
# In the Wagon can be 10 passengers for example.
# When using the len function on a Wagon, I want to see the number of passengers.
# When using len on a train, I want to see a list of Wagons without a locomotive.
# Each wagon must have a number.
# When printing a wagon to the console, I want to see the following "[n]" where n is the number of the wagon.
# ***
#
# Implement a train print from task 2.
# When you print a train, wagons and a locomotive should be displayed in the console in the following format:
#
# ﻿<=[HEAD]-[1]-[2]-[3]-[4]-[...]-[n]-[n-1]

from homework_12.train import Train
from homework_12.wagon import Wagon

if __name__ == '__main__':
    train = Train()
    print(f'Train length is {len(train)}')
    wagon_1 = Wagon(1, ['Julia', 'Andrew', 'George'])
    wagon_2 = Wagon(2, ['Tim', 'Walt'])
    wagon_3 = Wagon(3, ['Ana'])
    train[1] = str(wagon_1)
    train[2] = str(wagon_2)
    train[3] = str(wagon_3)
    print(f'Train length is {len(train)}')
    print(f'Number of passengers in wagon {wagon_1} is {len(wagon_1)}')
    print(f'Number of passengers in wagon {wagon_2} is {len(wagon_2)}')
    print(f'Number of passengers in wagon {wagon_3} is {len(wagon_3)}')
    print(wagon_1)
    print(wagon_2)
    print(wagon_3)
    wagon_1.__add__('Frodo')
    print(len(wagon_1))
    print(train.form_the_train())
