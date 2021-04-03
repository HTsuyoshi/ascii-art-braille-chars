import convertImg
import PIL.Image

path = 'Write the path for the file: '
choose = '(Default = 100) Choose the image width: '
boundary1 = '(Default = 128) Choose the boundary (0-255): '
boundary2 = 'Paint if the value is higher (h) or lower (l) than boundary: '
exception1 = 'Width has to be higher than 0'
exception2 = 'Boundary has to be a number'
exception3 = 'Boundary has to be lower than 256 and higher than -1'
exception4 = "The input has to be 'h' or 'l'"

def resize_image(image, new_width):
    width, height = image.size
    new_height = int(new_width * (height / width))
    new_image = image.resize((new_width, new_height))
    return new_image

def gray_pixels(image):
    return image.convert("L").getdata()

def set_default(string, default_value):
    if string == '':
        return default_value
    else:
        return string

if __name__ == '__main__':
    try:
        image = PIL.Image.open(input(path))
    except:
        print(path, 'File not found')
        exit()

    new_image_width = set_default(input(choose), 100)
    new_image_width = int(new_image_width)
    if new_image_width < 0:
        raise Exception(exception1)
    image = resize_image(image, new_image_width)

    boundary = set_default(input(boundary1), '128')
    if not boundary.isnumeric():
        raise Exception(exception2)
    boundary = int(boundary)
    if boundary > 255 or boundary < 0:
        raise Exception(exception3)

    boundaryhl = set_default(input(boundary2), 'h')
    if boundaryhl != 'h' and boundaryhl != 'l':
        raise Exception(exception4)

    width, height = image.size
    px_array = gray_pixels(image)
    ascii_art = convertImg.px_ascii_art(px_array, width, height, boundary, boundaryhl)

    output_file = open('waifu.txt', 'w')
    output_file.write(ascii_art)

    print(ascii_art)
