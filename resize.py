from PIL import Image
from os import walk, path, system
import re
import threading
from concurrent.futures import ThreadPoolExecutor


class Resize:
    def __init__(self, extension: str, path: list):
            self.extension = extension
            self.__path_list = path
            self.__max_thread = ThreadPoolExecutor(max_workers=5)
            self.__list_image = []

    def __view_directory(self, dir: str):
        for root, _, files in walk(dir):
            for file in files:
                _, extension = path.splitext(file)
                if extension.lower() == f".{self.extension.lower()}":
                     self.__list_image.append(path.join(root, file))

    def __resize(self, path):
        with Image.open(path) as img:
            width, height = img.size
            if width >= 1024 or height >= 1024:
                res = img.resize((int(width/2), int(height/2)))
                res.save(path)

    def convert(self):
        for path_dir in self.__path_list:
            self.__view_directory(path_dir)
        self.__max_thread.map(self.__resize, self.__list_image)
        self.__max_thread.shutdown(wait=True)