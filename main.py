import os
from testworck import services

path = f'{os.getcwd()}{services.SEPARATOR}{services.get_random_string(services.LENGTH_STRING)}'
services.create_new_folder(path)
for i in range(50):
    new_folder_path = f'{path}{services.SEPARATOR}{services.get_random_string(services.LENGTH_STRING)}'
    services.create_new_folder(new_folder_path)
    for itm in range(100):
        file_name = f'{new_folder_path}{services.SEPARATOR}{services.get_random_string(services.LENGTH_STRING)}.xml'
        services.create_xml(file_name)
    services.create_zip_from_folder(f'{new_folder_path}.zip', new_folder_path)
