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

    Label(root,text="ENTER DETAILS",font=("ARIAL",15,'bold','italic'),bg="dodger blue",fg="white").pack(pady=(20,20),ipadx=10,ipady=10)
    mainf=Frame(root,bg="white")
    mainf.pack(padx=30,pady=(20,5),ipadx=30,ipady=20)

    userf=Frame(mainf)
    userf.pack()
    useri=ImageTk.PhotoImage(Image.open(assetpath+"login.png").resize((40,40)))
    Label(userf,image=useri).pack(side=LEFT)
    usere=ttk.Entry(userf)
    usere.pack(side=LEFT)


    #a curated set of security questions
    sec_ques=["What is your pet name?",
    "What was the first company that you worked for?",
    "Where did you meet your spouse?",
    "Where did you go to high school/college?",
    "What city were you born in?"]

    quesf=Frame(mainf)
    quesf.pack()
    quesi=ImageTk.PhotoImage(Image.open(assetpath+"question.png").resize((40,40)))
    Label(quesf,image=quesi).pack(side=LEFT)
    quesc=ttk.Combobox(quesf,values=sec_ques,state='readonly')
    quesc.current(0)
    quesc.pack(side=LEFT)

    