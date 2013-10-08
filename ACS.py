
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


            
    
        
class student(object):
    '''An instance of a student.'''

    def __init__(self,name,stage):
        '''
        >>> kurtis = student('Kurtis Knigge','Maintainance',

        '''
        self.name = name
        self.stage = stage
        

        
        self.program = {}
        self.athletics = {}
        self.academic = {}
        self.family_rep = {}
        self.psychotherapy = {}
        self.educational_grp = {}

        
    def __str__(self):
        return self.name + ' ' + self.stage

    def return_info(self):
        return self.name, self.stage
    
############# PROGRAM AVERAGE CODE #################
####################################################
####################################################
    def update_program(self,week):
        '''Updates a students program average.
        '''
        self.program = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def program_average(self):
        '''Returns a particular students program average.
        '''
        return singular_average(self.program)

    def print_program(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.program['mon']), 'Tuesday: ' + str(self.program['tue']),
              'Wednesday: ' + str(self.program['wed']),'Thursday: ' + str(self.program['thur'])
              , 'Friday: ' + str(self.program['fri']), 'Saturday: ' + str(self.program['sat']),
              'Sunday: ' + str(self.program['sun']))
        
                                                                                                                                                                                    
########### ATHLETICS AVERAGE CODE  ##################
######################################################
######################################################
    def update_athletics(self,week):
        '''Updates a students program average.
        '''
        self.athletics = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def athletics_average(self):
        '''Returns a particular students program average.
        '''
        return singular_average(self.athletics)

    def print_athletics(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.athletics['mon']), 'Tuesday: ' + str(self.athletics['tue']),
              'Wednesday: ' + str(self.athletics['wed']),'Thursday: ' + str(self.athletics['thur'])
              , 'Friday: ' + str(self.athletics['fri']), 'Saturday: ' + str(self.athletics['sat']),
              'Sunday: ' + str(self.athletics['sun']))
        
############ ACADEMIC AVERAGE CODE ####################
########################################################
########################################################
    def update_academic(self,week):
        '''Updates a students program average.
        '''
        self.academic = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def academic_average(self):
        '''Returns a particular students program average.
        '''
        return singular_average(self.academic)

    def print_academic(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.academic['mon']), 'Tuesday: ' + str(self.academic['tue']),
              'Wednesday: ' + str(self.academic['wed']),'Thursday: ' + str(self.academic['thur'])
              , 'Friday: ' + str(self.academic['fri']), 'Saturday: ' + str(self.academic['sat']),
              'Sunday: ' + str(self.academic['sun']))
############ FAMILY REP CODE ###########################
########################################################
########################################################
    def update_family_Rep(self,week):
        '''Updates a students program average.
        '''
        self.family_rep = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def family_Rep_average(self):
        '''Returns a particular students program average.
        '''
        return singular_average(self.family_rep)

    def print_family_Rep(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.family_rep['mon']), 'Tuesday: ' + str(self.family_rep['tue']),
              'Wednesday: ' + str(self.family_rep['wed']),'Thursday: ' + str(self.family_rep['thur'])
              , 'Friday: ' + str(self.family_rep['fri']), 'Saturday: ' + str(self.family_rep['sat']),
              'Sunday: ' + str(self.family_rep['sun']))

########### PSYCHOTHERAPY CODE ##########################
#########################################################
#########################################################
    def update_psychotherapy(self,week):
        '''Updates a students program average.
        '''
        self.psychotherapy = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def psychotherapy_average(self):
        '''Returns a particular students program average.
        '''
        return singular_average(self.psychotherapy)

    def print_psychotherapy(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.psychotherapy['mon']), 'Tuesday: ' + str(self.psychotherapy['tue']),
              'Wednesday: ' + str(self.psychotherapy['wed']),'Thursday: ' + str(self.psychotherapy['thur'])
              , 'Friday: ' + str(self.psychotherapy['fri']), 'Saturday: ' + str(self.psychotherapy['sat']),
              'Sunday: ' + str(self.psychotherapy['sun']))
   
