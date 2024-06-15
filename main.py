from PIL import Image

# ASCII characters used for mapping
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 is used to correct aspect ratio
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert('L')

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel//range_width] for pixel in pixels])
    return ascii_str

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return
    
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    
    ascii_str = map_pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = '\n'.join([ascii_str[index:index + img_width] for index in range(0, ascii_str_len, img_width)])
    
    return ascii_img

def save_ascii_image(ascii_img, output_file):
    with open(output_file, 'w') as f:
        f.write(ascii_img)

# main function for ui 
def main():
    image_path = input("Enter the path to the image file: ")
    output_file = input("Enter the path to save the ASCII art (e.g., ascii_image.txt): ")
    new_width = int(input("Enter the desired width of the ASCII art (e.g., 100): "))
    
    ascii_img = convert_image_to_ascii(image_path, new_width)
    
    if ascii_img:
        save_ascii_image(ascii_img, output_file)
        print(f"ASCII art saved to {output_file}")

# Run main 
if __name__ == "__main__":
    main()
