# author: Louca Malerba
# date: 03/08/2025

# Public libraries
import os
import random
import string
import argparse

# Internal libraries
from captcha.image import ImageCaptcha

##################################

def generate_images(imgs_nbr, output_path_imgs, output_path_masks, captcha_length):
    for k in range(imgs_nbr):
        chars = ''.join(random.choices(string.ascii_letters, k=captcha_length))
        captcha = ImageCaptcha()
        captcha.write(chars,
                      os.path.join(output_path_imgs, chars + ".png"),
                      segmentation=True, 
                      output_mask=os.path.join(output_path_masks, chars + ".png"))

if __name__ == "__main__":
    # Configuration
    parser = argparse.ArgumentParser(description="Captcha & mask dataset generator")
    parser.add_argument('--output', type=str, default="./outputs",
                        help="Root output directory (default: ./outputs)")
    parser.add_argument('--count', type=int, default=10,
                        help="Number of images to generate (default: 10)")
    parser.add_argument('--length', type=int, default=5,
                        help="Captcha text length (default: 5)")
    args = parser.parse_args()

    OUTPUT_PATH = os.path.abspath(args.output)
    OUTPUT_PATH_IMGS = os.path.join(OUTPUT_PATH, 'images')
    OUTPUT_PATH_MASKS = os.path.join(OUTPUT_PATH, 'masks')

    # Make output directories if they don't exist:
    os.makedirs(OUTPUT_PATH_IMGS, exist_ok=True)
    os.makedirs(OUTPUT_PATH_MASKS, exist_ok=True)

    # Launch Generation
    generate_images(args.count, OUTPUT_PATH_IMGS, OUTPUT_PATH_MASKS, args.length)