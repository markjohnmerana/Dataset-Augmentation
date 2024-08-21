Here's a README description for your GitHub repository based on the provided code:

---

# Image Processing Script

This Python script automates the process of applying various image transformations to all image files within a specified directory. It uses the Python Imaging Library (PIL) to handle image manipulations such as rotation, flipping, brightness adjustments, temperature adjustments, and hue modifications. The transformed images are then saved in a specified output directory.

## Features

- **Image Rotation:** Rotate images by 0°, 90°, 180°, and 270°.
- **Image Flipping:** Flip images horizontally and vertically.
- **Brightness Adjustment:** Increase or decrease the brightness of the images.
- **Color Temperature Adjustment:** Warm or cool the images by adjusting the red color channel.
- **Hue Adjustment:** Adjust the hue by converting the image to grayscale and recoloring with a specified hue.

## Supported Image Formats

The script supports various image formats, including:
- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.gif`
- `.tiff`
- `.HEIC`

## Usage

1. Place the images you want to process in the `Healthy` directory.
2. Run the script.
3. Processed images will be saved in the `output_images` directory with appropriate suffixes indicating the transformation applied.

## How It Works

- The script iterates through all files in the input directory (`Healthy`).
- It checks if each file is an image by verifying the file extension.
- For each image, it applies a set of predefined transformations.
- The transformed images are saved in the `output_images` directory with descriptive filenames.

## Example Output Filenames

If you have an image named `example.jpg`, the script will generate the following output files:
- `example_rotate_0.jpg`
- `example_rotate_90.jpg`
- `example_rotate_180.jpg`
- `example_rotate_270.jpg`
- `example_flip_horizontal.jpg`
- `example_flip_vertical.jpg`
- `example_brightness_increase.jpg`
- `example_brightness_decrease.jpg`
- `example_temperature_warm.jpg`
- `example_temperature_cool.jpg`
- `example_hue_adjust.jpg`

## Requirements

- Python 3.x
- PIL (Pillow)

You can install the required libraries using pip:

```bash
pip install pillow
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

