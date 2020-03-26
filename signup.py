from tkinter import Toplevel,PhotoImage,Button,Label,Frame,W
from tkinter.ttk import Style,Combobox,Entry
from PIL import ImageTk,Image
from passlib.hash import sha256_crypt


#change this to suit your asset path
assetpath='C:\\Users\\skili\\Documents\\GitHub\\Pass-Man\\assets\\'
def exitSignup():
    root.destroy()

def startSignup():
    global root
    root=Toplevel()
    # root.attributes('-topmost',True)
    root.title("  Signup")
    root.geometry("330x620")
    # root.resizable(0,0)
    root.configure(bg="white")
    root.iconphoto(True,PhotoImage(file=assetpath+'login.png'))
    root.tk.call('tk', 'scaling', 1.6)

    style=Style()
    style.configure("TLabel",background="white")

    Label(root,text="CREATE AN ACCOUNT",font=("ARIAL",15,'bold','italic'),bg="dodger blue",fg="white").pack(pady=(20,20),ipadx=10,ipady=10)
    mainf=Frame(root,bg="white")
    mainf.pack(padx=30,pady=(20,5),ipadx=30,ipady=20)


    #making the form
    Label(mainf,text="Username :",font=("Arial",8,'bold'),bg="white").pack(anchor=W)
    userb=Frame(mainf,bg="dodger blue",bd=2)
    userb.pack(anchor=W)
    usere=Entry(userb,width=30)
    usere.pack(anchor=W,ipadx=5,ipady=5)

    Label(mainf,text="Email :",font=("Arial",8,'bold'),bg="white").pack(anchor=W)
    mailb=Frame(mainf,bg="dodger blue",bd=2)
    mailb.pack(anchor=W)
    maile=Entry(mailb,width=30)
    maile.pack(anchor=W,ipadx=5,ipady=5)

    Label(mainf,text="Choose Password :",font=("Arial",8,'bold'),bg="white").pack(anchor=W)
    passb=Frame(mainf,bg="dodger blue",bd=2)
    passb.pack(anchor=W)
    passe=Entry(passb,width=30,show="*")
    passe.pack(anchor=W,ipadx=5,ipady=5)

    Label(mainf,text="Confirm Password :",font=("Arial",8,'bold'),bg="white").pack(anchor=W)
    passcb=Frame(mainf,bg="dodger blue",bd=2)
    passcb.pack(anchor=W)
    passce=Entry(passcb,width=30,show="*")
    passce.pack(anchor=W,ipadx=5,ipady=5)

    #a curated set of security questions
    sec_ques=["What is your pet name?",
    "What was the first company that you worked for?",
    "Where did you meet your spouse?",
    "Where did you go to high school/college?",
    "What city were you born in?"]


    Label(mainf,text="Security Question :",font=("Arial",8,'bold'),bg="white").pack(anchor=W)
    combo=Combobox(mainf,values=sec_ques,width=29,state='readonly')
    combo.pack(anchor=W,pady=(10,10))
    combo.current(0)
    quesb=Frame(mainf,bg="dodger blue",bd=2)
    quesb.pack(anchor=W)
    quese=Entry(quesb,width=30)
    quese.pack(anchor=W,ipadx=5,ipady=5)

    Label(mainf,text="The security question will help you\n login if you forget your password",bg="white").pack(pady=(20,10))
    createb=Button(mainf,width=30,text="Create Account",font=('ARIAL',10,'bold'),bd=0,fg="white",bg="dodger blue",activebackground="dodger blue",activeforeground="white")
    createb.pack(ipadx=5,ipady=5,padx=10,pady=20)
   
    root.mainloop()

if __name__ == "__main__":
    startSignup()
