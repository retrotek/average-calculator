from tkinter import *
from tkinter import filedialog

import ACS_clone



##########################
##########################
def donothing():
    pass


def fileNew():
    studentList.delete(0,END)
    areaList.delete(0,END)
    dailyList.delete(0,END)
    
    ACS_clone.student2average = {}
    global SL
    SL = []
    
def fileSave():
    ACS_clone.save()

def fileLoad():
    ACS_clone.load()
    studentList.delete(0,END)
    studentListINIT()


def viewRoster():
    def close():
        roster.destroy()
    roster = Tk()
    roster.title("Roster")
    for names in SL:
        Label(roster, text=names, justify=CENTER).pack()
    close = Button(roster,text = 'Close', command=close)
    close.pack()
    roster.mainloop()

def addStudent():
    def add():
        student = entry.get()
        if student != '':
            ACS_clone.student2average[student] = {"Program":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
                "Athletics":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
                "Academics":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
                "Psychotherapy":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
                "Family Rep":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
                "Educational Group":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"}}
            addWindow.destroy()
            studentList.insert(END, student)
            global SL
            
            SL.append(student)
            
            areaList.delete(0,END)
            areaListINIT()
        else:
            def errorClose():
                error.destroy()
                
            error = Tk()
            error.title("Error")
            msg = Message(error, text='Error: Please enter a name', width=200)
            msg.pack()
            close = Button(error, text='Close',command=errorClose)
            close.pack()
            error.mainloop()
        
        
    def close():
        addWindow.destroy()
        
    addWindow = Tk()
    addWindow.title("Add Student")
    msg = Message(addWindow, text='Student Name:', width = 200)
    msg.pack()
    entry = Entry(addWindow,)
    entry.pack()
    bottomFrame = Frame(addWindow)
    bottomFrame.pack(side=BOTTOM)
    add = Button(bottomFrame, text='Add', command=add)
    add.pack(side=LEFT)
    close = Button(bottomFrame, text='Close', command=close)
    close.pack(side=RIGHT)
    addWindow.geometry("200x75")
    addWindow.mainloop()



def deleteStudent():
    def delete(event):
        
        student = SL[int(deleteList.curselection()[0])]
        confirm = Tk()
        confirm.title("Warning")
        msg = Message(confirm, text='Are you sure you want to delete ' + student, width=200)
        msg.pack()
        buttonFrame = Frame(confirm)
        buttonFrame.pack(side=BOTTOM)
        def do():
            del ACS_clone.student2average[student]
            SL.remove(student)
            confirm.destroy()
            deleteWindow.destroy()
            studentList.delete(0,END)
            studentListINIT()
        def dont():
            confirm.destroy()
        yes = Button(buttonFrame, text='Yes', command=do)
        yes.pack(side=LEFT)
        no = Button(buttonFrame, text='No', command=dont)
        no.pack(side=RIGHT)
        confirm.mainloop()
        
       
    def close():
        deleteWindow.destroy()
        
    deleteWindow = Tk()
    deleteWindow.title('Delete Student')
    frame1 = Frame(deleteWindow)
    frame1.pack(side=LEFT)
    studentLabel = Label(frame1, text="Student List")
    studentLabel.pack(side=TOP)
    deleteList = Listbox(frame1, selectmode = SINGLE)
    deleteList.pack(side=LEFT,padx=5)
    deleteList.bind('<ButtonRelease-1>', delete)
    for students in SL:
        deleteList.insert(END, students)
    close=Button(deleteWindow, text='Cancel', command=close)
    close.pack(side=BOTTOM)
    deleteWindow.geometry('200x200')
    deleteWindow.mainloop()

def quickList():
    def singular_average(dict):
        total = 0
        daycount = 0
    
        if dict['Mon'] != "None":
            total += float(dict['Mon'])
            daycount += 1
        if dict['Tue'] != "None":
            total += float(dict['Tue'])
            daycount += 1
        if dict['Wed'] != "None":
            total += float(dict['Wed'])
            daycount += 1
        if dict['Thur'] != "None":
            total += float(dict['Thur'])
            daycount += 1
        if dict['Fri'] != "None":
            total += float(dict['Fri'])
            daycount += 1
        if dict['Sat'] != "None":
            total += float(dict['Sat'])
            daycount += 1
        if dict['Sun'] != "None":
            total += float(dict['Sun'])
            daycount += 1
        if daycount !=0 :    
            return total/daycount
    def overall_avg(areas):
        total = 0
        counter = 0
        for num in range(0, len(areas)):
            if areas[num] == None:
                pass
            else:
                total += areas[num]
                counter +=1
                return total/counter
            
    def close():
        quickList.destroy()
        
    quickList = Tk()
    quickList.title("Quick List")
    
    for student in ACS_clone.student2average:
        x = ACS_clone.student2average[student]
        aca = x['Academics']
        ath = x['Athletics']
        edu = x['Educational Group']
        pro = x['Program']
        psy = x['Psychotherapy']
        fam = x['Family Rep']
        areas = [singular_average(aca),singular_average(ath),singular_average(edu),
                 singular_average(fam),singular_average(pro),singular_average(psy)]
        Label(quickList,text=student+ ':  ' + str(overall_avg(areas)) + '\n', width=25).pack()
        
    close = Button(quickList, text='Close', command=close)
    close.pack()
    quickList.mainloop()



    
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
    if studentList.get(0,END) == ():
        pass
    else:
        global selectedStudent
        selectedStudent = SL[int(studentList.curselection()[0])]
        if len(dailyList.get(0,END)) > 1:
                global dailyList
                dailyList.destroy()
                dailyList = Listbox(frame3, selectmode = SINGLE)
                dailyList.pack(padx=5)
                dailyList.bind('<ButtonRelease-1>', dailyUPDATE)
        
    

############################
#          AREA            #
############################.
def areaDestroy(event):
    areaList.children.clear()

def areaListINIT():
    
    global AL
    AL = ['Academics','Athletics', 'Educational Group', 'Family Rep', 'Program', 'Psychotherapy'] 
    for area in AL:
        areaList.insert(END,area)




global selectedArea
selectedArea = None

def checkStudent(event):
    def destroy(event):
        msgRoot.destroy()
        
    if selectedStudent == None or selectedStudent not in SL:
        msgRoot = Tk()
        msgRoot.title("Error!")
        x = Message(msgRoot, text='Error: Please select a Student', width=200)
        x.pack()
        close = Button(msgRoot, text='Close')
        close.pack(side=BOTTOM)
        close.bind("<ButtonRelease-1>", destroy)
        
        msgRoot.mainloop()
        
    else:
        pass
global week
week = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
def selectArea(event):
    if areaList.curselection() != ():
        global selectedArea
        selectedArea = AL[int(areaList.curselection()[0])]
        if len(dailyList.get(0,END)) > 1:
            global dailyList
            dailyList.destroy()
            dailyList = Listbox(frame3, selectmode = SINGLE)
            dailyList.pack(padx=5)
            dailyList.bind('<ButtonRelease-1>', dailyUPDATE)
        global week
        for days in week:
            dailyList.insert(END, days + ': ' + str(ACS_clone.student2average[selectedStudent][selectedArea][days]))

            
#############################
#      Daily List           #
#############################
global day
day = None

global update
update = None

def dailyUPDATE(event):
    def save():
        update = entry.get()
        if update.lower() != 'none':
            ACS_clone.student2average[selectedStudent][selectedArea][day] = float(update)
        else:
            ACS_clone.student2average[selectedStudent][selectedArea][day]= 'None'
            
        updateRoot.destroy()
        if len(dailyList.get(0,END)) > 1:
            global dailyList
            dailyList.delete(0,END)
        global week
        for days in week:
            dailyList.insert(END, days + ': ' + str(ACS_clone.student2average[selectedStudent][selectedArea][days]))


    def cancel():
        updateRoot.destroy()

    if dailyList.get(0,END) == ():
        pass
    else:
        global day
        day = week[int(dailyList.curselection()[0])]
        updateRoot = Tk()
        updateRoot.title(selectedStudent + ' ' + selectedArea + ': ' + day) 
        updateprompt = Message(updateRoot, text='Enter Average',width=200)
        updateprompt.pack()
        entry = Entry(updateRoot)
        entry.pack()
        entry.insert(0,str(ACS_clone.student2average[selectedStudent][selectedArea][day]))
        bottomFrame = Frame(updateRoot)
        bottomFrame.pack(side=BOTTOM)
        save = Button(bottomFrame, text='Save', command = save)
        save.pack(side=LEFT)
        cancel = Button(bottomFrame, text='Cancel', command = cancel)
        cancel.pack(side=RIGHT)
        updateRoot.geometry('300x75')
        updateRoot.mainloop()


#############################




root = Tk()
root.title("Average Calculator")

#######################
#        MENU         #
#######################
menubar = Menu(root)
root.config(menu=menubar)



fileMenu = Menu(menubar)
fileMenu.add_command(label='New', command=fileNew)
fileMenu.add_command(label='Save', command=fileSave)
fileMenu.add_command(label='Load', command=fileLoad)
fileMenu.add_command(label='Exit', command=exit)

menubar.add_cascade(label='File', menu=fileMenu)

studentMenu = Menu(menubar)

studentMenu.add_command(label='View Roster', command=viewRoster)
studentMenu.add_command(label='Add Student', command=addStudent)
studentMenu.add_command(label='Delete Student', command=deleteStudent)

menubar.add_cascade(label='Students', menu=studentMenu)

averageMenu = Menu(menubar)

averageMenu.add_command(label='Quick List', command=quickList)
##averageMenu.add_command(label='Inspect', command=donothing)
##averageMenu.add_command(label='Update', command=donothing)

menubar.add_cascade(label='Averages', menu=averageMenu)


##########################
#       Frame1           #
##########################

frame1 = Frame(root)
frame1.pack(side=LEFT)
studentLabel = Label(frame1, text="Student List")
studentLabel.pack(side=TOP)
studentList = Listbox(frame1, selectmode = SINGLE)
studentList.pack(side=LEFT,padx=5)
studentList.bind('<ButtonRelease-1>', selectStudent)

###########################
#       Frame2            #
###########################

frame2 = Frame(root)
frame2.pack(side=LEFT)
areaLabel = Label(frame2, text="Area List")
areaLabel.pack(side=TOP)
areaList= Listbox(frame2, selectmode = SINGLE)
areaList.pack(padx=5)
areaList.bind('<Button-1>', checkStudent)
areaList.bind('<ButtonRelease-1>', selectArea)

###########################
#       Frame3            #
###########################
frame3 = Frame(root)
frame3.pack(side=LEFT)
dailyLabel = Label(frame3, text='Daily Averages')
dailyLabel.pack()
dailyList = Listbox(frame3, selectmode = SINGLE)
dailyList.pack(padx=5)
dailyList.bind('<ButtonRelease-1>', dailyUPDATE)





############################
#        INIT              #
############################

studentListINIT()
areaListINIT()
root.geometry('405x200')
root.mainloop()

