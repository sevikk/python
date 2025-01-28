def areThereDuplicates(numbers):
    if len(numbers) == 0:
        raise ValueError("No items")
    
    for item in numbers:
        if numbers.count(item) > 1:
            return True

    return False


# print(areThereDuplicates([1, 2, 3])) # // false
# print(areThereDuplicates([1, 2, 2])) # // true
# print(areThereDuplicates(['a', 'b', 'c', 'a'])) #// true
print(areThereDuplicates([]))
