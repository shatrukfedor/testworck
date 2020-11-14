import random
import string
import xml.etree.ElementTree as xml

LENGTH_STRING = 9
MIN_INT = 1
MAX_INT = 100
used_strings = []


def get_random_string(length: int) -> str:
    """
    Возвращает рандомную строку
    :param length: длина рандомной строки
    :type length: int
    :return: рандомная строка
    """
    return ''.join(random.choices(string.ascii_uppercase, k=length))


def create_xml(file_name: str):
    """Создает xml файл"""
    global used_strings
    root = xml.Element('root')
    id = xml.Element('id')
    while True:
        value = get_random_string(LENGTH_STRING)
        if value not in used_strings:
            id.text = value
            used_strings.append(value)
            break
    root.append(id)
    level = xml.Element('level')
    level.text = str(random.randint(MIN_INT, MAX_INT))
    root.append(level)
    objects = xml.Element('objects')
    for i in range(random.randint(1, 10)):
        xml.SubElement(objects, get_random_string(LENGTH_STRING))
    root.append(objects)
    tree = xml.ElementTree(root)
    tree.write(file_name)

