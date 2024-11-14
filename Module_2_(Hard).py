def result(number):
    res = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                res += str(i) + str(j)
    return res

print('Введи число из первого поля: ')
print(result(int(input())))
