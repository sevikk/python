def averagePair(numbers, targer):
    if len(numbers) == 0:
        return False
    
    start = 0
    end = len(numbers) - 1
    while start < end:
        avg = (numbers[start] + numbers[end]) / 2
        if (avg == targer):
            return [True, avg]
        elif avg < targer:
            start = start + 1
        else:
            end = end - 1

    return False

print(averagePair([1,2,3], 2.5)) #// true
print(averagePair([1,3,3,5,6,7,10,12,19],8)) #// true
print(averagePair([-1,0,3,4,5,6], 4.1)) # // false
print(averagePair([],4)) # // false