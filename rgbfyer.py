from PIL import Image

def get_rgb_values(image_path):
    image = Image.open(image_path)
    width, height = image.size
    rgb_values = []
    for y in range(height):
        for x in range(width):
            rgb_values.append(image.getpixel((x, y)))
    return rgb_values

def main():
    image_path = r'path'
    vals = get_rgb_values(image_path)
    fmtr = '['
    for val in vals:
        fmtr += str(pixel)
        fmtr += ','
    print(star + ']')

if __name__ == "__main__":
    main()
