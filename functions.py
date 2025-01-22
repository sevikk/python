from sys import getsizeof


def sums(a, b):  # None
    a += 4
    c = a + b
    print(c)

# sums(1, 4)


def increasePersonAge(person):
    personCopy = person.copy()
    personCopy['age'] += 1
    return personCopy


personOne = {
    'name': 'Bob',
    'age': 21
}
mewPerson = increasePersonAge(personOne)
# print(personOne['age'])
# print(mewPerson['age'])

# Position arguments


def sumNums(*args):
    print(args)
    print(type(args))
    print(args[1])

    return sum(args)


# print(sumNums(2, 3, 7, 12))

#


def getPostNumbers():
    return 10


def getPostInfo(name, posts_qty=getPostNumbers()): # **kwargs
    return f"{name} wrote {posts_qty} posts"


# print(getPostInfo(name='Seva'))

#


def getPostInfoDict(**person):
    """return Person data string

    Args:
        person (dict): Person Model

    Returns:
        str: _description_
    """
    print(person)
    print(type(person))
    info = (
        f"{person['name']} wrote "
        f"{person.get('posts_qty')} posts"
    )
    return info


# print(getPostInfoDict(name='Seva', posts_qty=35))

#
def print_number_info(num):
    """ Check if number is Even or Odd 

    Args:
        num (int): Number to be evaluated

    Returns:
        None
    """
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def process_number(num, collback_fn):
    collback_fn(num)


# number = int(input("Enter number: "))
# process_number(number, print_number_info)


#
a = 1


def check():
    # global d
    # global a
    d = 10
    a = True
    b = 2
    if (a):
        c = 3
    print(a)
    print(b)
    print(c)
    print(d)


# check()

# print(a)
# print(d)


def outer_function():
    count = 0

    def inner_function():
        nonlocal count
        count += 1
        return count

    return inner_function

my_counter = outer_function()
# print(my_counter())  # Output: 1
# print(my_counter())  # Output: 2


# Операторы

# + - * /
# == != < >
# not, and, or
# =
# is, is not

a = 10
b = a
c = a + b
d = [1, 2]
e = [1, 2]
# print(b is a) # if id is equal
# print(id(b), id(a)) # if id is equal
# print(c is a, id(b), id(a), id(c))
# print(b == a)
# print(d.__eq__(e))

# print(not 0)
# print(not 10)

my_car = {
    'brand': 'honda'
}

# print('brand' in my_car)
# print('year' in my_car)
# print('year' not in my_car)


# Logic
# not, and, or

not 10    # False
not 0     # True
not 'ABC'  # False
not ''    # True
not True  # False
not None  # True

not not 10    # True
not not 0     # False
not not 'ABC'  # True
not not ''    # False
not not True  # True
not not None  # False


red_button = {
    'width': 200,
    'text': 'Buy',
    'color': 'grey',
}
grey_button = {
    'color': 'red',
}
# button = {
#     **red_button,
#     **grey_button
# }
button = red_button | grey_button

# print(red_button)
# print(button)

# STRING Concat

hello = 'Hello'
world = 'World'
concat1 = f'{hello} + {world}'

# print(concat1)

# Lambda

# lambda parameters: expression - anonyms
# lambda in closure

numbers = [1, 2, 3, 4, 5]

numbersMapped = list(map(lambda x: x * x, numbers))
numbersFiltered = list(filter(lambda x: x % 2 == 0, numbers))
# print(numbersMapped)
# print(numbersFiltered)

def mult(a, b):
    return a * b


lambda a, b: a * b


def greeting(greet):
    return lambda name: f"{greet}, {name}"


morning_greeting = greeting("Good Morning")

# print(morning_greeting('Seva'))

evening_greeting = greeting('Good Evening')
# print(evening_greeting('Seva'))


# Try/Except

# try:
#     print(10/1)
# except Exception as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:  # Если ошибки не возникли
#     print("there was no error")
# finally:  # выполняется в любом случае
#     print('Continue...')

# Create error


def devide_nums(a, b):
    if b == 0:
        raise ValueError("Second arg is 0")
    return a / b

# try:
#     devide_nums(10, 0)
# except Exception as e:
#     print(e)
# # except ZeroDivisionError as e:
# #     print(e)
# except TypeError as e:
#     print(e)
# else:  # Если ошибки не возникли
#     print("there was no error")
# finally:  # выполняется в любом случае
#     print('Continue...')


# Unpacked list/tuples
my_fruits = ['apple', 'banana', 'lime']
# my_fruits = ['Seva', '35']
my_fruitsTuple = ('apple', 'banana', 'lime')
numbers = [1, 2, 3]

apple, *remaianing_fruits = my_fruits
apple1, *remaianing_fruits_tuple = my_fruitsTuple


user_profile = {
    'name': 'S'
}


def user_info(name, age=0):
    if not age:
        return f"{name} has no comments"

    return f"{name} is {age} old"


person = {
    'name': 'Bob',
    'age': 21
}
# print(user_info(**person))
# print(user_info(*my_fruits))

# Conditional
# if, if..else, if ... elif

def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Not a number"
    elif a >= b:
        info = f"{a} greater then {b}"
    else:
        info = f"{a} less {b}"
    return info


# print(nums_info(10, 2))
# print(nums_info(True,2))
# print(nums_info(4,15))


my_number = 21
# print('is int') if type(my_number) is int else print("is not int")


# LOOPS
# for ... in, while
my_list = list([1, 2, 3])

# for key, value in personOne.items():
#     print(key, value)

# videos = {1435, 4317, 57567}
# for item in videos:
#     print(item)

# for num in range(5): # Использовать для подключения к серверу например
#     print(num)

# While
i =  10
# while i < 50:
#     print(i)
#     if i == 40:
#         break
#     if i == 30:
#         print("WOW its 30")
#         i += 10
#         continue
#     i += 10

# comprehension loops
all_nums = [-3, 1, 0, 10, -20, -50, 10]

absolute_nums = [abs(num) for num in all_nums]
positive_nums = [num for num in all_nums if num > 0]

# print(absolute_nums)
# print(positive_nums)

my_set = {1, 10, 15}
new_set = {val ** 2 for val in my_set}

# print(new_set)

my_scores = {
    'a': 10,
    'b': 20,
    'c': 5
}

all_nums1 = [1, 0, 10, 10]

new_scores = dict({key: value * 2 for key, value in my_scores.items()})
scores = {index: elem * elem for index, elem in enumerate(all_nums1)}
# scores = {index: elem * elem for index, elem in all_nums}

# print(scores)


# GENERATORS (...)

squares_gen = (num * num for num in range(100))
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

