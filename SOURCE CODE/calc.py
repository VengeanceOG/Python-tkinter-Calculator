import tkinter as tk
from typing import Tuple,List
from PIL import ImageTk,Image
from pathlib import Path
import os

#Some constants to use in calc.
WHITE = '#FFFFFF'
LIGHT_BLACK = '#1F1F21'
BIG_FONT = ('Helvetica',28)
SMALL_FONT = ('Helvetica',12)
BUTTON_FONT = ('lucida',19)
OPERATOR_FONT = ('lucida',23)
BLACK = '#000000'
BLUE = '#00AEFF'
LIGHT_BLUE = '#4CC6FF'
ORANGE = '#BE5504'
LIGHT_ORANGE = '#FC6A03'

class calc:

    def __init__(self) -> None:
        self.root = tk.Tk()


        #Basic root window configuration settings.
        self.title = None
        self.icon_path = None
        self.height = 554
        self.width = 332
        self.bg = BLACK
        self.resizable = False
        # self.root.overrideredirect(True)

        #Setting constants for expression frame.
        self.expression = tk.StringVar()
        self.expression.set('')
        self.expression_color = WHITE
        self.total = tk.StringVar()
        self.total.set('')
        self.total_color = WHITE
        self.expression_frame_height = 139
        self.seperating_line_img = None
        self.remove_btn_img = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\close-image.png'))
        self.remove_btn_activeimg = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\light-close-image.png'))

        #Setting constants for buttons.
        self.button_color = WHITE
        self.button_img = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\grey_circle.png'))
        self.button_activeimg = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\light_grey_circle.png'))
        self.numbers = {'7':[1,0],'8':[1,1],'9':[1,2],
                        '4':[2,0],'5':[2,1],'6':[2,2],
                        '1':[3,0],'2':[3,1],'3':[3,2],
                                  '0':[4,1]}
        self.operators = {'C':[0,0],'(':[0,1],')':[0,2],'÷':[0,3]
                                                        ,'×':[1,3]
                                                        ,'-':[2,3]
                                                        ,'+':[3,3]
                           ,'x²':[4,0]        ,'.':[4,2],'=':[4,3]}
        self.outer_button_color = BLUE
        self.submit_button_image = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\blue-circle.png'))
        self.submit_button_activeimage = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\light-blue-circle.png'))

    def create_expression_frame(self) -> tk.Frame:
        expression_frame = tk.Frame(self.root,bg=BLACK,height=self.expression_frame_height)
        expression_frame.pack(side='top',fill='x')
        expression_frame.pack_propagate(False)
        return expression_frame
    
    def create_seperate_line(self) -> tk.Label:
        line = tk.Label(self.expression_frame,bg=BLACK,image=self.seperating_line_img,anchor='center')
        line.pack(side='bottom',pady=10)
        return line

    def create_display_labels(self) -> Tuple[tk.Label,tk.Label,tk.Button]:
        remove_btn = btn(self.expression_frame,activebackground=self.bg,image=self.remove_btn_img,bg=self.bg,activeimage=self.remove_btn_activeimg,border=0,command=self.update,arg='remove',activeforeground=self.bg)
        remove_btn.pack(side='bottom',anchor='se',padx=12,pady=5)

        expression_label = tk.Label(self.expression_frame,textvariable=self.expression,fg=self.expression_color,bg=self.bg,font=BIG_FONT,anchor='se')
        expression_label.pack(side='bottom',padx=12,expand=True,fill='x',anchor='se',pady=5)

        total_label = tk.Label(self.expression_frame,textvariable=self.total,fg=self.total_color,bg=self.bg,font=SMALL_FONT,anchor='ne')
        total_label.pack(side='top',padx=12,expand=True,fill='x',anchor='ne',pady=5)


        return (expression_label,total_label)
    

    def create_operator_frame(self) -> tk.Frame:
        operator_frame = tk.Frame(self.root,bg=self.bg)
        operator_frame.pack(fill='both',expand=True,padx=5,pady=5)
        return operator_frame
    
    def add_number_buttons(self) -> List[tk.Button]:
        number_buttons = []
        for number,position in self.numbers.items():
            number_button = btn(self.operator_frame,text=number,fg=self.button_color,activebackground=self.bg,compound='center',font=BUTTON_FONT,image=self.button_img,bg=self.bg,activeimage=self.button_activeimg,border=0,command=self.update,arg=number)
            number_button.grid(position=position,sticky='nsew')
            number_buttons.append(number_button)
        
        return number_buttons

    def add_operators(self) -> List[tk.Button]:
        operator_buttons = []
        for operator,position in self.operators.items():
            [row,column] = position

            if operator == 'C':
                operator_button = btn(self.operator_frame,text=operator,fg=ORANGE,activebackground=self.bg,compound='center',font=OPERATOR_FONT,image=self.button_img,bg=self.bg,activeimage=self.button_activeimg,border=0,command=self.update,arg=operator,activeforeground=LIGHT_ORANGE)

            elif operator == '=':
                operator_button = btn(self.operator_frame,text=operator,fg=self.button_color,activebackground=self.bg,compound='center',font=OPERATOR_FONT,image=self.submit_button_image,bg=self.bg,activeimage=self.submit_button_activeimage,border=0,command=self.update,arg=operator)

            elif operator == 'x²':
                operator_button = btn(self.operator_frame,text=operator,fg=self.button_color,activebackground=self.bg,compound='center',font=BUTTON_FONT,image=self.button_img,bg=self.bg,activeimage=self.button_activeimg,border=0,command=self.update,arg=operator)

            elif row==0 or column==3:
                operator_button = btn(self.operator_frame,text=operator,fg=self.outer_button_color,activebackground=self.bg,compound='center',font=OPERATOR_FONT,image=self.button_img,bg=self.bg,activeimage=self.button_activeimg,border=0,command=self.update,arg=operator,activeforeground=LIGHT_BLUE)

            else:
                operator_button = btn(self.operator_frame,text=operator,fg=self.button_color,activebackground=self.bg,compound='center',font=OPERATOR_FONT,image=self.button_img,bg=self.bg,activeimage=self.button_activeimg,border=0,command=self.update,arg=operator)
            
            operator_button.grid(position=position,sticky='nsew')
            operator_buttons.append(operator_button)

        return operator_buttons

    def run(self) -> None:

        self.root.geometry(f'{self.width}x{self.height}')
        self.root.configure(bg=BLACK)
        self.root.resizable(width=self.resizable,height=self.resizable)
        
        if self.icon_path:
            self.root.iconbitmap(self.icon_path)

        if self.title:
            self.root.title(self.title)

        self.expression_frame = self.create_expression_frame()

        if self.seperating_line_img:
            self.seperating_line = self.create_seperate_line()

        self.expression_label, self.total_label = self.create_display_labels()

        self.operator_frame = self.create_operator_frame()

        self.number_buttons = self.add_number_buttons()

        self.operator_buttons = self.add_operators()

        self.root.mainloop()

    def update(self,character: str) -> None:

        if character == 'C':
            self.expression.set('')
            self.total.set('')
            self.expression_label.update()
            self.total_label.update()

        elif not self.expression.get() == 'SYNTAX ERROR':

            if character == 'remove':
                expression = self.expression.get()[0:-1]
                try:
                    total = eval(expression.replace('÷','/').replace('×','*').replace('²','**2'))
                except:
                    if expression:
                        total = self.total.get()

                    else:
                        total = ''

            elif character == 'x²':
                expression = self.expression.get() + '²'
                try:
                    total = eval(expression.replace('÷','/').replace('×','*').replace('²','**2'))
                except:
                    total = ''

            elif character == '=':
                try:
                    total = eval(self.expression.get().replace('÷','/').replace('×','*').replace('²','**2'))
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
                        total = eval(expression.replace('÷','/').replace('×','*').replace('²','**2'))
                    except:
                        total = ''
                else:
                    total = self.total.get()
            self.expression.set(expression)
            self.total.set(total)

            self.expression_label.update()
            self.total_label.update()


