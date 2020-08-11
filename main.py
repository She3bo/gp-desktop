from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pprint import pprint
from PIL import ImageDraw

import pytesseract
from PIL import Image
from googletrans import Translator


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('Translator')
        self.minsize(400, 400)
        # self.wm_iconbitmap('icon.ico')
        self.labelFrame = ttk.LabelFrame(self,text='Chose File').grid(column = 0, row = 1, padx = 20, pady = 20)
        self.button()
        self.optionMenu()
        self.buttonTranslate()
        self.textArea("")
    def button(self):
        self.button = ttk.Button(self.labelFrame,text='Browse A File', command = self.fileDialog)
        self.button.grid(column = 1, row = 1)

    imageFile = ""
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/" , title = "Select A File",filetypes = (("All Files","*.*"),('jpeg','jpg'),("png file","png")))
        self.label = ttk.Label(self.labelFrame,text="")
        self.label.grid(column = 2, row = 1)
        name = self.filename.split('/')[-1]
        # pprint(name)
        self.label.configure(text = name)
        self.imageFile = self.filename

    def optionMenu(self):
        lang = StringVar()
        lang.set('ar')
        self.drop = OptionMenu(self,lang, "ar","en","es", command=self.func)
        self.drop.grid(column=3, row=1)

    lang = "ar"
    def func(self, value):
        # pprint(value)
        self.lang = str(value)

    def buttonTranslate(self):
        self.button = ttk.Button(self.labelFrame,text='Translate', command = self.translate)
        self.button.grid(column = 3, row = 3)

    def translate(self):
        if(self.imageFile == ""):
            return
        result = pytesseract.image_to_string(Image.open(self.imageFile))
        # pprint(result)
        trans = Translator()
        t = trans.translate(result, src='en', dest=self.lang)
        pprint(t)
        self.textArea(t)

    def textArea(self,res):
        # print(res)
        text = Text(self,height=20, width=30,wrap=WORD)
        text.grid(row=5,columnspan=10,sticky=W)
        text.insert(2.1,res)

if __name__ == '__main__':
    root = Root()
    root.mainloop()
