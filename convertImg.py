import data
import numpy

def to_num(matrix, chars_per_line, boundary):
    num_array = [0] * chars_per_line

    line_size = len(matrix)
    column_size = len(matrix[0])

    for i in range(line_size):
        for j in range(column_size):
            if matrix[i][j] > boundary:
                num_array[i // 2] = num_array[i // 2] + 2 ** ((j * 2) + (i % 2))

    return num_array

def to_matrix(array, height_index, width):
    matrix = numpy.zeros((width, 4))
    array_index = 0 + height_index * width
    for j in range(4):
        for i in range(width):
            matrix[i][j] = array[array_index]
            array_index = array_index + 1
    return matrix

def px_ascii_art(array, width, height):

    width = width - width % 2
    height = height - height % 4
    number_of_lines = height // 4
    ascii_art = ""
    boundary = 128

    height_index = 0
    while number_of_lines > 0:
        matrix = to_matrix(array, height_index, width)
        num_array = to_num(matrix, width // 2, boundary)
        
        for number in num_array:
            ascii_art = ascii_art + chr(data.braileData.get(number))

        ascii_art = ascii_art + "\n"
        height_index = height_index + 4
        number_of_lines = number_of_lines - 1

    return ascii_art
