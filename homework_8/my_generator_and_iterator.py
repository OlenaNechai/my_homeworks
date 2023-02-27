# 2. Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive.
# The solution should work and not freeze your computer.

def my_generator():
    counter = 0
    while counter < 1000000000:
        yield counter
        counter += 1


def my_iterator():
    generator = my_generator()
    list_of_squares = []
    iterator = iter(generator)
    for element in iterator:
        if element % 2 == 0:
            list_of_squares.append(pow(element, 2))
        else:
            continue
    return list_of_squares


if __name__ == '__main__':
    print(my_iterator())
