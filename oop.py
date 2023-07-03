# Объектно ориентированное программирование
# 1 : классы \ объекты \ наследование
# на примере описание робота
# класс --- его чертеж = начинка ( характеристики )
# объект --- сам робот созданный по чертежу ( классу )
# наследование --- дорисовываем\добавляем новые опции в чертеж\класс
# полиформизм --- общий функционал , что можно переписать для определенной модели робота , как бы свод правил\законов в определеноой области ооп
# инкапсуляция --- Инкапсуляцию можно считать защитной оболочкой, которая предохраняет код и данные от произвольного доступа со стороны другого кода, находящегося снаружи оболочки. Доступ к коду и данным, находящимся внутри оболочки, строго контролируется тщательно определенным интерфейсом (набором общедоступных, публичных методов).
# вне классов - переменная \ в классах - поле
#
#
#
#
#
###


class Robot: # класс
    model = None
    price = None
    years = None
    isCombat = None

    def set_data(self, model , price , years , isCombat):
        self.model = model
        self.price = price
        self.years = years
        self.isCombat = isCombat

    def get_data(self):
        print('Years of create: ', self.years, '. Model: ', self.model, '. Price: ', self.price)


robot_xa = Robot()
robot_xa.set_data('xa', '52375$', 2027 , False)
print(robot_xa.years, robot_xa.model, robot_xa.price)

robot_xr = Robot() # object 1
robot_xr.model = 'xr'
robot_xr.price = '74500$'
robot_xr.years = 2028
robot_xr.isCombat = False

robot_xrg = Robot() # object 2
robot_xrg.model = 'xrg'
robot_xrg.price = '149000$'
robot_xrg.years = 2030
robot_xrg.isCombat = True

print(robot_xr.years, robot_xr.model, robot_xr.price)
print(robot_xrg.years, robot_xrg.model, robot_xrg.price)

robot_xa.get_data()
robot_xr.get_data()
robot_xrg.get_data()
