def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ValueError("Nothing to match")

    l = list(zip(*strs))
    prefix = ""

    for i in l:
        if len(set(i)) == 1: # ('f', 'f', 'f') => {'f'} => true, ('o','o','o') => {'o', 'i'} => false
            prefix += i[0]
        else:
            break
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))