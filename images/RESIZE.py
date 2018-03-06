import os
from PIL import Image

path = "QR/"

images = os.listdir(path)
for image in images:
    img_path = path + image
    img = Image.open(img_path)
    thumb = img.resize((120, 120), Image.ANTIALIAS)
    thumb.save(path+image.split('.')[0]+'.png', quality=100)

print(images)

