def validAnagram(str1, str2):
    if len(str1) != len(str2):
        return False

    for char in str1:
        char = char.lower()
        if str1.lower().count(char) != str2.lower().count(char):
            return False

    return True



# print(validAnagram("arr", "rra"))
# print(validAnagram('', '')) #// true
# validAnagram('aaz', 'zaa')# // true
# print(validAnagram('anagram', 'nagaram')) #// true
# print(validAnagram("rat","car")) #// false) // false
# print(validAnagram('awesome', 'awesom')) #// false
# print(validAnagram('amanaplanacanalpanama', 'acanalmanplanpamana')) #// false
# print(validAnagram('qwerty', 'qeywrt')) #// true
print(validAnagram('texttwisttime', 'Timetwisttext')) #// true