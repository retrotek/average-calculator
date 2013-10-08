
##  Average Calculator Suite 0.1
##
##  Written by: Kurtis Knigge
##
##




########### TRIAL CODE #################

class week(dict):
    ''' A dictionary that lists the days of the week and their corresponding
    average.''' 

    def __init__(self,mon=None,tue=None,wed=None,thur=None,fri=None,sat=None,sun=None):


        self.mon = mon
        self.tue = tue
        self.wed = wed
        self.thur = thur
        self.fri = fri
        self.sat = sat
        self.sun = sun


            
    
    

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

    if daycount == 0:
        print('There are no daily averages \n')
    else:    
        return total/daycount

'''def singular_average(week):
    total=0
    dayCount=0
    if week.mon != None:
            total+= week.mon
            dayCount+=1
    if week.tue != None:
            total+= week.tue
            dayCount+=1
    if week.wed != None:
            total+= week.wed
            dayCount+=1
    if week.thur != None:
            total+= week.thur
            dayCount+=1
    if week.fri != None:
            total+= week.fri
            dayCount+=1
    if week.sat != None:
            total+= week.sat
            dayCount+=1
    if week.sun != None:
            total+= week.sun
            dayCount+=1
            
    return total/dayCount'''


########## END OF TRIAL CODE #############



########## UI FUNCTIONS #####################
#############################################


def student_list():
    students = []
    x = open('names.txt','r')
    counter = 1
    for line in x:
        '''if counter % 2 ==0:
            stage = line
        else:
            name = line

        counter+=1
    students.append(name.rstrip('\)'''
        name = line
        students.append(name.rstrip('\n'))
    x.close()
    return students

def add_student():
    num = input('How many students would you like to add?  ')
    
    for it in range(0,int(num)):
        name = input("Please type the student's name:  ")
        x = open('names.txt','a')
        x.write('\n' + name)
        x.close()
        student2average[name] = {"Program":{"Mon":None,"Tue":None,"Wed":None,"Thur":None,"Fri":None,"Sat":None,"Sun":None},
        "Athletics":{"Mon":None,"Tue":None,"Wed":None,"Thur":None,"Fri":None,"Sat":None,"Sun":None},
        "Academics":{"Mon":None,"Tue":None,"Wed":None,"Thur":None,"Fri":None,"Sat":None,"Sun":None},
        "Psychotherapy":{"Mon":None,"Tue":None,"Wed":None,"Thur":None,"Fri":None,"Sat":None,"Sun":None},
        "Family Rep":{"Mon":None,"Tue":None,"Wed":None,"Thur":None,"Fri":None,"Sat":None,"Sun":None},
        "Educational Group":{"Mon":None,"Tue":None,"Wed":None,"Thur":None,"Fri":None,"Sat":None,"Sun":None}}
        print("You added " + name + " to the student list")
        
    
def global_var_set():
    global student2average
    student2average = {}
    for num in range(0,len(student_list())):
        student2average[student_list()[num]] = {"Program":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
        "Athletics":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
        "Academics":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
        "Psychotherapy":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
        "Family Rep":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"},
        "Educational Group":{"Mon":"None","Tue":"None","Wed":"None","Thur":"None","Fri":"None","Sat":"None","Sun":"None"}}
    
def delete_student():
    '''num = input('How many students would you like to delete?  ')
    students = names()
    file = open('names.txt','w')
    for x in range(0,int(num)):
        name = input("Please type the student's name:  ")
        students.remove(name)
        file.write(students[x] + '\n')
        print("You removed " + name + " from the student list")
    list = str(students).lstrip('[')
    list = list.rstrip(']')'''
    students = student_list()
    
    name = input("Please type the student's name:  ")
    students.remove(name)
    file = open('names.txt','w')
    for x in range(0,len(students)):
        file.write(students[x] + '\n')
    print("You removed " + name + " from the student list")
    file.close()
    del student2average[name]

    


