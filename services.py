import random
import re
import string
import xml.etree.ElementTree as xml
import xml.dom.minidom as minidom
import os
import zipfile
from sys import platform
import csv


if platform == "linux" or platform == "linux2":
    SEPARATOR = "/"
elif platform == "darwin":
    SEPARATOR = "/"
elif platform == "win32":
    SEPARATOR = "\\"

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
    return ''.join(random.choices(string.ascii_letters, k=length))


def create_xml(file_name: str):
    """
    Создает xml файл
    :param file_name: имя файла
    :type file_name: str
    """
    global used_strings
    root = xml.Element('root')
    id_el = xml.Element('id')
    while True:
        value = get_random_string(LENGTH_STRING)
        if value not in used_strings:
            id_el.text = value
            used_strings.append(value)
            break
    root.append(id_el)
    level = xml.Element('level')
    level.text = str(random.randint(MIN_INT, MAX_INT))
    root.append(level)
    objects = xml.Element('objects')
    for i in range(random.randint(1, 10)):
        xml.SubElement(objects, get_random_string(LENGTH_STRING))
    root.append(objects)
    tree = xml.ElementTree(root)
    tree.write(file_name)


def create_zip_from_folder(file_name: str, dir_path: str):
    """
    Архивирует заданную директорию
    :param file_name: имя файла
    :type file_name: str
    :param dir_path: путь к директории для архивации
    :type dir_path: str
    """
    zip_file = zipfile.ZipFile(file_name, 'w')
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            zip_file.write(os.path.join(root, file))
    zip_file.close()


def create_new_folder(path: str):
    """
    Создает новую директорию
    :param path: путь к создаваемой директории
    :type path: str
    """
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)


def get_all_zip_files_from_directory(dir_path: str) -> list:
    '''
    вернет список всех zip файлов из директории
    :param dir_path: абсолютный путь директории
    :type dir_path: str
    :return: список абсолютных путей zip файлов
    '''
    zip_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if re.findall(r'\.zip', file):
                zip_files.append(os.path.join(root, file))
    return zip_files


def xml_parser_from_zip(file_obj: object) -> list:
    """
    парсит xml из zip файла
    :param file_obj: zip file
    :return: list
    """
    parse_list = []
    xml_string = file_obj.read()
    doc = minidom.parseString(xml_string.decode())
    id_el = doc.getElementsByTagName('id')[0].childNodes[0].data
    level = doc.getElementsByTagName('level')[0].childNodes[0].data
    objects = []
    for child in doc.getElementsByTagName('objects')[0].childNodes:
        objects.append(child.nodeName)
    parse_list.append([[id_el, level], [id_el, objects]])
    return parse_list


def csv_append_element(file_name: str, el: list):
    """
    дозаписывает элемент в файл
    :param file_name: путь к файлу
    :type file_name: str
    :param el: элемент для записи
    :type el: list
    """
    with open(file_name, 'a') as file:
        F_N_WRITER = csv.writer(file)
        F_N_WRITER.writerow(el)
