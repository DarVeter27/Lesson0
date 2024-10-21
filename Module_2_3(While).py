my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start_index = 0
while start_index <= len(my_list):
    if my_list[start_index] > 0:
        print(my_list[start_index])
        start_index += 1
        continue
    if my_list[start_index] == 0:
        del my_list[start_index]
        continue
    if my_list[start_index] < 0:
        break















