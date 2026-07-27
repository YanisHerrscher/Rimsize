import tkinter as tk
from resize import Resize

class window():
    def __init__(self):
        self._window = tk.Tk()
        self._window.title("")
        self._window.iconbitmap("")
        self.__width= 500
        self.__height= 500

    def execute(self, extension, path):
        if extension != "" or path != "":
            image = Resize(extension, [path])
            image.convert()

    def core(self):
        label = tk.Label(self._window, text="extension")
        label.place(
            x=50,
            y=150,
            width=360,
            height=30
        )
        extension = tk.Entry(self._window, validate="key")
        extension.place(
            x=50,
            y=180,
            width=360,
            height=30
        )
        label = tk.Label(self._window, text="path")
        label.place(
            x=50,
            y=60,
            width=360,
            height=30
        )
        path = tk.Entry(self._window, validate="key")
        path.place(
            x=50,
            y=90,
            width=360,
            height=30
        )

        button_confirm = tk.Button(self._window, command=lambda: self.execute(extension.get(), path.get()))
        button_confirm.place(
            x=50,
            y=270,
            width=360,
            height=30
        )

        self._window.geometry("%dx%d" % (self.__width, self.__height))
        self._window.mainloop()
        return self._window