class btn:
    def __init__(self,master,font=None,text=None,image=None,activeimage=None,activebackground = None,activeforeground=None,bg=None,fg=None,border=0,command=None,arg=None,compound=None) -> None:
        self.master = master
        self.activebackground = activebackground
        self.activeforeground = activeforeground
        self.bg = bg
        self.fg = fg
        self.border = border
        self.command = command
        self.text = text
        self.font = font
        self.image = image
        self.activeimage = activeimage
        self.arg = arg
        self.compound = compound

        if not self.arg:
            self.button = tk.Button(self.master,text=self.text,font=self.font,activebackground=self.activebackground,activeforeground=self.activeforeground,bg=self.bg,fg=self.fg,border=self.border,command=self.command,image=self.image,compound=self.compound)
        
        else:
            self.button = tk.Button(self.master,text=self.text,font=self.font,activebackground=self.activebackground,activeforeground=self.activeforeground,bg=self.bg,fg=self.fg,border=self.border,command=lambda: self.command(self.arg),image=self.image,compound=self.compound)
        
        if self.activeimage:
            #Creating an activeimage.
            self.button.bind('<Button-1>',lambda event: self.button.configure(image=self.activeimage))
            self.button.bind('<ButtonRelease-1>',lambda event: self.button.configure(image=self.image))

    def grid(self,position,sticky=None):
        [row,column] = position
        self.button.grid(row=row,column=column,sticky=sticky)
        self.button.grid_rowconfigure(row,weight=1)
        self.button.grid_columnconfigure(column,weight=1)   

    def pack(self,padx=0,pady=0,anchor=None,side=None):
        self.button.pack(padx=padx,pady=pady,anchor=anchor,side=side)
