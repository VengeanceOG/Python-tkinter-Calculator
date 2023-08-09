import os
import sys
import customtkinter as ctk
from PIL import Image


def abs_path(relative_path: str):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    with open('temp.txt', 'w') as f:
        f.write(base_path)

    return os.path.join(base_path, relative_path)


def path_2_img(relative_path: str):
    img = Image.open(abs_path(relative_path))
    return ctk.CTkImage(img)
