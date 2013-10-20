from tkinter import *

import ACS_clone
 
def donothing():
    pass


root = Tk()
root.title("Average Calculator Suite")


menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar)
fileMenu.add_command(label='New', command=donothing)
fileMenu.add_command(label='Save', command=donothing)
fileMenu.add_command(label='Load', command=donothing)
fileMenu.add_command(label='Exit', command=exit)

menubar.add_cascade(label='File', menu=fileMenu)

studentMenu = Menu(menubar)

studentMenu.add_command(label='View Roster', command=donothing)
studentMenu.add_command(label='Add Student', command=donothing)
studentMenu.add_command(label='Delete Student', command=donothing)

menubar.add_cascade(label='Students', menu=studentMenu)

averageMenu = Menu(menubar)

averageMenu.add_command(label='Quick List', command=donothing)
averageMenu.add_command(label='Inspect', command=donothing)
averageMenu.add_command(label='Update', command=donothing)

menubar.add_cascade(label='Averages', menu=averageMenu)

contentFrame = Frame(root)

studentlist = Listbox(contentFrame)
for students in ACS_clone.student2average:
    studentlist.insert(END, students)

studentlist.bind("<<ListboxSelect>>") 


root.config(menu=menubar)
root.mainloop()

