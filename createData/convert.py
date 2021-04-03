from resources import dataFormat, imgProcess, braille, matrixNum

line_size = 607
line_amount = 128
chars_per_line = 47
distance1 = 5
distance2 = 8
skip_line = 5

alternate_distance = True

if __name__ == '__main__':
    array = imgProcess.get_grayscale_pixels("BCS.png")

    output_file = open("braileData.py", "w")
    output_file.write("braileData = {\n")

    for line in range(6):

        matrix = braille.get_line_dots(array, 608 + (line_size * 22 * line))
        num_array = matrixNum.to_num(matrix, chars_per_line)
        dataFormat.print_formated_data(num_array, output_file, 47 * line)

    output_file.write("}")
