from PIL import Image
from os import walk, path
from sys import argv
import re
import threading
from concurrent.futures import ThreadPoolExecutor


class Resize:
    def __init__(self, path: list):
            self.__path_list = path
            self.__max_thread = ThreadPoolExecutor(max_workers=5)
            self.__list_image = []

    def __view_directory(self, dir: str):
        for root, _, files in walk(dir):
            for file in files:
                if re.search(r"\.png$", file):
                     self.__list_image.append(path.join(root, file))

    def __resize(self, path):
        with Image.open(path) as img:
            width, height = img.size
            if width >= 1024 or height >= 1024:
                res = img.resize((int(width/2), int(height/2)))
                res.save(path)

    def convert(self):
        for path in self.__path_list:
            self.__view_directory(path)
        self.__max_thread.map(self.__resize, self.__list_image)
        im.__max_thread.shutdown(wait=True)

im = Resize([argv[1]])
im.convert()