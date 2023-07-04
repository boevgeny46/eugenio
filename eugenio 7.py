from tkinter import *  #  # GUI - графический интерфейс пользователя
from PIL import Image, ImageTk
from tkinter import filedialog

status = False

class Okno:
    def __init__(self):
        self.window = Tk()  # Инициализация GUI

        self.window.title('welcome to tkinter')  # сначала создаем окно
        self.window.geometry('800x600')
        self.window.resizable(True, True)  # этой командой можно запрещать измерения по координатам
        self.lbl = Label(self.window, text= ' Label')
        self.lbl.pack()
        self.canvas = Canvas(self.window, height=100, width=133)
        self.file = Image.open('images/resized.png')
        self.image = ImageTk. PhotoImage(self.file)
        self.canvas.create_image(50, 50,  image=self.image)
        self.canvas.pack()
        self.btn = Button(self.window, text='Push', command=self.click)  # вводим команду кнопка  - она появится в окне
        self.btn.pack()



        self.window.mainloop()   # ПРОГРАММА РАБОТАЕТ - РИСУЕМ КНОПКУ, ОФОРМЛЯЕМ ЕЕ и вставляем картинку из png

    def click(self):
        path = filedialog.askopenfilename()
        original = Image.open(path)
        w,h = original. size
        ratio = w/h
        if w>133:
            original.resize((133, int(h/ ratio)))
        self.image = ImageTk.PhotoImage(original)
        self.canvas.create_image(50, 50, image=self.image)

if __name__ =='__main__':

    app = Okno()


# def click():
#      global status
#      if not status:
#        lbl['text'] = 'PUSH'
#        lbl['background'] = '#ff00ff'
#        btn['text'] = ' PUSH'
#        btn['background'] = '#ff00ff'
#      else:
#
#         lbl['text'] = 'Кнопка нажата'
#        # lbl['background'] = window.cget('bg') # ак можно вернуться к прежнему цвету
#         btn['text'] = ' just pushed'
#         btn['background'] = window.cget('bg')
#
# status = not status

# class Okno:
#     def __init__(self):
#         self.window = Tk()  # Инициализация GUI
#
#         self.window.title('welcome to tkinter')  # сначала создаем окно
#         self.window.geometry('800x600')
#         self.window.resizable(True, True)  # этой командой можно запрещать измерения по координатам
#         self.lbl = Label(window, text= ' Label')
#         self.lbl.pack()
#         self.canvas = Canvas(window, height=100, width=133)
#         self.file = Image.open('images/resized.png')
#         self.image = ImageTk. PhotoImage(file)
#         self.canvas.create_image(50,50,  image=image)
#         self.canvas.pack()
#         self.btn = Button(window, text='Push', command=click)  # вводим команду кнопка  - она появится в окне
#         self.btn.pack()
#
#
#
#         self.window.mainloop()   # ПРОГРАММА РАБОТАЕТ - РИСУЕМ КНОПКУ, ОФОРМЛЯЕМ ЕЕ и вставляем картинку из png
#
#     def click(self):
#         self.image = ImageTk.PhotoImage(Image.open('image/ingon.jpg'))
#         self.canvas.create_image(50,50, image= self.image)
#
# app = Okno()