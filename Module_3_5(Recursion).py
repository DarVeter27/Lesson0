# создаем функцию get_multiplied_digits с параметром (number)
def get_multiplied_digits(number):
    # создаем переменную str_number присваивая ей строковое значению параметра (number)
    str_number = str(number)
    # создаем переменную first присваивая ей числовое предстваление превого символа из переменной str_number
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if first == 0:
        return 1
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)