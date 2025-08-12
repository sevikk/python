from collections import defaultdict

def main():

    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']

    # fruitCounter = defaultdict(int)
    fruitCounter = defaultdict(lambda: 100)

    for fruit in fruits:
        fruitCounter[fruit] += 1

    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))

    pass


if __name__ == "__main__":
    main()