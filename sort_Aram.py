from pprint import pprint
import os

ABSOLUT_NAMES = os.getcwd() 
DIRNAME = 'D:\Арам\Нетология\ДЗ\Сортировка текстов'
files = os.listdir(DIRNAME)
FILES_TXT = 'files_for_sort'
FULL_PATH = os.path.join(DIRNAME, FILES_TXT)
files = os.listdir(FULL_PATH) 

min_max_lines = {}
dict_file = {}
for file in files:
    with open(os.path.join(DIRNAME, FILES_TXT, file), 'r', encoding = 'utf-8') as file_obj:
        min_max_lines[file] = len(file_obj.readlines())
    with open(os.path.join(DIRNAME, FILES_TXT, file), 'r', encoding = 'utf-8') as file_obj:
        dict_file.update({file:file_obj.read()})
        
ascending_line = sorted(min_max_lines.items(), key=lambda item: item[1])

new_file = open('Итоговый файл.txt', 'a', encoding = 'utf-8')
for new_line, len_line in ascending_line:
    end = f"{new_line}\n{str(len_line)}\n{dict_file[new_line]}\n" 
    new_file.write(end.rstrip())
new_file.close
with open(os.path.join(DIRNAME, 'Итоговый файл.txt'), 'r', encoding = 'utf-8') as end_file:
    pprint(end_file.read())




