### Базовые операции
# print("hello world^ ", 4, 5, 6, ".", sep="", end="\n")
# print("Second line", end='!!!!!!')
# print('HELLO WORLD'+'!!!!!!!!!!!')
# print('Result: ', 5 // 2 , min(3, 2 , -5.3, 4))
# input('Write ur name: ')
# print('Nice to meet u')
### Переменные и типы данных
# short , int , long , char , float , bite , boolean , double
# number = 5.6745 # float
# number1 = -10 # integer
# del number , number1
# boolean = True # bool + = error
# str_num = '5'
# print(number+int(str_num), boolean)
# print(number+number1, boolean)
# del number , number1
# number = 10
# number1 = -265
# print(number1/number)
# word = 'Result: '
# print(word, number1*number)
# У питона нет строгой типизации в джаве все было объектно ориентированно , тут же строго строчка за строчкой работает
# num1 = int(input(' Write first number: ')) #String without int
# num2 = int(input(' Write second number: '))
# num1 += 5
# num2 %= 10
# print("Result: ", num2+num1)
# ('Result: ', num1-num2)
# print('Result: ', num1/num2)
# print('Result: ', num1*num2)
# print('Result: ', num1**num2)
# print('Result: ', num1//num2)
# word = 'Hi' # string
# print(word * 10)
# word = True
### Условные операторы
# if 5 == 5:
#    print('yes',5, sep=' ')
# user_data = int(input('Write 10: '))
# if user_data == 10: # != , >= , <= , == , > , <
#    print('Nice')
# else:
#    print('Are u dumb ? its not 10... ')
# if not user_data > 10:
#    print('its less than 10  ')
# if not user_data < 10:
#    print('its more than 10 ')
# happy = True # False , True
# if happy and user_data == 5 or user_data != 4:
#    print('User is happy')
# elif user_data == 10:
#    print('10')
# else:
#    print('User unhappy')
# data = input()
# if data == 'Five':
#    number = 5
# else:
#    number = 0
#    print(number)
# number = 5 if data == 'FFF' else 0 # тернарные операторы - просто в 1 строку
# print(number)
### Циклы и операторы в них for \ while
# for a in range(6):
#    print(a)
# for i in range(1, 6, 2):
#    print(i)
# word = 'Hello!'
# count = 0
# for a in word:
#    print(a * 10)
#    if a == '!':
#        count += 1
# print('Count: ', count)
# a = 5
# while a <= 15:
#    print(a)
#    a += 0
# hope = True
# while hope:
#    if input('Write stop to end: ') == "Stop":
#            hope = False
# for i in range (1, 11):
#    if i >= 5: # до 5 тк брик
#        break
#    if i % 2 == 0: # % = / т.е в этом цикле выводятся значение которые при деление на 2 дают 0 в остатке
#        continue
#    print(i)
# found = None # 90-97 пример правильного поиска символа в строке
# for i in "hello":
#    if i == 'h':
#        found = True
#        break
#   else:
#        found = False
# print(found)
### Списки (list). Функции и их методы
# nums = [[1, 2, False], 5, 1, 2, 3, 4, 5, 6, True , 'Hi', 1.245]
# nums[1] = 1
# nums[8] = False
# print(nums[0][2])
# numbers = [1, 2, 3]
# numbers.append(100)
# numbers.insert(3, False)
# b = [9, 10]
# numbers.append(b)
# numbers.extend([True, 7, 12, 5])
# numbers.sort()
# numbers.reverse()
# numbers.pop(1)
# numbers.remove(100)
# numbers.clear()
# print(numbers)
# print(numbers.count(5))
# print(len(numbers))
# nums = [1, 5, 10, True]
# for el in nums:
#    el -= 2
#    print(el)
# b = int(input('Enter number: '))
# user_list = []
# a = 0
# while a < b:
#   string = "Enter #"+ str(a+1) + ': '
#   user_list.append(input(string))
#    a += 1
# print(user_list)
### Функции строк . Индексы и срезы







