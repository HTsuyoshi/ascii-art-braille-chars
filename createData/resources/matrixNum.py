def to_num(matrix, chars_per_line):
    num_array = [0] * chars_per_line 

    line_size = len(matrix)
    column_size = len(matrix[0])

    for i in range(line_size):
        for j in range(column_size):
            if matrix[i][j] != 255:
                num_array[i // 2] = num_array[i // 2] + 2 ** ((j * 2) + (i % 2))

    return num_array
