# 1. Create a decorator that prints to the console the name of the function that was called.
# The function should work as intended. For example, create a pair of functions
# for the arithmetic operations of summation and multiplication. When calling these functions,
# the result of the operation must be returned and the name of the function that was called
# must be displayed in the console with the result. Small hint (__name__)


def print_name_of_function(func):

    def wrapper(left_operand: int, right_operand: int):
        return f'The {func.__name__} returns {func(left_operand, right_operand)}'

    return wrapper


@print_name_of_function
def add_two_numbers(left_operand: int, right_operand: int):
    if isinstance(left_operand, int) and isinstance(right_operand, int):
        return left_operand + right_operand
    else:
        return 'Please use integers to call add_two_numbers function'


@print_name_of_function
def multiply_two_numbers(left_operand: int, right_operand: int):
    if isinstance(left_operand, int) and isinstance(right_operand, int):
        return left_operand * right_operand
    else:
        return 'Please use integers to call add_two_numbers function'


if __name__ == '__main__':
    print(add_two_numbers(10, -3))
    print(multiply_two_numbers(3, 11))
