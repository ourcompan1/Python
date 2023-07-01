### конструкции try , except
### обработчики исключений

x = 0
while x == 0:
    try:
        a = int(input('Press number: '))
        a *= 10
        print(a)
    except ValueError:
        print('NUmBer no float no string')
    except TypeError:
        print('Dumb')
    finally:
        print('!')



