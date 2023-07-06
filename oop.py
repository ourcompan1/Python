# Объектно ориентированное программирование
# 1 : классы \ объекты \ наследование...
# на примере описание робота
# класс --- его чертеж = начинка ( характеристики )
# объект --- сам робот созданный по чертежу ( классу )
# наследование --- дорисовываем\добавляем новые опции в чертеж\класс
# полиформизм --- общий функционал , что можно переписать для определенной модели робота , как бы свод правил\законов в определеноой области ооп
# инкапсуляция --- Инкапсуляцию можно считать защитной оболочкой, которая предохраняет код и данные от произвольного доступа со стороны другого кода, находящегося снаружи оболочки. Доступ к коду и данным, находящимся внутри оболочки, строго контролируется тщательно определенным интерфейсом (набором общедоступных, публичных методов).
# вне классов - переменная \ в классах - поле
# В oop конструктор класса — специальный блок инструкций, вызываемый при создании объекта.
# Переопределение методов --- другими словами установка значений полей по умолчанию в дочерних методах
# __init__ --- конструктор
#
#
###


# class Robot: # класс
#     model = None
#     price = None
#     years = None
#     isCombat = None
#
#     def __init__(self, model={}, price=None, years=None, isCombat=None):
#         self.set_data(model, price, years, isCombat)
#         self.get_data()
#
#     def set_data(self, model, price, years, isCombat):
#         self.model = model
#         self.price = price
#         self.years = years
#         self.isCombat = isCombat
#
#     def get_data(self):
#         print('Years of create: ', self.years, '. Model: ', self.model, '. Price: ', self.price)

#внутри описания теперь пишем тк добавили конструктор позволяющий это сдлеать __unit__
# robot_xa = Robot('xa', 222, 12, True) # object
# robot_xa.set_data('xa', '52375$', 2027 , False)
# print(robot_xa.years, robot_xa.model, robot_xa.price)

# robot_xr = Robot('xr', 1, 2, False) # object
# robot_xr.model = 'xr'
# robot_xr.price = '74500$'
# robot_xr.years = 2028
# robot_xr.isCombat = False

# robot_xrg = Robot('xrg', 2, 4, True) # object
# robot_xrg.model = 'xrg'
# robot_xrg.price = '149000$'
# robot_xrg.years = 2030
# robot_xrg.isCombat = True


# print(robot_xr.years, robot_xr.model, robot_xr.price)
# print(robot_xrg.years, robot_xrg.model, robot_xrg.price)

# robot_xa.get_data() # method
# robot_xr.get_data() # method
# robot_xrg.get_data() # method



### 2
# Класс родителя = супер класс = класс правитель
# Класс наследник наследует все ( методы \ конструкоторы \ поля ) от супер класса
# наследование это надо для простоты чтение кода
# например класс билд имеет функции для здания , а создам класс наследник ( больница ) имеющий все функции здания , но так же добавлю функции конкретно под больницу
# классы наследники , тоже могут иметь наследников
#
#
#

# class build: # общие характерестики в родительском классе
#     __price = None
#     __country = None
#
#     def __init__(self, price=None, country=None):
#         self.price = price
#         self.country = country
#
#     def get_info(self):
#         print('Country: ', self.country, '. Price = ', self.price)
#
#
# class Hospital(build): # общие + доп в классе наследнике ( 2ой супер класс добавить через , нельзя ) = отсуствует множественное наследование в питоне
#     doctors = None
#
#     def __init__(self, doctors=None, price=None, country=None): # если в супер классе было переопределенпие то и в наследнкике тоже так сделать надо
#         super(Hospital, self).__init__(price, country)  # супер ( класс куда пердаем +метод сенлф ).какой метод ( что передаем
#         self.doctors = doctors
#
#     def get_info(self):
#         super(Hospital, self).get_info() # здесь1 --- тут мы сделали так называемый полиформизм
#         print('Workers in hospotal: ', self.doctors)
# class palata(Hospital): # наследник класса госпиталь которые наследует от класса здание
#     beds = None
#
#     def __init__(self, beds=None, doctors=None, price=None, country=None):
#         super(palata, self).__init__(doctors, price, country)
#         self.beds = beds
#
#     def get_info(self): # и здесь1 --- тут мы сделали так называемый полиформизм
#         super(palata, self).get_info()
#         print('V palate: ', self.beds, ' beds.')
# # class camp(build):
# # #     population = 0
# # #     cars = None
# # #
# # #
# # # class home(build):
# # #     pass
# # #
# # home1 = home('15000 $', 'China')
# # home1.get_info()
# # hospital1 = palata(62, 55, '225000 $', 'Portugal')
# # hospital1.get_info()
# # camp1 = camp('6700 $', 'Belarus')
# # camp1.get_info()
# #
# # # home1.get_info()
# # hospital1.get_info()
# # camp1.get_info()



# в питоне икапсуляция сделано не оч ( в супер классе добавляем к началу поля 2 _ --- __прайс)
# как бы защита однако изменить

# hospital1.price = 5 # обрабатываеться коректно
# hospital1.__country = 5 # так тоже , тогда зачем эта недоделанная инкапсулиция
# print(home1.__country) # тут не даёт вывести ( в питоне считаю следует знать такую концепцию , хоть её и не особо то и надо использовать
#
###       iterator --- это объект, который возвращает свои элементы по одному за раз. С точки зрения Python - это любой объект, у которого есть метод__ next__. Этот метод возвращает следующий элемент, если он есть, или возвращает исключение StopIteration, когда элементы закончились. Кроме того, итератор запоминает, на каком объекте он остановился в последнюю итерацию.
#
#
#
#
nums = [10, 3, 5, 7, 'Hello']
i = iter(nums)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

word = 'Tima'
a = iter(word)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

r = range(10, 16)
b = iter(r)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

for a in range(10): # оператор фор пользуется итерацией
   print(a)







