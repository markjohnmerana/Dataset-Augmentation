

from PIL import Image, ImageEnhance, ImageOps
import os

input_directory = 'Healthy'  
output_directory = 'output_images'
os.makedirs(output_directory, exist_ok=True)

supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.HEIC')


def adjust_temperature(image, factor):
    r, g, b = image.split()
    r = r.point(lambda i: i * factor)
    return Image.merge('RGB', (r, g, b))

def adjust_hue(image, hue_factor):
    grayscale = ImageOps.grayscale(image)
    return ImageOps.colorize(grayscale, black="black", white=hue_factor)

for filename in os.listdir(input_directory):
    if filename.lower().endswith(supported_extensions):
        
        image_path = os.path.join(input_directory, filename)
        image = Image.open(image_path)
        
     
        transformations = [
            ('rotate_0', image),
            ('rotate_90', image.rotate(90)),
            ('rotate_180', image.rotate(180)),
            ('rotate_270', image.rotate(270)),
            ('flip_horizontal', image.transpose(Image.FLIP_LEFT_RIGHT)),
            ('flip_vertical', image.transpose(Image.FLIP_TOP_BOTTOM)),
            ('brightness_increase', ImageEnhance.Brightness(image).enhance(1.5)),
            ('brightness_decrease', ImageEnhance.Brightness(image).enhance(0.7)),
            ('temperature_warm', adjust_temperature(image, 1.2)),
            ('temperature_cool', adjust_temperature(image, 0.8)),
            ('hue_adjust', adjust_hue(image, "orange")),
        ]
        
        
        base_name, ext = os.path.splitext(filename)
        for i, (name, transformed_image) in enumerate(transformations):
            output_filename = f'{base_name}_{name}{ext}'
            output_path = os.path.join(output_directory, output_filename)
            transformed_image.save(output_path)

print(f'Images have been processed and saved to {output_directory}')

