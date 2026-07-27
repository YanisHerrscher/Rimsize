from PIL import Image
from os import listdir, path
from sys import argv

a = [argv[1]]

def view_directory(dir: list):
    new_list = []
    tree = listdir(dir)
    for x in tree:
        if path.isfile(f"{dir}/{x}"):
            img = Image.open(f"{dir}/{x}")
            width, height = img.size
            res = img.resize((int(width/2), int(height/2)))
            res.show()
        else:
            new_list.append(f"{dir}\\{x}")


    print("returned value:", new_list)

view_directory(a[0])