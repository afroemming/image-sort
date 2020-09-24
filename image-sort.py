import os, shutil, argparse

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
        c_dir = os.path.join(args.path, str(im.width) + 'x' + str(im.height))
        im.close()
        if not os.path.isdir(c_dir):
            os.mkdir(c_dir)
        try:
            shutil.move(f, c_dir)
        except:
            pass

parser = argparse.ArgumentParser(description="Sort images recursively into folders by resolutions")
parser.add_argument('path', metavar='P', type=str, help='base path to sort below')
args = parser.parse_args()

i_sort(args.path)