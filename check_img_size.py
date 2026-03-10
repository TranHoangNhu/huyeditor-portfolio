import os
from PIL import Image

img_path = 'img/port-pages/page_1.jpg'
if os.path.exists(img_path):
    with Image.open(img_path) as img:
        print(f"Dimensions: {img.size[0]}x{img.size[1]}")
        print(f"Aspect ratio: {img.size[0]/img.size[1]}")
else:
    print("Image not found")
