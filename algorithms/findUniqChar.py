def firstUniqChar(str: str):
    print(type(str), type(str) is not str)
    # if type(str) is not str:
    #     raise ValueError('Value is not string')
    if len(str) == 0:
        raise ValueError('Nothing here')
    
    


# firstUniqChar("leetcode")
firstUniqChar("loveleetcode")
# firstUniqChar("aabb")