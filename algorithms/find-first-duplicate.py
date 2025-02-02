def findDublicate(str):
    if len(str) <= 0:
        return "Empty string"
    
    for index, item in enumerate(str):
        if str.count(item) > 1:
            return index
        
    return 'No Duplicates'

print(findDublicate('abqtweryuiot'))