import convertImg, convertImgRGB, strings
import PIL.Image

def resize_image(image, new_width):
    width, height = image.size
    new_height = int(new_width * (height / width))
    new_image = image.resize((new_width, new_height))
    return new_image

def recieve_int(integer, exception1, exception2, limit=9999):
    if not integer.isnumeric():
        raise Exception(exception1)
    integer = int(integer)
    if integer < 0 or integer > limit:
        raise Exception(exception2)
    return integer

def set_default(string, default_value):
    if string == '':
        return default_value
    else:
        return string

def normal_pixels(image):
    return image.getdata()

def gray_pixels(image):
    return image.convert("L").getdata()

if __name__ == '__main__':
    try:
        image = PIL.Image.open(input(strings.path))
    except:
        print(path, 'File not found')
        exit()

    new_image_width = set_default(input(strings.choose1), '100')
    new_image_width = recieve_int(new_image_width, strings.exception1, strings.exception8)

    image = resize_image(image, new_image_width)

    boundary = set_default(input(strings.boundary1), '128')
    boundary = recieve_int(boundary, strings.exception2, strings.exception3, 255)

    boundaryhl = set_default(input(strings.boundary2), 'h')
    if boundaryhl != 'h' and boundaryhl != 'l':
        raise Exception(strings.exception4)

    RGB = set_default(input(strings.choose2),'n')
    if RGB != 'y' and RGB != 'n':
        raise Exception(strings.exception5)

    red, green, blue = 0, 0, 0
    width, height = image.size
    ascii_art = ""

    if RGB == 'y':
        px_array = normal_pixels(image)
        red = set_default(input(choose_red), '1')
        red = recieve_int(red, strings.exception6, strings.exception7)
        green = set_default(input(choose_green), '1')
        green = recieve_int(green, strings.exception6, strings.exception7)
        blue = set_default(input(choose_blue), '1')
        blue = recieve_int(blue, strings.exception6, strings.exception7)
        rgb_array = [red, green, blue]
        ascii_art = convertImgRGB.px_ascii_art(px_array, width, height, boundary, boundaryhl, rgb_array)
    else:
        px_array = gray_pixels(image)
        ascii_art = convertImg.px_ascii_art(px_array, width, height, boundary, boundaryhl)


    output_file = open('waifu.txt', 'w')
    output_file.write(ascii_art)

    print(ascii_art)
