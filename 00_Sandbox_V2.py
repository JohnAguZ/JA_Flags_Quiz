import os
import random
from PIL import Image

path = 'E:\COM301\Programming\JA_Flags_Quiz\Flags_Dataset'
image_list = []

names = random.choice(os.listdir(path))  # ----> Randomly select 5 images
for filename in names:
    full_path = os.path.join(path, filename)
    if os.path.isfile(full_path):
        img = Image.open(full_path)
        image_list.append(img)

print(image_list)
