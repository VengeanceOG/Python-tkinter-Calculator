import tkinter
from typing import Callable, Optional, Tuple, Union
import customtkinter as ctk
import tkinter as tk

from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage
from utils import abs_path, path_2_img

WHITE = '#FFFFFF'
BLUE = '#0F8DCB'
TEXT_COLOR = '#0F8DCB'
BG_COLOR = '#000000'
BUTTON_COLOR = '#343434'
ORANGE = '#FF5757'


class calc:

    def __init__(self) -> None:
        self.root = ctk.CTk(BG_COLOR)

        self.root.title('CALCULATOR')
        self.height = 554
        self.width = 332
        self.root.geometry(f'{self.width}x{self.height}')
        self.root.update()
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(width=0, height=0)
        self.root.iconbitmap(abs_path('calc_images\calc-icon.ico'))

        self.expression = tk.StringVar()
        self.expression.set('')
        self.total = tk.StringVar()
        self.total.set('')
        self.expression_frame = self.create_expression_frame()
        self.expression_label, self.total_label = self.create_display_labels()

        self.operator_frame = self.create_operator_frame()
        self.numbers = {'7': [1, 0], '8': [1, 1], '9': [1, 2],
                        '4': [2, 0], '5': [2, 1], '6': [2, 2],
                        '1': [3, 0], '2': [3, 1], '3': [3, 2],
                        '0': [4, 1]}
        self.number_buttons = self.add_number_buttons()
        self.operators = {'C': [0, 0], '(': [0, 1], ')': [0, 2], '÷': [0, 3], '×': [
            1, 3], '-': [2, 3], '+': [3, 3], 'x²': [4, 0], '.': [4, 2], '=': [4, 3]}
        self.operator_buttons = self.add_operators()

    def create_expression_frame(self):
        expression_frame = ctk.CTkCanvas(
            self.root, bg=BG_COLOR, height=self.root.winfo_height()*0.225, borderwidth=0, highlightthickness=0)
        expression_frame.pack(side='top', expand=0)
        expression_frame.pack_propagate(False)
        x1 = 0
        x2 = expression_frame.winfo_reqwidth()
        y = expression_frame.winfo_reqheight()-5
        expression_frame.create_line(
            x1, y, x2, y, width=2, fill=BUTTON_COLOR)
        return expression_frame

    def create_display_labels(self):
        remove_btn = btn(
            self.expression_frame, bg_color='transparent', image=path_2_img('cross.png', (25, 13)), fg_color=BG_COLOR, text='', height=13, width=25, corner_radius=0, cmd=self.update, cmd_args='remove')
        remove_btn.pack(side='bottom', anchor='se', padx=0, pady=20)

        big_font_size = -int(self.expression_frame.winfo_reqheight()*0.25)
        small_font_size = -int(self.expression_frame.winfo_reqheight()*0.1)
        expression_label = ctk.CTkLabel(self.expression_frame, textvariable=self.expression,
                                        text_color=WHITE, bg_color='transparent', font=ctk.CTkFont('Helvetica', big_font_size, 'bold'), anchor='se')
        expression_label.pack(side='bottom', expand=True,
                              fill='x', anchor='se', pady=0)

        total_label = ctk.CTkLabel(self.expression_frame, textvariable=self.total,
                                   text_color=WHITE, bg_color='transparent', font=ctk.CTkFont('Helvetica', small_font_size, 'normal'), anchor='ne')
        total_label.pack(side='top', expand=True,
                         fill='x', anchor='ne')

        return expression_label, total_label

    def create_operator_frame(self):
        operator_frame = ctk.CTkFrame(
            self.root, bg_color='transparent', fg_color=BG_COLOR)
        operator_frame.pack(fill='both', expand=True, padx=5, pady=5)
        return operator_frame

    def add_number_buttons(self):
        number_buttons = dict()
        button_font_size = -int(self.operator_frame.winfo_reqheight()*0.1)
        for number, position in self.numbers.items():
            number_button = btn(
                self.operator_frame, text=number, text_color=WHITE, fg_color=BUTTON_COLOR, bg_color='transparent', font=ctk.CTkFont('lucida', button_font_size, 'normal'), corner_radius=100, cmd=self.update, cmd_args=number)
            number_button.grid(
                row=position[0], column=position[1], sticky='nsew', padx=1, pady=1)
            number_buttons[number] = number_button

        return number_buttons

    def add_operators(self):
        operator_buttons = dict()
        button_font_size = -int(self.operator_frame.winfo_reqheight()*0.1)
        for operator, position in self.operators.items():
            row, column = position

            if operator == 'C':
                operator_button = btn(
                    self.operator_frame, text=operator, text_color=ORANGE, fg_color=BUTTON_COLOR, bg_color='transparent', font=ctk.CTkFont('lucida', button_font_size, 'normal'), corner_radius=100, cmd=self.update, cmd_args=operator)

            elif operator == '=':
                operator_button = btn(
                    self.operator_frame, text=operator, text_color=WHITE, fg_color=TEXT_COLOR, bg_color='transparent', font=ctk.CTkFont('lucida', button_font_size, 'normal'), corner_radius=100, cmd=self.update, cmd_args=operator)
            elif operator == 'x²':
                operator_button = btn(
                    self.operator_frame, text=operator, text_color=WHITE, fg_color=BUTTON_COLOR, bg_color='transparent', font=ctk.CTkFont('lucida', button_font_size, 'normal'), corner_radius=100, cmd=self.update, cmd_args=operator)

            elif operator == '.':
                operator_button = btn(
                    self.operator_frame, text=operator, text_color=WHITE, fg_color=BUTTON_COLOR, bg_color='transparent', font=ctk.CTkFont('lucida', button_font_size, 'normal'), corner_radius=100, cmd=self.update, cmd_args=operator)

            else:
                operator_button = btn(
                    self.operator_frame, text=operator, text_color=TEXT_COLOR, fg_color=BUTTON_COLOR, bg_color='transparent', font=ctk.CTkFont('lucida', button_font_size, 'normal'), corner_radius=100, cmd=self.update, cmd_args=operator)
            operator_button.grid(row=row, column=column,
                                 sticky='nsew', padx=1, pady=1)
            operator_buttons[operator] = operator_button
            self.operator_frame.columnconfigure(position[1], weight=1)
            self.operator_frame.rowconfigure(position[0], weight=1)

        return operator_buttons

    def update(self, character: str):

        if character == 'C':
            self.expression.set('')
            self.total.set('')
            self.expression_label.update()
            self.total_label.update()

        elif not self.expression.get() == 'SYNTAX ERROR':

            if character == 'remove':
                expression = self.expression.get()[0:-1]
                try:
                    total = eval(expression.replace(
                        '÷', '/').replace('×', '*').replace('²', '**2'))
                except:
                    if expression:
                        total = self.total.get()

                    else:
                        total = ''

            elif character == 'x²':
                expression = self.expression.get() + '²'
                try:
                    total = eval(expression.replace(
                        '÷', '/').replace('×', '*').replace('²', '**2'))
                except:
                    total = ''

            elif character == '=':
                try:
                    total = eval(self.expression.get().replace(
                        '÷', '/').replace('×', '*').replace('²', '**2'))
                    expression = total
                except Exception as e:

                    if type(e) == ZeroDivisionError:
                        expression = 'DIVISION ERROR'

                    else:
                        expression = 'SYNTAX ERROR'
                    total = ''

            else:
                expression = self.expression.get() + character
                if character.isdigit():
                    try:
                        total = eval(expression.replace(
                            '÷', '/').replace('×', '*').replace('²', '**2'))
                    except:
                        total = ''
                else:
                    total = self.total.get()
            self.expression.set(str(expression)[:13])
            self.total.set(str(total)[:13])

            self.expression_label.update()
            self.total_label.update()

    def run(self):
        (self.root.winfo_width())
        self.root.mainloop()


class btn(ctk.CTkButton):
    def __init__(self, master, cmd=None, cmd_args=None, **kwargs):
        self.cmd = cmd
        self.cmd_args = cmd_args
        super().__init__(master, **kwargs)
        if cmd:
            self.configure(command=lambda: self.cmd(self.cmd_args))
