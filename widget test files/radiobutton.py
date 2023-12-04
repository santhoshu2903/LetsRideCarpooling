from tkinter import *
from tkinter import ttk

root=Tk()
root.grid_anchor(anchor='center')

image=PhotoImage(file='HOME.png')

style=ttk.Style()

def changetheme():
    themeval=themevar.get()
    style.theme_use(themeval)
   
themevar=StringVar()
themevar.set("vista")

btn1=Radiobutton(root,text='winnative theme',value="winnative",command=changetheme,variable=themevar)
btn2=Radiobutton(root,text='clam theme',value="clam",command=changetheme,variable=themevar)
btn3=Radiobutton(root,text='alt theme',value="alt",command=changetheme,variable=themevar)
btn4=Radiobutton(root,text='classic theme',value="classic",command=changetheme,variable=themevar)
btn5=Radiobutton(root,text='vista theme',value="vista",command=changetheme,variable=themevar)
btn6=Radiobutton(root,text='xpnative theme',value="xpnative",command=changetheme,variable=themevar)

btn1.grid(row=0,column=2)
btn2.grid(row=1,column=2)
btn3.grid(row=2,column=2)
btn4.grid(row=3,column=2)
btn5.grid(row=0,column=3)
btn6.grid(row=1,column=3)

changetheme()

var=IntVar()

radiobutton1=ttk.Radiobutton(root, text='Radio Button 1', value=1, variable=var)
radiobutton1.grid(row=0, column=0, padx=10, pady=10)

radiobutton2=ttk.Radiobutton(root, text='Radiobutton2', value=2, variable=var, image=image, width=20)
radiobutton2.grid(row=1, column=0, padx=15, pady=15)

radiobutton3=ttk.Radiobutton(root, text='Radiobutton3', value=3, variable=var, width=20, compound='text', style='Toolbutton')
radiobutton3.grid(row=2, column=0, padx=15, pady=15)

radiobutton4=ttk.Radiobutton(root, text='Radiobutton4', value=4, variable=var, image=image, compound="top", style='Toolbutton')
radiobutton4.grid(row=3, column=0, padx=15, pady=15)

root.mainloop()