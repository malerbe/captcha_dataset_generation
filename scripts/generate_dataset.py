# author: Louca Malerba
# date: 03/08/2025

# Public libraries
import os
import random
import string

# Internal libraries
from captcha.image import ImageCaptcha

##################################

def generate_images():
    for k in range(IMGS_NBR):
        chars = ''.join(random.choices(string.ascii_letters, k=5))
        captcha = ImageCaptcha()
        captcha.write(chars,
                      os.path.join(OUTPUT_PATH_IMGS, chars + ".png"),
                      segmentation=True, 
                      output_mask=os.path.join(OUTPUT_PATH_MASKS, chars + ".png"))

if __name__ == "__main__":
    # Configuration
    OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'outputs')
    IMGS_NBR = 1


    OUTPUT_PATH_IMGS = os.path.join(OUTPUT_PATH, 'images')
    OUTPUT_PATH_MASKS = os.path.join(OUTPUT_PATH, 'masks')

    # Make output directories if they don't exist:
    os.makedirs(OUTPUT_PATH_IMGS, exist_ok=True)
    os.makedirs(OUTPUT_PATH_MASKS, exist_ok=True)

    # Launch Generation
    generate_images()