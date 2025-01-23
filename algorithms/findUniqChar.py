def firstUniqChar(str: str):
    # if type(str) is not str:
    #     raise ValueError('Value is not string')
    if len(str) == 0:
        raise ValueError('Nothing here')

    collection = dict({})
    for key in str:
        collection[key] = (collection.get(key, 0) +
                           1) if key in collection else 1

    for index in range(len(str)):
        char = str[index]
        if collection[char] == 1:
            return {"char": char, "index": index}

    return -1


# firstUniqChar("leetcode")
print(firstUniqChar("loveleetcode"))
# firstUniqChar("aabb")
