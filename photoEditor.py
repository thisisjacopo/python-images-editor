from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = './editedImages'

for filename in os.listdir(path):

    img = Image.open(f'{path}/{filename}')
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    factor = 1.2
    enhancer = ImageEnhance.Contrast(edit)
    final_image = enhancer.enhance(factor)
    final_name = os.path.splitext(filename)[0]
    final_image.save(f'{pathOut}/{final_name}_edited.jpg')