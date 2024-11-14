def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(70, 'не строка', False)
print_params(27, 'Ozzy Osborn')
print_params(b = 'пастэль')
print_params(b = 25)
print_params(c = [1, 2, 3])
print()

values_list = [756, 'студент', True]
values_dict = {'a': 234, 'b': 'входной билет', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print('The End')
