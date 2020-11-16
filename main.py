import os
import zipfile

from testworck import services

DIR_PATH = os.getcwd()
OUTPUT_FILE_ID_LEVEL = 'file1.csv'
OUTPUT_FILE_ID_OBJECTS = 'file2.csv'
PATH_FROM_CREATE = f'{os.getcwd()}{services.SEPARATOR}{services.get_random_string(services.LENGTH_STRING)}'
zip_files = []

services.create_new_folder(PATH_FROM_CREATE)
for i in range(50):
    new_folder_path = f'{PATH_FROM_CREATE}{services.SEPARATOR}{services.get_random_string(services.LENGTH_STRING)}'
    services.create_new_folder(new_folder_path)
    for itm in range(100):
        file_name = f'{new_folder_path}{services.SEPARATOR}{services.get_random_string(services.LENGTH_STRING)}.xml'
        services.create_xml(file_name)
    services.create_zip_from_folder(f'{new_folder_path}.zip', new_folder_path)


zip_files = services.get_all_zip_files_from_directory(DIR_PATH)

for file in zip_files:
    zip_el = zipfile.ZipFile(file, 'r')
    for i in range(len(zip_el.filelist)):
        list_from_write = services.xml_parser_from_zip(zip_el.open(zip_el.filelist[i]))
        services.csv_append_element(OUTPUT_FILE_ID_LEVEL, list_from_write[0][0])
        for i in list_from_write[0][1][1]:
            services.csv_append_element(OUTPUT_FILE_ID_OBJECTS, [list_from_write[0][1][0], i])
