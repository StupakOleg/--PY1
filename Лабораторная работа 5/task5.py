from string import ascii_uppercase, ascii_lowercase, digits
from random import shuffle, sample


def get_random_password(n: int) -> str:
    code_list = [element for element in sample((ascii_uppercase + ascii_lowercase + digits), n)]
    shuffle(code_list)
    code_string = ''.join(code_list)
    return code_string


print(get_random_password(8))
