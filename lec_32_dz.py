import os
import shutil


while True:
    come = input('Чтобы начать, напишите - YES : ')
    if come == 'YES':
        print('= = = Содержание текущей директории = = =')
        for item in os.listdir():
            print(item)
        print('_________________________________________')
        print('= = = Файловий менеджер = = =')
        print(' STOP - Закрыть программу')
        print(' NEW FILE - Создать новый файл')
        print(' NEW FOLDER - Создать новую папку')
        print(' RENAME - Переименовать файл или папку')
        print(' DELETE FILE - Удалить файл')
        print(' DELETE FOLDER - Удалить папку')
        print(' COPY FILE - Копировать файл')
        print(' COPY FOLDER - Копировать папку')
        print(' RELOCATE - Переместить файл/папку')
    else:
        print('Выход из программы ')
    manage = input('-- Какое действие вы хотите совершить? -- ')
    if manage == 'NEW FILE':
        name_new = input('Имя создаваемого файла: ')
        with open(name_new, 'w') as file:
            print('Создан')
            file.close()
    if manage == 'NEW FOLDER':
        folder_name = input('Имя создаваемой папки: ')
        os.mkdir(folder_name)
    if manage == 'RENAME':
        name_rename = input('Введите имя файла, который надо переименовать: ')
        name = input('Введите новое имя файла: ')
        if os.path.exists(name) == True:
            print('Такое имя уже есть')
        else:
            os.rename(name_rename, name)
            print('Готово')
    if manage == 'DELETE FILE':
        name_delete = input('Имя удаляемого файла: ')
        os.remove(name_delete)
    if manage == 'DELETE FOLDER':
        name_delete = input('Имя удаляемого файла: ')
        os.rmdir(name_delete)
    if manage == 'COPY FILE':
        name_copy = input('Имя файла для копирования:')
        name, extension = name_copy.split('.')
        shutil.copy(name_copy, "{}-копия.{}".format(name, extension))
    if manage == 'RELOCATE':
        name_reloc = input('Имя файла для перемещения:')
        reloc_address = input('Новое расположение файла:')
        shutil.move(name_reloc, reloc_address)
    if manage == 'STOP':
        break