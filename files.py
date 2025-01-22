from pathlib import Path

file_path = Path('new.txt')

# print(Path('usr').joinpath('local').joinpath('bin'))
# print(Path('usr') / 'local' / 'bin')

# print(Path('text.txt').exists())
# print(Path('text.txt').is_file())
# print(Path('../').is_dir())

# for f in Path('.').iterdir():
# print(f)

# test_file = open('new.txt', 'w')
# test_file.write("First Line \n")
# test_file.write("Second Line \n")
# test_file.close()

with open('new.txt', 'w') as test_file: # "a", "w"
    test_file.write("First Line \n")
    test_file.write("Second Line \n")
    test_file.write("Third Line \n")

with open('new.txt') as test_file:
    # print(test_file.read())
    # print(test_file.readlines())
    for line in test_file:
        print(line)

with open('new.txt') as test_file:
    while True:
        line = test_file.readline()
        print(line)
        if not line:
            break


if file_path.exists():
    file_path.unlink()