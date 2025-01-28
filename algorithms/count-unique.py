def countUniqueValues(numbers):
    i = 0
    j = 1

    while j < len(numbers):
        if numbers[i] < numbers[j]:
            i += 1
            numbers[i] = numbers[j]
        j += 1


    return i + 1


# print(countUniqueValues([1, 2, 2, 5, 7, 7, 99]))
# print(countUniqueValues([1,1,1,1,1,2])) # 2
print(countUniqueValues([1,2,3,4,4,4,7,7,12,12,13])) # 7