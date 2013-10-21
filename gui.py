from tkinter import *

import ACS_clone
 
def donothing():
    pass

def roster():
    x = Label(root, text='Hello')
    x.grid(row=2, column=1)

def studentListClick(event):
    '''works = Label(root, text=list[int(studentList.curselection()[0])]).grid(row=5,column=5)
    '''
    student = list[int(studentList.curselection()[0])]
    x = Label(root, text=student).grid(row=2,column=6)
    
    areas = Listbox(root)
    
    for area in ACS_clone.student2average[student]:
        areas.insert(END, area)


    areas.grid(row=2, column=5)
    
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

studentMenu.add_command(label='View Roster', command=roster)
studentMenu.add_command(label='Add Student', command=donothing)
studentMenu.add_command(label='Delete Student', command=donothing)

menubar.add_cascade(label='Students', menu=studentMenu)

averageMenu = Menu(menubar)

averageMenu.add_command(label='Quick List', command=donothing)
averageMenu.add_command(label='Inspect', command=donothing)
averageMenu.add_command(label='Update', command=donothing)

menubar.add_cascade(label='Averages', menu=averageMenu)



studentList = Listbox(root)
list = []
for student in ACS_clone.student2average:
    list.append(student)
for num in range(0, len(ACS_clone.student2average)):
        studentList.insert(num, list[num])
studentList.bind('<Double-1>', studentListClick)
studentList.grid(row=2, column=1)





root.config(menu=menubar)
root.geometry('400x400')
root.mainloop()

