from tkinter import *
from tkinter import ttk

root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    
    def tela(self):
        self.root.title("Método das Velocidades Indexadas")
        self.root.configure(background='#32cd32',)
        self.root.geometry("1050x550")
        self.root.resizable(True, True)
        self.root.maxsize(width=1150, height=600)
        self.root.minsize(width=700, height=500)
    
    



App()