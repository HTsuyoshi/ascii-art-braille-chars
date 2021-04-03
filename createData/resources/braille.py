import numpy

line_size = 607
line_amount = 128
chars_per_line = 47
distance1 = 5
distance2 = 8
distance_end_line = 4
skip_line = 4


def get_line_dots(array , start):

    matrix = numpy.zeros((chars_per_line * 2, 4))


    for j in range(4):
        alternate_distance = True
        for i in range(chars_per_line * 2):
            matrix[i][j] = array[start]

            if alternate_distance == True:
                start = start + distance1
                alternate_distance = False
            else:
                start = start + distance2
                alternate_distance = True
        start = start + ((line_size) * skip_line) - distance_end_line

    return matrix
