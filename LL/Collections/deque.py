import collections
import string

def main():

    d = collections.deque(string.ascii_lowercase)

    print("Items count: ", str(len(d)))

    for elem in d:
        print(elem.upper(), end=",")

    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)

    # print(d)

    d.rotate(10)

    print(d)


    pass


if __name__ == "__main__":
    main()