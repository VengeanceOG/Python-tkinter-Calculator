import os
import sys
import customtkinter as ctk
from PIL import Image


def abs_path(relative_path: str):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base_path, relative_path)


def path_2_img(relative_path: str, size):
    img = Image.open(abs_path(f'calc_images\{relative_path}'))
    return ctk.CTkImage(img, size=size)
