class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(numbers)

    def __is_valid_vin(selfself, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапозон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


# PRIMER 1
# def greet_person(person_name):
#     if person_name == 'volan de mort':
#         raise Exception("we dont like u volan")
#     print(f'hi, {person_name}')
#
# greet_person('dear student')
# greet_person('volan de mort')

# PRIMER 2
# try:
#     raise NameError('hi there')
# except NameError as exc:
#     print(f'исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}')
#     raise

# PRIMER 3
# class ProZero(Exception):
#     def __init__(self, message, extra_info):
#         self.message = message
#         self.extra_info = extra_info
#
# def f(a, b):
#     if b == 0:
#         raise ProZero("Деление на ноль невозможно", {"a": a, "b": b})
#     return a / b
#
# try:
#     result = f(10, 0)
#     print(result)
# except ProZero as e:
#     print("не очень хороший день - словили ошибку")
#     print(f"сообщение об ошибке: {e.message}")
#     print(f"доп. инфа: {e.extra_info}")

# try:
#     i = 0
#     print(10 // i)
#     print('сделано')
# except ZeroDivisionError:
#     print('нельзя делить на ноль')
#
# try:
#     tru = a + b
#     tru = 10 // 0
# except(ZeroDivisionError, NameError):
#     print('что-то пошло не так, но мы устояли')
#
# try:
#     tru = a + b
#     tru = 10 // 0
# except ZeroDivisionError:
#     print('что-то пошло не так, но мы устояли')
# except NameError:
#     print('не так всё')
#
# try:
#     a = 10 // 0
# except ZeroDivisionError as exc:
#     print(f'что-то пошло не так - {exc} но мы устояли')
#
#
# print('Such a lonely day, and its mine')
# i = int(input('Enter: '))
#
# try:
#     result = 10 * (1 // i)
# except ZeroDivisionError as exc:
#     print('U cant do it', exc)
# else:
#     print('Wow, we dont do it')
# finally:
#     print('Finally, we done :)')
