from random import choices
import string


def get_random_string(length: int) -> str:
    """
    Возвращает рандомную строку
    :param length: длина рандомной строки
    :type length: int
    :return: рандомная строка
    """
    return ''.join(choices(string.ascii_uppercase, k=length))
