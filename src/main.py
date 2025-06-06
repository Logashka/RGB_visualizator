from tkinter import Tk
from gui import build_gui

if __name__ == '__main__':
    root = Tk()
    root.title("RGB Визуализация")
    build_gui(root)
    root.mainloop()
