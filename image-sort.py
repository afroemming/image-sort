from PIL import Image 

from os import listdir, mkdir
from shutil import move

files = listdir()
directories = []

for f in files:
    try:
        im = Image.open(f)
    except:
        continue
    c_dir = str(im.width) + 'x' + str(im.width)
    im.close()
    if not c_dir in directories:
        mkdir(c_dir)
        directories.append(c_dir)
    move(f, c_dir)
