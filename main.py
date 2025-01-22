from copy import deepcopy

int = 5
floatNumber = 4.3
string = "asdasd"
complexNumber = 3 + 2j
data = {"a": 10, "b": 9} # dictionary
my_list = list([1, 2, 3])
strings = ["123", 'asdad', 'rttrqweqwe', 1, 25, -100, 45]
# my_list1 = my_list
my_list1 = my_list[:]
my_list_test = strings[::-1]
# print(my_list_test)

# my_list1 = my_list.copy()
# my_list1 = list(my_list)
# print(dir(my_list1))
my_list1.append(323)
my_list.append(-1)
my_list.append(-3)
my_list.insert(4, 4)
# my_list.clear()
# print("MY", my_list)
# my_list.sort(reverse=False)
# my_list.sort(reverse=True)
# print(my_list == my_list1)
# print(bool(my_list), dir(my_list1))
def sum(a, b):
    return ["A", a+b, my_list]
# print(sum(1,2))

list1 = ["a", {'a': 10}, 3232, True]
# list1.pop(2)
# list1.sort()

list2 = [1, 2]
list2 = list1 + list2

# print(list2)


# DICT - mutable, Iterable
motor = {'brand': 12} # { ... }
other = {'brand': 12}
motor['price'] = 'AAAA'
price = motor['price']

list3 = [['first', 1], ['second', 2]]
dictionary = dict(list3)
# print(dictionary)
# print(motor.get('braaaaand', "Test"))

# print(dictionary)


# TUPLE - immutable
tupleS = ("a", {'a': 10}, 1, 1, True) # ( ... )
tupleS1 = ("a", 2, 1, 1, True)
tuple2 = tuple(('a', {'a': 20}, 20, 20)) 
# tupleS[0] = 123
# print(tuple2)
# print(tupleS.count(1))
# print(tupleS.index(1))


# SET - mutable, Iterable
sets1 = set({'apple', True, 151, tupleS1}) # ({   })
sets2 = {'apple', True}
sets3 = sets1.copy()
union = sets1.union(sets2)
inters = sets1.intersection(sets2)
inters1 = sets1 & sets2
subset = sets2.issubset(sets1)
sets1.discard('151') # NO ERROR
# sets1.remove('151') # Error if no value
# sets1.add("1")
# sets1.add(1)
# print(inters)
# print(sets1 | sets2) # union with sorting
# print(sets1 & sets2) # intersection
# print((sets1 | sets2) - (sets1 & sets2))


# RANGE
myRange = range(7)
myRange1 = range(10, 30, 3) # (from, to, step)

# print(myRange1[4])
# print(list(myRange1))


# ZIP
zipValue = zip(strings, my_list)

# print(list(zipValue))
# print(tuple(zipValue))
# print(dict(zipVal/ue))


# Change DICTs
info = {
    'name': 'Seva',
    'is_new': True,
    'isChange': []
}

# infoCopy = info.copy()
infoCopy = deepcopy(info)
# infoCopy = {
#     'name': 'Seva TEST',
#     'is_new': False
# }
# info['isChange'] = True
infoCopy['isChange'].append(False)

# print(info)
# print(infoCopy)


my_set = set({1,2,3,4})

frozenset = frozenset(my_set)

my_set.add(5)
# frozenset.add(5)
# print(frozenset)
# print(my_set)

my_list_test = strings[::-1]
print(my_list_test)


# Ternan 
my_number = 21
# print('is int') if type(my_number) is int else print("is not int")
