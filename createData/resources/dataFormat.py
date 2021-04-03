def print_formated_data(array, file, index):
    for x in array:
        char_value = str(10240 + index)
        file.write("\t" + str(x) + " : " +  char_value + ",\n")
        index = index + 1

