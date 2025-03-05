def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    if len(s) == 0:
        return False

    opcl = dict(('()', '{}', '[]'))

    stack = []

    for i in s:
        if len(stack):
            print(len(stack), "HERE" + opcl[stack.pop()] )
        if i in '({[':
            print(i, i in '({[')
            stack.append(i)
        elif len(stack) == 0 or i != opcl[stack.pop()]:
            return False

    return len(stack) == 0

# print(isValid('())'))
print(isValid("(()){}[])"))
        