from tkinter import *
from tkinter.messagebox import showinfo,showerror,showwarning


root=Tk()
root.geometry("450x600")
root.title("My Calculator")
root.wm_iconbitmap("calc.ico")
root.config(background="#ffe6e6")

#Font Style
fonts=("Verdana",20,'bold')
font2=("Verdana",8,'bold')

#Picture lebel
photo=PhotoImage(file='img/calc.png')
headinglabel1=Label(root,image=photo)
headinglabel1.pack(side=TOP,pady=3)

#Heading
heading=Label(root,text="My Calculator",font=fonts,underline=0, justify=CENTER)
heading.pack(side=TOP,pady=3)

screenvalue= StringVar()
screenvalue.set("")
screen=Entry(root,textvar=screenvalue,font=("times new roman",35, "bold"))
screen.pack(fill=X,ipadx=8, pady=10, padx=10)

#Frames
frame1=Frame(root)
frame1.pack(side=TOP)

#>>>>>>>>>>>>>Function<<<<click_btn_function

def click_btn_function(event):
    print("Clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='=':
        try:
            ex=screen.get()
            answer=eval(ex)
            screen.delete(0,END)
            screen.insert(0,answer)
        except:
            showerror("Error-Calulator","Error")
        return;

    screen.insert(END,text)

def clear():
    screen.delete(0,END)

def quitApp():
    root.destroy()

def backspace():
    ex=screen.get()
    ex= ex[0:len(ex)-1]
    screen.delete(0,END)
    screen.insert(0,ex)






#Buttons
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn= Button(frame1,text=str(temp),font=fonts,width=5,relief="groove",activebackground="#ccff33",fg="#667fcc")
        btn.grid(row=i,column=j,pady=3,padx=3)
        temp=temp+1
        btn.bind('<Button-1>',click_btn_function)

btn0= Button(frame1,text="0",font=fonts,width=5,relief="groove",activebackground="#ccff33",fg="#667fcc")
btn0.grid(row=3,column=0,pady=3,padx=3)

btndot= Button(frame1,text=".",font=fonts,width=5,relief="groove",activebackground="#ccff33",fg="#667fcc")
btndot.grid(row=3,column=1,pady=3,padx=3)

btnequal= Button(frame1,text="=",font=fonts,width=5,relief="ridge",activebackground="#ccff33",fg="#667fcc")
btnequal.grid(row=3,column=2,pady=3,padx=3)

btnplus= Button(frame1,text="+",font=fonts,width=5,relief="groove",activebackground="#ccff33",fg="#667fcc")
btnplus.grid(row=0,column=3,pady=3,padx=3)

btnminus= Button(frame1,text="-",font=fonts,width=5,relief="groove",activebackground="#ccff33",fg="#667fcc")
btnminus.grid(row=1,column=3,pady=3,padx=3)

btnMultiply= Button(frame1,text="*",font=fonts,width=5,relief="groove",activebackground="#ccff33",fg="#667fcc")
btnMultiply.grid(row=2,column=3,pady=3,padx=3)

btnDivide= Button(frame1,text="/",font=fonts,width=5,relief="groove",activebackground="#ccff33",fg="#667fcc")
btnDivide.grid(row=3,column=3,pady=3,padx=3)

btnBackspace= Button(frame1,text="<--",font=fonts,width=10,command=backspace,relief="groove",activebackground="#ccff33",fg="#667fcc")
btnBackspace.grid(row=4,column=0,pady=3,padx=3,columnspan=2)

btnClr= Button(frame1,text="Clear",font=fonts,width=10,command=clear,relief="groove",activebackground="#ccff33",fg="#667fcc")
btnClr.grid(row=4,column=2,pady=3,padx=3,columnspan=2)
btnExit= Button(frame1,text="Exit",font=fonts,command=quitApp,width=10,relief="groove",activebackground="#ccff33",fg="#667fcc")
btnExit.grid(row=5,column=1,pady=3,padx=3,columnspan=2)

#Binding Buttons
btnDivide.bind('<Button-1>',click_btn_function)
btnminus.bind('<Button-1>',click_btn_function)
btnplus.bind('<Button-1>',click_btn_function)
btndot.bind('<Button-1>',click_btn_function)
btnMultiply.bind('<Button-1>',click_btn_function)
btn0.bind('<Button-1>',click_btn_function)
btnClr.bind('<Button-1>')
btnBackspace.bind('<Button-1>')
btnequal.bind('<Button-1>',click_btn_function)
btnExit.bind('<Button-1>')

#####>>>>>>>>>>>>>>>Scientific Calculator<<<<<<<<<<<<<<<<<<<
# menubar=Menu(root)
# ModeMenu=Menu(menubar,tearoff=0)
# ModeMenu.add_command(label="Scientific Calculator")
#
# menubar.add_cascade(label="Mode", menu=menubar)
#
# root.config(menu=menubar)



BottomHeading=Label(root,text="Developed By-Tamjeed Shah\n All Right Reserved",font=font2,underline=0, justify=CENTER)
BottomHeading.pack(side=BOTTOM,pady=3)


root.mainloop()