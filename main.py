#Sai

import PIL.Image

#ASCII used for output @%#*+=-:.
ASCII_chars = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]

#resize image as per requirement
def resize_img(img, new_width=100):
    width,height = img.size
    ratio = height / width
    new_height= int(new_width * ratio * 0.55)
    resize_image = img.resize((new_width,new_height))
    return resize_image

#convert pixel to grey scale
def gray_img(img):
    gray_image = img.convert("L")
    return gray_image

#convert pixel to string of ASCII characters
def pixel_to_ascii(img,bg="white"):
    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        index = pixel * (len(ASCII_chars) - 1) // 255

        if bg == "white":
            ascii_str += " " if pixel >= 240 else ASCII_chars[index]
        elif bg == "black":
            ascii_str += " " if pixel <= 15 else ASCII_chars[index]
        else:
            ascii_str += ASCII_chars[index]

    return ascii_str

#Get image from user input
def main(new_width=100):
    path = input("Enter a valid path to an image: ")
    try:
        img = PIL.Image.open(path)
    except:
        print(path,"is not a valid path to an image")


    bg_color = input("Is the background 'white' or 'black'?: ").strip().lower()

#convert image to ASCII
    new_img_data = pixel_to_ascii(gray_img(resize_img(img)))

#format
    pixel_count = len(new_img_data)
    ascii_image = "\n".join(new_img_data[i:(i+new_width)] for  i in range(0, pixel_count, new_width))

#print ASCII image
    with open("ASCII_img.txt","w") as f:
        f.write(ascii_image)

    print("ASCII image written to ASCII_img.txt")

main()