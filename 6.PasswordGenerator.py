import secrets
import string


def contains_upper(pw:str) -> bool:
    """checks if the password contains a uppercase letter"""
    for char in pw:
        if char.isupper():
            return True
    return False

def contains_symbols(pw:str) -> bool:
    """checks if the password contains a symbols"""
    for char in pw:
        if char in string.punctuation:
            return True
    return False

def gen_pw(length: int, symbols:bool, uppercase: bool):
    """
    :param length:
    :param symbols:
    :param uppercase:
    :return:
    """
    comb: str = string.ascii_lowercase + string.digits

    if symbols:
        comb += string.punctuation

    if uppercase:
        comb += string.ascii_uppercase
    comb_len: int = len(comb)
    new_pw: str = ''

    for _ in range(length):
        new_pw += comb[secrets.randbelow(comb_len)]
    return new_pw

if __name__ == '__main__':

    for i in range(1,6):
        new_pw: str = gen_pw(length = 40, symbols = True, uppercase = True)
        specs: str = f'U: {contains_upper(new_pw)}, S: {contains_symbols(new_pw)}'
        print(f'{i} -> {new_pw} ({specs})')



