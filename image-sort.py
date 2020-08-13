from PIL import Image 

from os import listdir, mkdir, getcwd
from os.path import join, isdir
from shutil import move

def i_sort(w_path):
    print(w_path)
    files = map(lambda x: join(w_path, x), listdir(w_path))
    directories = []

    for f in files:
        print(f)
        if isdir(f):
            i_sort(f)
        try:
            im = Image.open(f)
        except:
            continue
        c_dir = join(b_path, str(im.width) + 'x' + str(im.width))
        im.close()
        if not isdir(c_dir):
            mkdir(c_dir)
            directories.append(c_dir)
        move(f, c_dir)

b_path = getcwd()
i_sort(b_path)