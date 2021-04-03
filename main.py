import convertImg
import PIL.Image

path = 'Write the path for the file: '
choose = 'Choose the image width (recommended size: 100):'

def resize_image(image, new_width=100):
    width, height = image.size
    new_height = int(new_width * (height / width))
    new_image = image.resize((new_width, new_height))
    return new_image

def gray_pixels(image):
    return image.convert("L").getdata()

if __name__ == '__main__':
    try:
        image = PIL.Image.open(input(path))
    except:
        print(path, 'File not found')
        exit()

    new_image_width = int(input(choose))
    image = resize_image(image, new_image_width)

    width, height = image.size
    px_array = gray_pixels(image)
    ascii_art = convertImg.px_ascii_art(px_array, width, height)
    output_file = open("waifu.txt", "w")
    output_file.write(ascii_art)

    print(ascii_art)
