
##  Average Calculator Suite 0.1
##
##  Written by: Kurtis Knigge
##
##




########### BETA CODE #################
class student(object):
    '''An instance of a student.'''

    def __init__(self,name,stage,week):
        '''
        >>> kurtis = student('Kurtis Knigge','Maintainance',

        '''
        self.name = name
        self.stage = stage
        self.week = week
        

    def return_info(self):
        return self.name, self.stage, self.week
    
    
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


########## END OF BETA CODE #############

class program(week):



class academics(week):



class family_rep(week):



class psychotherapy(week):



class educational_grp(week):
    
