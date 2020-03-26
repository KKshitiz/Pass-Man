from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from passlib.hash import sha256_crypt

#change this to suit your asset path
assetpath='C:\\Users\\skili\\Documents\\GitHub\\Pass-Man\\assets\\'

def startForget():
    global root
    root=Tk()
    root.title("  Recover Password")
    root.geometry("400x400")
    # root.resizable(0,0)
    root.configure(bg="white")
    root.iconphoto(True,PhotoImage(file=assetpath+'key.png'))
    root.tk.call('tk', 'scaling', 1.6)

    style=ttk.Style()
    style.configure("TLabel",background="white")