def student_info():
    ''' (str) -> dict
    '''
    student = input("Please type the student's name:  ")
    area = input("Please type the desired area (Overall, Academics, Athletics, Educational Group, Family Rep, Program, Psychotherapy) :  " )
    x = student2average[student]
    m = 'Mon'
    t = 'Tue'
    w = 'Wed'
    th = 'Thur'
    f = 'Fri'
    s = 'Sat'
    sn = 'Sun'
    aca = x['Academics']
    ath = x['Athletics']
    edu = x['Educational Group']
    pro = x['Program']
    psy = x['Psychotherapy']
    fam = x['Family Rep']
    
    if area.lower() == 'overall':
        '''i = 0
        for num in range(0,len(student2average[student])):
            print(singular_average(student2average[student][i]))
            i+=1'''
        print("Academics: \n" + m + ':  ' + str(aca[m]) + '\n' +
              t + ': ' + str(aca[t]) + '\n' + w + ': ' + str(aca[w]) + '\n'
              + th + ': ' + str(aca[th]) + '\n' + f + ': ' + str(aca[f]) + '\n'
              + s + ': ' + str(aca[s]) + '\n' + sn + ': ' + str(aca[sn]) + '\n' + '\n')
        print(singular_average(aca))
        
        print("Athletics: \n" + m + ':  ' + str(ath[m]) + '\n' +
              t + ': ' + str(ath[t]) + '\n' + w + ': ' + str(ath[w]) + '\n'
              + th + ': ' + str(ath[th]) + '\n' + f + ': ' + str(ath[f]) + '\n'
              + s + ': ' + str(ath[s]) + '\n' + sn + ': ' + str(ath[sn]) + '\n' + '\n')
        print(singular_average(ath))
       
        print("Educational Group: \n" + m + ':  ' + str(edu[m]) + '\n' +
              t + ': ' + str(edu[t]) + '\n' + w + ': ' + str(edu[w]) + '\n'
              + th + ': ' + str(edu[th]) + '\n' + f + ': ' + str(edu[f]) + '\n'
              + s + ': ' + str(edu[s]) + '\n' + sn + ': ' + str(edu[sn]) + '\n' + '\n')
        print(singular_average(edu))
        
        print("Family Rep:  \n" + m + ':  ' + str(fam[m]) + '\n' +
              t + ': ' + str(fam[t]) + '\n' + w + ': ' + str(fam[w]) + '\n'
              + th + ': ' + str(fam[th]) + '\n' + f + ': ' + str(fam[f]) + '\n'
              + s + ': ' + str(fam[s]) + '\n' + sn + ': ' + str(fam[sn]) + '\n' + '\n')
        print(singular_average(fam))
        
        print("Program: \n" + m + ':  ' + str(pro[m]) + '\n' +
              t + ': ' + str(pro[t]) + '\n' + w + ': ' + str(pro[w]) + '\n'
              + th + ': ' + str(pro[th]) + '\n' + f + ': ' + str(pro[f]) + '\n'
              + s + ': ' + str(pro[s]) + '\n' + sn + ': ' + str(pro[sn]) + '\n' + '\n')
        print(singular_average(pro))
       
        print("Psychotherapy:  \n" + m + ':  ' + str(psy[m]) + '\n' +
              t + ': ' + str(psy[t]) + '\n' + w + ': ' + str(psy[w]) + '\n'
              + th + ': ' + str(psy[th]) + '\n' + f + ': ' + str(psy[f]) + '\n'
              + s + ': ' + str(psy[s]) + '\n' + sn + ': ' + str(psy[sn]) + '\n' + '\n')
        print(singular_average(psy))
                
    else:
        if area.lower() == 'academics':
            print("Academics: \n" + m + ':  ' + str(aca[m]) + '\n' +
              t + ': ' + str(aca[t]) + '\n' + w + ': ' + str(aca[w]) + '\n'
              + th + ': ' + str(aca[th]) + '\n' + f + ': ' + str(aca[f]) + '\n'
              + s + ': ' + str(aca[s]) + '\n' + sn + ': ' + str(aca[sn]) + '\n' + '\n')
            print(singular_average(aca))
        elif area.lower() == 'athletics':
            print("Athletics: \n" + m + ':  ' + str(ath[m]) + '\n' +
              t + ': ' + str(ath[t]) + '\n' + w + ': ' + str(ath[w]) + '\n'
              + th + ': ' + str(ath[th]) + '\n' + f + ': ' + str(ath[f]) + '\n'
              + s + ': ' + str(ath[s]) + '\n' + sn + ': ' + str(ath[sn]) + '\n' + '\n')
            print(singular_average(ath))
        elif area.lower() == 'Educational Group':
            print("Educational Group: \n" + m + ':  ' + str(edu[m]) + '\n' +
              t + ': ' + str(edu[t]) + '\n' + w + ': ' + str(edu[w]) + '\n'
              + th + ': ' + str(edu[th]) + '\n' + f + ': ' + str(edu[f]) + '\n'
              + s + ': ' + str(edu[s]) + '\n' + sn + ': ' + str(edu[sn]) + '\n' + '\n')
            print(singular_average(edu))
        elif area.lower() == 'family rep':
            print("Family Rep:  \n" + m + ':  ' + str(fam[m]) + '\n' +
              t + ': ' + str(fam[t]) + '\n' + w + ': ' + str(fam[w]) + '\n'
              + th + ': ' + str(fam[th]) + '\n' + f + ': ' + str(fam[f]) + '\n'
              + s + ': ' + str(fam[s]) + '\n' + sn + ': ' + str(fam[sn]) + '\n' + '\n')
            print(singular_average(fam))
        elif area.lower() == 'program':
            print("Program: \n" + m + ':  ' + str(pro[m]) + '\n' +
              t + ': ' + str(pro[t]) + '\n' + w + ': ' + str(pro[w]) + '\n'
              + th + ': ' + str(pro[th]) + '\n' + f + ': ' + str(pro[f]) + '\n'
              + s + ': ' + str(pro[s]) + '\n' + sn + ': ' + str(pro[sn]) + '\n' + '\n')
            print(singular_average(pro))
        elif area.lower() == 'psychotherapy':
            print("Psychotherapy:  \n" + m + ':  ' + str(psy[m]) + '\n' +
              t + ': ' + str(psy[t]) + '\n' + w + ': ' + str(psy[w]) + '\n'
              + th + ': ' + str(psy[th]) + '\n' + f + ': ' + str(psy[f]) + '\n'
              + s + ': ' + str(psy[s]) + '\n' + sn + ': ' + str(psy[sn]) + '\n' + '\n')
            print(singular_average(psy))
        else:
            print('Error: Invalid Input')
        
    

