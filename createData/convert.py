import numpy, PIL.Image

line_size = 607
line_amount = 128
chars_per_line = 47
distance1 = 5
distance2 = 8
distance_end_line = 4
skip_line1 = 4
skip_line = 5
alternate_distance = True

def get_grayscale_pixels(name):
    try:
        return PIL.Image.open(name).convert("L").getdata()
    except:
        print("File not found")

def to_num(matrix, chars_per_line):
    num_array = [0] * chars_per_line

    line_size = len(matrix)
    column_size = len(matrix[0])

    for i in range(line_size):
        for j in range(column_size):
            if matrix[i][j] != 255:
                num_array[i // 2] = num_array[i // 2] + 2 ** ((j * 2) + (i % 2))

    return num_array

def print_formated_data(array, file):

    for x in list:
        file.write("\t" + str(x[1]) + ",\n")

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
        start = start + ((line_size) * skip_line1) - distance_end_line

    return matrix

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][0] > arr[j+1][0] :
                arr[j][0], arr[j+1][0] = arr[j+1][0], arr[j][0]
                arr[j][1], arr[j+1][1] = arr[j+1][1], arr[j][1]

if __name__ == '__main__':
    array = get_grayscale_pixels("BCS.png")
    output_file = open("brailleData.py", "w")
    output_file.write("brailleData = [\n")
    list = []

    for line in range(6):

        i = 0
        matrix = get_line_dots(array, 608 + (line_size * 22 * line))
        num_array = to_num(matrix, chars_per_line)
        while(num_array[len(num_array)-1] == 0):
            num_array.pop()
        for x in num_array:
            list.append([x, 10240 + 47 * line + i])
            i += 1

    bubbleSort(list)
    print_formated_data(num_array.sort(), output_file)

    output_file.write("]")
