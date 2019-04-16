# Gabriel Carver
from tkinter import *

class Start:
    def __init__(self, root):
        self.root = root
        self.t_frame = Frame(self.root)
        self.b_frame = Frame(self.root)
        self.b1_frame = Frame(self.b_frame)
        self.b2_frame = Frame(self.b_frame)
        self.b3_frame = Frame(self.b_frame)
        self.t_frame.pack(side=TOP)
        self.b_frame.pack(side=TOP)
        self.b1_frame.pack(side=TOP)
        self.b2_frame.pack(side=TOP)
        self.b3_frame.pack(side=TOP)


def main():
    root= Tk()
    strt = Start(root)
    root.mainloop()