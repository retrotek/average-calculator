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
    global student
    student = list[int(studentList.curselection()[0])]
    x = Label(frame1, text='Selected Student: ' + student).grid(row=2,column=6)
    global areas
    areas = Listbox(frame1)
    global areaList
    areaList = []
    for area in ACS_clone.student2average[student]:
        areas.insert(END, area)
        areaList.append(area)
    areas.bind('<ButtonRelease-1>', areasClick)
    areas.grid(row=2, column=5)

def areasClick(event):
    
    area = areaList[int(areas.curselection()[0])]
    grades = ACS_clone.student2average[student][area]
    global areaFrame
    areaFrame = Frame(frame2)
    areaFrame.grid(row=5,column=1)
    
    x = Label(areaFrame, text='Selected Area: ' + area).pack()
    dailyAVG = Listbox(frame2)
    week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    for days in week:
        dailyAVG.insert(END, days + ': ' + grades[days])

    dailyAVG.grid(row=6,column=1)
    
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

frame1 = Frame(root)
frame2 = Frame(root)
studentList = Listbox(frame1)
list = []
for student in ACS_clone.student2average:
    list.append(student)
for num in range(0, len(ACS_clone.student2average)):
        studentList.insert(num, list[num])
studentList.bind('<ButtonRelease-1>', studentListClick)
studentList.grid(row=2, column=1)




frame1.grid(row=2, column=1)
frame2.place(x=2,y=150)
root.config(menu=menubar)
root.geometry('400x400')
root.mainloop()

