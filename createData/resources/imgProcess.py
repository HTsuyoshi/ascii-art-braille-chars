import PIL.Image

def get_grayscale_pixels(name):
    try: 
        return PIL.Image.open(name).convert("L").getdata()
    except:
        print("File not found")