############# EDUCATIONAL GROUPS ########################
#########################################################
#########################################################
    def update_educational_grp(self,week):
        '''Updates a students program average.
        '''
        self.educational_grp = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def educational_grp_average(self):
        '''Returns a particular students program average.
        '''
        return singular_average(self.educational_grp)

    def print_educational_grp(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.educational_grp['mon']), 'Tuesday: ' + str(self.educational_grp['tue']),
              'Wednesday: ' + str(self.educational_grp['wed']),'Thursday: ' + str(self.educational_grp['thur'])
              , 'Friday: ' + str(self.educational_grp['fri']), 'Saturday: ' + str(self.educational_grp['sat']),
              'Sunday: ' + str(self.educational_grp['sun']))





        
def singular_average(week):
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
            
    return total/dayCount


########## END OF TRIAL CODE #############

class program(week):
    '''A week of daily averages for the PROGRAM area.
    '''

class athletics(week):
    '''A week of daily averages for the ATHLETICS area.
    '''

class academic(week):
    '''A week of daily averages for the ACADEMIC area.
    '''


class family_rep(week):
    '''A week of daily averages for the FAMILY REP area.
    '''


class psychotherapy(week):
    '''A week of daily averages for the PSYCHOTHERAPY area.
    '''


class educational_grp(week):
    '''A week of daily averages for the EDUCATIONAL GROUP area
    '''

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
        print("You added " + name + " to the student list")
    
    
def global_var_set():
    global student2average
    student2average = {}
    for num in range(0,len(student_list())):
        student2average[student_list()[num]] = {'Program':{'Mon':None,'Tue':None,'Wed':None,'Thur':None,'Fri':None,'Sat':None,'Sun':None},
        'Athletics':{'Mon':None,'Tue':None,'Wed':None,'Thur':None,'Fri':None,'Sat':None,'Sun':None},
        'Academics':{'Mon':None,'Tue':None,'Wed':None,'Thur':None,'Fri':None,'Sat':None,'Sun':None},
        'Psychotherapy':{'Mon':None,'Tue':None,'Wed':None,'Thur':None,'Fri':None,'Sat':None,'Sun':None},
        'Family Rep':{'Mon':None,'Tue':None,'Wed':None,'Thur':None,'Fri':None,'Sat':None,'Sun':None},
        'Educational Group':{'Mon':None,'Tue':None,'Wed':None,'Thur':None,'Fri':None,'Sat':None,'Sun':None}}
    
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
    

    


def student_info():
    ''' (str) -> dict
    '''
    student = input("Please type the student's name:  ")
    area = input("Please type the desired area (Overall, Academics, Athletics, Educational Group, Family Rep, Program, Psychotherapy) :  " )
    x = student2average[student]
    if area.lower() == 'overall':
        '''i = 0
        for num in range(0,len(student2average[student])):
            print(singular_average(student2average[student][i]))
            i+=1'''
        print("Academics: \n" + x['Academics'])
        print("Athletics: \n" + x['Athletics'])
        print("Educational Group: \n" + x['Educational Group']
        print("Program: \n" + x['Program']
    else:
        return x[area]
        
            
        
    

def update():
    student = input("Which student would you like to update?  ")
    info = students2average[student]
    
    
###########################################################
###########################################################
import time
def initialize():
    print("Please type one of the following commands: ")
    print("ROSTER, ADD, DELETE, UPDATE, INSPECT, EXIT")
    x = input()
    y = x.lower()
    if y == 'roster':
        print(student_list())
       
    elif y == 'add':
        add_student()
        global_var_set()
    elif y == 'delete':
        delete_student()
        global_var_set()
    elif y == 'update':
        ########## FIX!!!! ######
        None
        
    elif y == 'inspect':
        print(student_info())
        
    elif y == 'exit':
        print("..........")
        exit()
    else:
        print("Error: Invalid Command")
    
    print('\n')
    initialize()
    

print("Welcome to the Average Calculator Suite 0.1!")
print("Coded by Kurtis Knigge\n")
global_var_set()
initialize()


