from collections import Counter

def main():

    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah", "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    class2 = ["Bill", "Barry", "Frank", "James", "Joe", "Sam", "Tara"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1["James"])

    print(sum(c1.values()), " sums")

    c1.update(class2)
    print(sum(c1.values()))

    print(c1.most_common(3))

    c1.subtract(class2)

    print(c1)
    print(c1.most_common(3))

    print(c1 & c2)

    pass


if __name__ == "__main__":
    main()