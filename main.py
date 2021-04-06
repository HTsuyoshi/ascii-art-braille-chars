import convertImg, strings
import PIL.Image

def resize_image(image, new_width):
    width, height = image.size
    new_height = int(new_width * (height / width))
    new_image = image.resize((new_width, new_height))
    return new_image

def receive_int(integer, exception1, exception2, limit=9999):
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
    new_image_width = receive_int(new_image_width, strings.exception1, strings.exception8)

    image = resize_image(image, new_image_width)


    relative = set_default(input(strings.choose2),'y')
    if relative != 'y' and RGB != 'n':
        raise Exception(strings.exception5)

    if relative == 'n':
        boundary = set_default(input(strings.boundary1), '128')
        boundary = receive_int(boundary, strings.exception2, strings.exception3, 255)

    boundaryhl = set_default(input(strings.boundary2), 'h')
    if boundaryhl != 'h' and boundaryhl != 'l':
        raise Exception(strings.exception4)

    width, height = image.size
    ascii_art = ""

    if relative == 'y':
        px_array = normal_pixels(image)
        boundary = convertImg.calculate_boundary(px_array)
        px_array = gray_pixels(image)
        ascii_art = convertImg.px_ascii_art(px_array, width, height, boundary, boundaryhl)
    else:
        px_array = gray_pixels(image)
        ascii_art = convertImg.px_ascii_art(px_array, width, height, boundary, boundaryhl)


    output_file = open('waifu.txt', 'w')
    output_file.write(ascii_art)

    print(ascii_art)