def update():
    name = input("Which student would you like to update?  ")
    student = student2average[name]
    area_name = input("Which area would you like to update?   ")
    area = student[area_name]
    m = input("Monday Average:  ")
    t = input("Tuesday Average:  ")
    w = input("Wednesday Average:  ")
    th = input("Thursday Average:  ")
    f = input("Friday Average:  ")
    s = input("Saturday Average:  ")
    sn = input("Sunday Average:  ")
    if m != '':
        area['Mon'] = float(m)
    if t != '':   
        area['Tue'] = float(t)
    if w != '':
        area['Wed'] = float(w)
    if th != '':
        area['Thur'] = float(th)
    if f != '':
        area['Fri'] = float(f)
    if s != '':
        area['Sat'] = float(s)
    if sn != '':
        area['Sun'] = float(sn)

def save():
    now = datetime.datetime.now()
    header = str(now.month) + '/' + str(now.day)
    file = open('savedAverages.txt', 'w')
    file.write(json.dumps(student2average))
    file.close()
    print("Averages saved.")
    
def load():
    file = open('savedAverages.txt','r')
    x = json.loads(file.read())
    global student2average
    student2average = x
###########################################################
###########################################################

def initialize():
    print("Please type one of the following commands: ")
    print("ROSTER, ADD, DELETE, UPDATE, INSPECT, SAVE, LOAD, EXIT")
    x = input()
    y = x.lower()
    if y == 'roster':
        print(student_list())
       
    elif y == 'add':
        add_student()
        
    elif y == 'delete':
        delete_student()
    elif y == 'update':
        
        update()
        
    elif y == 'inspect':
        print(student_info())
    elif y == 'save':
        save()
    elif y == 'load':
        load()
    elif y == 'exit':
        print("..........")
        exit()
    else:
        print("Error: Invalid Command")
    
    print('\n')
    initialize()
    
import datetime
import json
global student2average
student2average = {}
print("Welcome to the Average Calculator Suite 0.1!")
print("Coded by Kurtis Knigge\n")
global_var_set()
initialize()


