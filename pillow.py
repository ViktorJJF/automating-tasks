from PIL import Image, ImageEnhance, ImageFilter
import os

path = "imgs"
path_out = "edited_images"

for filename in os.listdir(path):
    img = Image.open(path + "/" + filename)
    edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-90)
    FACTOR = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(FACTOR)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{path_out}/{clean_name}_edited.jpg")
