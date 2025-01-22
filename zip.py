from zipfile import ZipFile
from pathlib import Path


# Path('my-files').mkdir()

# with open("my-files/first.txt", "w") as my_file:
#     my_file.write('This is first file')

# with open("my-files/second.txt", "w") as my_file:
#     my_file.write('This is second file')

# with ZipFile("my-files.zip", mode='w') as zip_file:
#     print(zip_file)

#     for file in Path('my-files').iterdir():
#         print(file)
#         zip_file.write(file)

with ZipFile("my-files.zip") as zip_file:
    zip_file.extractall('my-files-unzip')