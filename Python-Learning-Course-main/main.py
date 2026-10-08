"""1.
collection = [] #list
is_start = True #flag

while (is_start):
    print("1 - показать заметки | 2 - добавить заметку")
    choice_user = input('Введите ваш выбор (1 или 2)')
    match int(choice_user):
        case 1:
            print(collection)
        case 2:
            collection.append('task')
            print(collection)
        case _:
            print('Такого пункта нет!')

2.
import os
import sys
import platform
import datetime

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
os_processor = platform.processor()
os_machine = platform.machine()
os_python_version = platform.python_version()
os_android = platform.android_ver()

now = datetime.datetime.now()
sys_in = sys.path
sys_platform = sys.platform
sys_version = sys.version

print(f"{os_name} \n" 
      f"{os_version} \n" 
      f"{os_arch} \n" 
      f"{now.year} \n" 
      f"{now.month} \n" 
      f"{now.day} \n" 
      f"{now.hour} \n"
      f"{now.minute} \n"
      f"{now.second} \n"
      f"{now.microsecond} \n" 
      f"{os_processor} \n" 
      f"{os_machine} \n" 
      f"{os_python_version} \n" 
      f"{os_android} \n")

Код выводит данные компьютера, такие как его имя, версия оп, время и т.д.



 Приложение Task Manager
==============================================================
    Консольное приложение - менеджер управления заметок,
    пользователь может создать заметки, редактировать,
    посмотреть все заметки или удалить выбранную.
==============================================================
~~~~~~~~~~~~~~~~~~~~~
| version app 0.0.7 |
~~~~~~~~~~~~~~~~~~~~~
v0.0.1: заложена базовая структура приложения, использован подход структурного программирования.
v0.0.2: реализована базовая работа с вводом и выводом — пользователь может вводить данные, а система — отображать результаты.
v0.0.3: логика цикла переработана с применением принципов функционального программирования.
v0.0.4: добавлены механизмы валидации и подтверждения операций, чтобы снизить риск случайных действий.
v0.0.5: внедрена файловая подсистема: данные можно сохранять в файл и загружать обратно.
v0.0.6: операции над задачами (создание, изменение, удаление) оформлены в виде отдельных методов — это улучшило читаемость и поддерживаемость кода.
v0.0.7: точка входа в программу вынесена в отдельный метод main, что сделало архитектуру понятнее.
v0.0.8: расширен формат задачи: теперь она включает имя автора и текстовое содержание.
v0.0.9: код разбит на модули для лучшей организации и масштабирования.
v0.1.0: завершена подготовка документации и сборка финальной версии приложения.
"""

# import processes

import app

if __name__ == "__main__":
    app.app()
