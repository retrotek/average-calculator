
##  Average Calculator Suite 0.1
##
##  Written by: Kurtis Knigge
##
##


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

    def __init__(self,mon,tue,wed,thur,fri,sat,sun):


        self.mon = mon
        self.tue = tue
        self.wed = wed
        self.thur = thur
        self.fri = fri
        self.sat = sat
        self.sun = sun
        
    
    def average_week(self):
        total=0
        dayCount=0
        for day in self:
            if self.day != None:
                total+= self.day
                dayCount+=1
        return total/dayCount


    
