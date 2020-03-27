#the imports are so used as to reduce the executable file size
from tkinter import Frame,Label,Button,TOP,LEFT,PhotoImage,Tk,HORIZONTAL,X
from tkinter.ttk import Entry,Style,Separator
from PIL import ImageTk,Image
from passlib.hash import sha256_crypt
from signup import startSignup
from forgetpwd import startForget

#change this to suit your asset path
assetpath='C:\\Users\\skili\\Documents\\GitHub\\Pass-Man\\assets\\'

#checks creds and starts panel
def login(user,pwd):
        return

#closes the login window
def exitLogin():
        root.destroy()


#starts the login window
def startLogin():
        global root
        root=Tk()
        root.title("  Pass-Man Login")
        root.geometry("400x400")
        root.resizable(0,0)
        root.configure(bg="white")
        root.iconphoto(True,PhotoImage(file=assetpath+'padlock.png'))
        root.tk.call('tk', 'scaling', 1.6)

        style=Style()
        style.configure("TLabel",background="white")

        topf=Frame(root,bg="white")
        topf.pack(pady=20,side=TOP)

        Label(topf,text="Pass-Man",font=("Helvetica",18,'bold'),bg="white").grid(row=0,column=4)
        Label(topf,text="Password manager",font=("Helvetica",8),bg="white").grid(row=1,column=4)
        img=ImageTk.PhotoImage(Image.open(assetpath+"padlock.png").resize((40,40)))
        Label(topf,image=img,bg="white").grid(row=0,column=2,rowspan=2,padx=8)

        # Separator(root,orient=HORIZONTAL).pack()
        # divider=ImageTk.PhotoImage(Image.open(assetpath+"divider.png").resize((300,20)))
        # Label(root,image=divider,bg="green").pack()
        

        detailf=Frame(root,bg="white")
        detailf.pack(pady=25,side=TOP)

        useri=ImageTk.PhotoImage(Image.open(assetpath+"login.png").resize((30,30)))
        Label(detailf,image=useri,bg="white").grid(row=0,column=2,padx=10)
        keyi=ImageTk.PhotoImage(Image.open(assetpath+"key.png").resize((30,30)))
        Label(detailf,image=keyi,bg="white").grid(row=1,column=2,padx=10)
        user=Entry(detailf)
        pwd=Entry(detailf,show="*")
        user.grid(row=0,column=3,columnspan=4)
        pwd.grid(row=1,column=3,columnspan=4)
        # user.insert(0,'Username')
        # pwd.insert(0,'Password')
        user.focus_force()
        pwd.focus_force()


        #submit area starts
        submitf=Frame(root,bg="white")
        submitf.pack(side=TOP,pady=(25,6))

        logini=ImageTk.PhotoImage(Image.open(assetpath+"tick.png").resize((30,30)))
        loginb=Button(submitf,text=" Login",image=logini,compound=LEFT,bg="white",bd=0,activebackground="white",command=lambda : login(user.get(),pwd.get()))
        loginb.pack(side=LEFT,padx=10)

        canceli=ImageTk.PhotoImage(Image.open(assetpath+"cancel.png").resize((30,30)))
        cancelb=Button(submitf,text=" Cancel",image=canceli,compound=LEFT,bg="white",bd=0,activebackground="white",command=exitLogin)
        cancelb.pack(side=LEFT,padx=10)


        #bottom frames
        bottomf=Frame(root,bg="white")
        bottomf.pack(pady=20)
        b1f=Frame(bottomf,bg="white")
        b1f.pack(side=TOP,pady=0)
        b2f=Frame(bottomf,bg="white")
        b2f.pack(side=TOP,pady=0)
        Label(b1f,text="Don't have an account?",bg="white").pack(side=LEFT)
        Button(b1f,text="Sign up",fg="dodger blue",bg="white",bd=0,activebackground="white",activeforeground="dodger blue",command=startSignup).pack(side=LEFT,pady=0,ipady=0)
        Button(b2f,text="Forgot your password?",fg="dodger blue",bg="white",bd=0,activebackground="white",activeforeground="dodger blue",command=startForget).pack(pady=0,ipady=0)

        root.mainloop()


        # Make topfLevelWindow remain on topf until destroyed, or attribute changes.
        # topfLevelWindow.attributes('-topfmost', 'true')
        # title_bar.bind('<B1-Motion>', move_window)


if __name__ == "__main__":
    startLogin()