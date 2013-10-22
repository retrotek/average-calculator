from tkinter import *

import ACS_clone



#######################
#######################
def donothing():
    pass

def roster():
    pass

###########################
#   Student List          #
###########################

def studentListINIT():
    global SL
    SL = []
    for student in ACS_clone.student2average:
        SL.append(student)
    for num in range(0,len(SL)):
        studentList.insert(END, SL[num])

global selectedStudent
selectedStudent = None

def selectStudent(event):
    selectedStudent = SL[int(studentList.curselection()[0])]


############################
#          AREA            #
############################
def areaDestroy(event):
    areaList.children.clear()

def areaListINIT():
    
    global AL
    AL = ['Academics','Athletics', 'Educational Group', 'Family Rep', 'Program', 'Psychotherapy'] 
    for area in AL:
        areaList.insert(END,area)




        
def checkStudent(event):
    if selectedStudent == None:
        Message(root, text='Please select a Student')
    
#############################
#      Daily List           #
#############################
def dailyUPDATE(event):
    pass




#############################




root = Tk()
root.title("Average Calculator")

#######################
#        MENU         #
#######################
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


##########################
#       Frame1           #
##########################

frame1 = Frame(root)
frame1.pack(side=LEFT)
studentLabel = Label(frame1, text="Student List")
studentLabel.pack(side=TOP)
studentList = Listbox(frame1)
studentList.pack(side=LEFT,padx=5)
studentList.bind('<ButtonRelease-1>', selectStudent)

###########################
#       Frame2            #
###########################

frame2 = Frame(root)
frame2.pack(side=LEFT)
areaLabel = Label(frame2, text="Area List")
areaLabel.pack(side=TOP)
areaList= Listbox(frame2)
areaList.pack(padx=5)
areaList.bind('<ButtonRelease-1>', checkStudent)

###########################
#       Frame3            #
###########################
frame3 = Frame(root)
frame3.pack(side=LEFT)
dailyLabel = Label(frame3, text='Daily Averages')
dailyLabel.pack()
dailyList = Listbox(frame3)
dailyList.pack(padx=5)
dailyList.bind('<ButtonRelease-1>', dailyUPDATE)





############################
#        INIT              #
############################

studentListINIT()
areaListINIT()
root.geometry('405x200')
root.mainloop()
