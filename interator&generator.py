from functions import my_list
from sys import getsizeof

# В Python итератор — это объект, позволяющий перемещаться по коллекции данных по одному элементу за раз.

my_iterator = iter(my_list) # [1, 2, 3]
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator)) # raise StopIteration

# Class with own iterator
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

my_data = MyIterator([1, 2, 3])
# for item in my_data:
#     print(item)

# GENERATORS
# В Python функции-генераторы — это особый тип функций, использующих ключевое слово 'yield'.
# Вместо того чтобы возвращать одно значение, они возвращают итератор, который создает последовательность значений.

""" В Python yield ключевое слово используется для создания функций-генераторов.
Эти функции не возвращают сразу одно значение.
вместо этого они возвращают специальный объект-итератор, который создает последовательность значений на лету. 
"""

squares_gen = (num * num for num in range(10))
# print(type(squares_gen))
# print(list(squares_gen))
# print(getsizeof(squares_gen))


# for elem in squares_gen:
#     print(elem)
#     if elem == 100:
#         break

squares_list = [num * num for num in range(100)]
# print(getsizeof(squares_list))
# print(list(squares_list))


def my_generator(n):
    """Generates a sequence of numbers from 0 to n-1."""
    # for i in range(n):
    #     yield i

    return (num for num in range(n))

# Create a generator object
my_sequence = my_generator(5)
print(type(my_sequence))

# Iterate over the generator
for number in my_sequence:
    print(number)
