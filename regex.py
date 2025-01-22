import re

# string = "Hello! My name is Seva. Seva is genius"

# res = re.search(r'S..a$',string )
# # res = re.search('^S..˜a',string )
# res = re.search(r'S..a.$',string )

# # my_pattern = re.compile(r'^Hello.*\.$')
# my_pattern = re.compile(r'S..a')

# # print(my_pattern.search(string))
# print(my_pattern.findall(string))



def check_email(email: str):
    email_regex = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check = re.compile(email_regex)
    validation_result = 'valid' if email_check.fullmatch(email) else 'Not valid'
    return (email, validation_result)


print(check_email("asd@asdasd.com"))