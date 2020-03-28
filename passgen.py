"""
function to generate random strong passwords
"""
from tkinter import Frame,Toplevel,PhotoImage,Label,LEFT,Button,BooleanVar,END,W,X
from tkinter.ttk import Style,Entry,Radiobutton,Checkbutton,Spinbox
from random import randint
from subprocess import check_call
from PIL import ImageTk,Image

assetpath='C:\\Users\\skili\\Documents\\GitHub\\Pass-Man\\assets\\'

lowerchars='abcdefghijklmnopqrstuvwxyz'
upperchars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
specialchars='!@#$%^&*()'


#function to copy text to clipboard
def copy2clip(txt):
    cmd='echo '+str(txt).strip()+'|clip'
    return check_call(cmd, shell=True)


#generates and returns password according to the options
def passGen(length=8,upper=True,digit=True,special=True):
    pass_chars=[]
    password=""
    pass_chars.append(lowerchars)
    if upper:
        pass_chars.append(upperchars)
    if digit:
        pass_chars.append(digits)
    if special:
        pass_chars.append(specialchars)

    for x in range(length):
        a=pass_chars[randint(0,len(pass_chars)-1)]
        password+=a[randint(0,len(a)-1)]

    passe.delete(0,END)
    passe.insert(0,password)
    

def setlength(a):
    global length
    length=int(a)


#closes the password generator
def exitPassGen():
    root.destroy()


#starts pass generator
def startPassGen():
    global root
    root=Toplevel()
    root.attributes('-topmost',True)
    root.title("  Password Generator")
    root.geometry("350x380")
    # root.resizable(0,0)
    root.configure(bg="white")
    root.iconphoto(True,PhotoImage(file=assetpath+'padlock.png'))
    root.tk.call('tk', 'scaling', 1.6)

    style=Style()
    style.configure("TLabel",background="white")
    style.configure('TCheckbutton', background='white')

    mainf=Frame(root,bg="white")
    mainf.pack(pady=20,padx=20,ipadx=10,ipady=10)

    f1=Frame(mainf,bg="white")
    f1.pack()
    icon=ImageTk.PhotoImage(Image.open(assetpath+'key.png').resize((45,45)))
    Label(f1,image=icon,bg="white").grid(row=0,column=0,rowspan=2,padx=2,pady=5)
    Label(f1,text="Pass-Gen",font=('ARIAL',15,'bold'),bg="white").grid(row=0,column=2)
    Label(f1,text="Password Generator",bg="white").grid(row=1,column=2)


    f2=Frame(mainf,bg="white")
    f2.pack(padx=10,pady=(30,15))
    global passe
    passe=Entry(f2,width=30)
    passe.pack(side=LEFT)
    copyi=ImageTk.PhotoImage(Image.open(assetpath+'copy.png').resize((25,25)))
    copyb=Button(f2,image=copyi,bg="white",bd=0,activebackground="white",command=lambda : copy2clip(passe.get()))
    copyb.pack(side=LEFT,padx=2)

    global length
    length=8

    lenf=Frame(mainf)
    lenf.pack()
    Label(lenf,text="Length  ",bg="white").pack(side=LEFT)
    s=Spinbox(lenf,from_=4,to=25,width=5,command=lambda : setlength(s.get()))
    s.set(8)
    s.pack(side=LEFT)

    upper=BooleanVar()
    digit=BooleanVar()
    special=BooleanVar()
    upper.set(True)
    digit.set(True)
    special.set(True)
    f3=Frame(mainf,bg="white")
    f3.pack(padx=10,pady=10)
    capb=Checkbutton(f3,text="Include Capitals",variable=upper,offvalue=False,onvalue=True)
    capb.pack(anchor=W,pady=5)
    digitb=Checkbutton(f3,text="Include Digits",variable=digit,offvalue=False,onvalue=True)
    digitb.pack(anchor=W,pady=5)
    specialb=Checkbutton(f3,text="Include Special Symbols",variable=special,offvalue=False,onvalue=True)
    specialb.pack(anchor=W,pady=5)

    genb=Button(mainf,text="Generate",command=lambda : passGen(length,upper.get(),digit.get(),special.get()),bg="turquoise3",activebackground="turquoise3",bd=0)
    genb.pack(pady=10,ipadx=20,padx=(43,10),side=LEFT)
    exitb=Button(mainf,text="Exit",command=exitPassGen,bg="firebrick1",activebackground="firebrick1",bd=0,width=37)
    exitb.pack(pady=10,ipadx=20,padx=(10,30),side=LEFT)

    root.mainloop()

if __name__ == "__main__":
    startPassGen()