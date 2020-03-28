from passgen import startPassGen
from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import ImageTk,Image

assetpath='C:\\Users\\skili\\Documents\\GitHub\\Pass-Man\\assets\\'


#class to create indie entries
class UserEntry:
    def __init__(self,master):
        self.master=master
        self.frame=Frame(self.master,bg="white")
        self.frame.pack(padx=10,pady=10)
        self.v=IntVar()
        self.v.set(0)
        self.checkb=ttk.Checkbutton(self.frame,text="",variable=self.v)
        self.checkb.pack(side=LEFT,padx=3)
        self.starb=Button(self.frame,image=starion,bg="white",bd=0)
        self.starb.pack(side=LEFT,padx=3)
        self.titlel=Label(self.frame,text="title1")
        self.titlel.pack(side=LEFT,padx=40)
        self.copyb=Button(self.frame,image=copyi,bg="white",bd=0)
        self.copyb.pack(side=RIGHT,padx=3)
        self.delb=Button(self.frame,image=deli,bg="white",bd=0)
        self.delb.pack(side=RIGHT,padx=3)
        self.editb=Button(self.frame,image=editi,bg="white",bd=0)
        self.editb.pack(side=RIGHT,padx=3)
        

def exitCpanel():
    root.destroy()


#function to move the main window with the cursor drag
def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root
    ywin = ywin - starty
    xwin = xwin - startx

    def move_window(event):
        root.geometry("800x600" + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
    startx = event.x_root
    starty = event.y_root

    rtoppanef.bind('<B1-Motion>', move_window)


#main cpanel gui
def startCpanelGui():

    global root
    root=Tk()
    root.title("  Password Manager")
    root.geometry("800x600")
    # root.resizable(0,0)
    root.configure(bg="white")
    root.iconphoto(True,PhotoImage(file=assetpath+'padlock.png'))
    root.tk.call('tk', 'scaling', 1.6)

    # root.overrideredirect(1)
    # root.attributes('-topmost',1)

    style=ttk.Style()
    style.configure("TLabel",background="white")
    style.configure("TCheckbutton",background="white")
   
    #left pane
    leftpanef=Frame(root,background="#1E1E1E")
    # leftpanef.config(bg="#1E1E1E")
    leftpanef.pack(side=LEFT,fill=Y)
    useri=ImageTk.PhotoImage(Image.open(assetpath+"user.png").resize((40,40)))
    Label(leftpanef,image=useri,bg="#1E1E1E").pack(padx=20,pady=(20,20))

    #right pane
    rightpanef=Frame(root,bg='green')
    rightpanef.pack(fill=X)
    global rtoppanef
    rtoppanef=Frame(rightpanef,bg="#333333")
    rtoppanef.pack(fill=X,side=TOP)
    rtoppanef.bind('<Button-1>', get_pos)
    Button(rtoppanef,text="x",command=exitCpanel).pack(side=RIGHT,padx=0,pady=0,ipadx=0,ipady=0)
    Label(rtoppanef,text="Pass Man",font=('helvetica',18,'bold'),bg="#333333",fg="white").pack()
    Label(rtoppanef,text="The password manager",bg="#333333",fg="white").pack(pady=(0,10))


    #details main frame
    rbottomf=Frame(rightpanef)
    rbottomf.pack(fill=BOTH)


    #entries frame
    entriesfmain=Frame(rbottomf,bg="blue")
    entriesfmain.grid(sticky=E+W+N+S)
    entriesf=Frame(entriesfmain,width=800,bg="red")
    entriesf.pack(side=LEFT)
    
    #declaring global icons for use
    global starion,starioff,deli,editi,copyi
    starion=ImageTk.PhotoImage(Image.open(assetpath+"staron.png").resize((15,15)))
    starioff=ImageTk.PhotoImage(Image.open(assetpath+"staroff.png").resize((15,15)))
    editi=ImageTk.PhotoImage(Image.open(assetpath+"edit.png").resize((15,15)))
    deli=ImageTk.PhotoImage(Image.open(assetpath+"delete.png").resize((15,15)))
    copyi=ImageTk.PhotoImage(Image.open(assetpath+"delete.png").resize((15,15)))

    

    entryheadf=Frame(entriesf)
    entryheadf.pack()
    v=BooleanVar()
    v.set(False)
    maincheck=ttk.Checkbutton(entryheadf,text="",onvalue=True,offvalue=False,variable=v)
    maincheck.pack(side=LEFT)
    starb=Button(entryheadf,image=starioff,bg="white",bd=0)
    starb.pack(side=LEFT)
    Label(entryheadf,text="Title").pack(side=LEFT)
    Label(entryheadf,text="Actions").pack(side=LEFT)

    UserEntry(entriesf)
    UserEntry(entriesf)
    UserEntry(entriesf)
    UserEntry(entriesf)
    UserEntry(entriesf)



    #single entry display frame
    # entryf=Frame(rbottomf)
    # entryf.pack(fill=Y)
    # f1=Frame(entryf)
    # f1.pack(side=TOP,padx=10)
    # titlel=Label(f1,text="Title",bg="blue")
    # titlel.pack(fill=X)
    # userl=Label(f1,text="Username:")
    # userl.pack()
    # urll=Label(f1,text="URL:")
    # urll.pack()




    root.mainloop()

if __name__ == "__main__":
    startCpanelGui()