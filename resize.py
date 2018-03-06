from PIL import Image
import os

path = "images/"

images = os.listdir(path)

TARGET_WIDTH = 6 * 30
target = Image.new('RGB', (TARGET_WIDTH, 30*2))
for i in range(len(images)):
    image_path = path + images[i]
    image = Image.open(image_path)
    black = image.convert('L')
    thumbnail = image.resize((30, 30), Image.ANTIALIAS)
    thumbblack = black.resize((30, 30), Image.ANTIALIAS)
    target.paste(thumbblack, (i*30, 0, (i+1)*30, 30))
    target.paste(thumbnail, (i * 30, 30, (i + 1) * 30, 30*2))
    # thumbnail.save(path + str(i) + '.png', quality=100)
target.save(path +'new.png', quality=100)
    # print(image)



