def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        empty_list = []
        matrix.append(empty_list)
        for j in range(m):
            empty_list.append(value)
    print(matrix)

get_matrix(2,2,10)
get_matrix(3,5,42)
get_matrix(4,2,13)