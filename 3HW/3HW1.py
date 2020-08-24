while True:

    def div(*args):
        try:
            arg1 = int(input("Введи делимое "))
            arg2 = int(input("Введи делитель: "))
            res = arg1 / arg2
        except ValueError:
            return 'Ошибка'
        except ZeroDivisionError:
            return "Неправильный пример"

        return res


    print(f'result  {div()}')
    print('----------------------------------')
