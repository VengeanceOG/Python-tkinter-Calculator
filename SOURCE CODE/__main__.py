from calc import calc,Image,ImageTk,os

calculator = calc()

calculator.title = 'CALCULATOR'
calculator.icon_path = os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\calc_icon.ico'
calculator.seperating_line_img = ImageTk.PhotoImage(Image.open(os.path.dirname(os.path.abspath(__file__)) + r'\calc_images\seperate_line.png'))

calculator.run()