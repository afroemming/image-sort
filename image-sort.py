import os, shutil

from PIL import Image 

def i_sort(w_path):
    print(w_path)
    files = map(lambda x: os.path.join(w_path, x), os.listdir(w_path))

    for f in files:
        print(f)
        if os.path.isdir(f):
            i_sort(f)
        try:
            im = Image.open(f)
        except:
            continue
        c_dir = os.path.join(b_path, str(im.width) + 'x' + str(im.height))
        im.close()
        if not os.path.isdir(c_dir):
            os.mkdir(c_dir)
        shutil.move(f, c_dir)

b_path = os.getcwd()
i_sort(b_path)