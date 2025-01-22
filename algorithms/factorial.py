def factorial(num: int):
    if type(num) is not int:
        raise ValueError("Is not int")
    if num <= 0:
        raise ValueError("Number should be greater then zero")
    
    if num == 1: return 1
    return factorial( num - 1) * num

print(factorial(4))