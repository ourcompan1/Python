### Базовые операции
# print("hello world^ ", 4, 5, 6, ".", sep="", end="\n")
# print("Second line", end='!!!!!!')
# print('HELLO WORLD'+'!!!!!!!!!!!')
# print('Result: ', 5 // 2 , min(3, 2 , -5.3, 4))
# input('Write ur name: ')
# print('Nice to meet u')
# name = 'serge'
# age = 11
# print(f'Hello {name} and ur age is {age}')
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
### Списки (list). Функции и их методы   [][][]
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
# word = 'study'
# word = 'Hi, Hello, Whats_up'
# print(len(word), word[0], word[1], word[2], word[3], word[4])
# print(word.count('s')) # поиск отдельных символов
# print(word.upper() + word.lower())
# print(word.isupper(), word.islower())
# print(word.capitalize())
# print(word.find('y')) # поиск номера символа в листе
# print(word.split(', '))
# words = word.split(', ')
# print(words[2]) # вот как сделать список по другому
# word = 'Hey, Hello, Hi'
# ff = word.split(', ')
# for a in range(len(ff)):
#    ff[a] = ff[a].capitalize()
# result =', '.join(ff)
# print(result)
# word = 'YeSnoTKish' # Index cuts
# print(word[5:-1:2])
# list = [ 5, 7 , 'hello', True]
# print(list[0:3])
##НАПОМИНАЛКА about Type conversion and casting
# Python automatically converts
# d to float as it is a float multiplication
# d = a * b
# print(d)
# print(type(d)) ///
# type Casting
# a = 5.9
# typecast to int
# n = int(a)
# print(n)
# print(type(n)) ///
# string variable
# a = "5.9"
# typecast to float
# n = float(a)
# print(n)
# print(type(n))
### Кортежи - tuple , примерно те же списки только меньше путей и веса ()()()
# tuple = (1, 3, 45, False, 7.4, 'Hello')
# print(tuple[::3])
# print(tuple.count(45))
# print(len(tuple))
# print(tuple)
# tuple = 1, False, True, 5.9
# print(tuple[::1])
# tupl = (1, 3, 45, False, 7.4, 'Hello')
# for i in tupl:
#   print(i)
# nums = [5, 5, 4]
# new_nums = tuple(nums)
# print(new_nums)
# say = tuple('Hi, my name George')
# print(say)
### Словари и функции для работы с ними - dict {}{}{}
# towns = {'Towns': 4} # Ключ : то что после открытия ключом
# print(towns["Towns"])
# country = {'code': 'USA bombs', 'code1': 'Russia bombs', 'populationRU': '62.457.835'}
# print(country['populationRU'])
# country = dict(code='Russian', code1='Usa')
# print(country['code1'])
# country = {'code': 'USA bombs', 'code1': 'Russia bombs'}
# print(country.items())
# for key, opened in country.items():
#    print(key, ' <---> ', opened)
# country = {'code': 'USA bombs', 'code1': 'Russia bombs'}
# print(country.get('code1')) # =[key]
# country.clear()
# country.popitem()
# country.pop('code')
# print(country.values())
# country['code1'] = "They lost it"
# rint(country.keys())
# human = {
#     'Alternative human':{
#         'age': "15-18",
#         'size': 6.3,
#         'iq': "~100~",
#         'is he think like me?': {"YES": 'dont believe', "NO": 'of course'}
#     },
#     'Vika':{
#         '!': "just break up with atrashkov",
#         '!?': "just break up with atrashkov",
#         'is she love him?': ['I D K', '100% NO', False]
#     }
# }
# print(human['Alternative human']['is he think like me?']['YES'])
# print(human['Vika']['is she love him?'])
### Множества <=> set , frozen
# data = set('hi')
# print(data)
# если указываем ключи мы создаем словарь , если нет то множество
# data = {'key', 7 , 6 , 4, 5, 7, 6, 5}
# data.update([35, 98, 'k', True])
# data.add(90)
# data.remove(90)
# data.pop()
# data.clear()
# print(data)
# data = frozenset([5, 4, 5, 6, 7, 120]) # свойство кортежей
# print(data)
### Функции - def - lambda
# def testing_func():
#    print('Hi', end='!')
#    print(' -  hello?')
#    pass # = nothing

# testing_func()

# def test():
#    word = 'Hello!'
#    count = 0
#    for a in word:\
#            print(a * 10)
#    if a == '!':
#         count += 1
#        print('Count: ', count)

# test()

# def test(key):
#    print(key, end='!')


# test('Hello')
# test(111111111888888888888)

# def test_summa(hi, abc):
#    return hi + abc
#    data = hi + abc
#    return data
##   print('Result:  ', data)

##  test_summa(17.33 , 16.67)
# data = test_summa('Hello', "!?")
# print(data)
# print(test_summa(3.33, 6.67))

# def poisk_min(l):
#    minimal = l[0]
#    for b in l:
#        if b < minimal:
#             minimal = b


#    print(minimal)


# spisok10 = [1, 5, 25, 2, 6]
# poisk_min(spisok10)


# spisok1 = [1, 5, 25, 2, 6, 25, 10]
# print(poisk_min(spisok1))

# spisok1 = [1, 5, 25, 2, 0.5, 6]
# min = spisok1[0]
# for i in spisok1:
#     if i < min: # if i > min: = max
#         min = i

# print(min)

## lamda > def
alo_f = lambda a, b: a * b
print(alo_f(100, 3.33))












































































