### Work with files
# file = open('data/text.txt', 'w')  # w = reading , delete and add ( если такого файла не существует w создаёт его )

# file.write('Work\n')
# file.write('Lets go!')

# file.close()

# file = open('data/text.txt', 'a')  # a (upend) = add new info

# file.write(' Work\n')
# file.write('Lets go!\n')

# file.close()

# data = input('Press text: ')
# file = open('data/text.txt', 'a')
#
# file.write(data + '\n')
#
#
# file.close()

# file = open('data/text.txt', 'r') # r = read file in command window
#
# print(file.read())
# for line in file:
#     print(line)
#
# file.close()


# try:
#     file = open('text.txt', 'r')
#     file.read()
# except FileNotFoundError:
#      print('File not found')
# finally:
#     file.close()  # здесь ошибка переменная находиться в трай и файнали её не читает , далее решение

# with...as автоматически закрывает файл поэтому нет надобности в @@@.close()
try:
    with open('text.txt', 'r', encoding='utf-8') as file: # open ( name file , method , кодировка) as "любое имя переменной"
        print(file.read())
except FileNotFoundError:
    print('File not found')
