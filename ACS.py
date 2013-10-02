
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
        self.aacademic = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def academic_average(self):
        '''Returns a particular students program average.
        '''
        return singular_average(self.academic)

    def print_academic(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.academic['mon']), 'Tuesday: ' + str(self.academic['tue']),
              'Wednesday: ' + str(self.academic['wed']),'Thursday: ' + str(self.academic['thur'])
              , 'Friday: ' + str(self.aacademic['fri']), 'Saturday: ' + str(self.academic['sat']),
              'Sunday: ' + str(self.academic['sun']))



    def update(self,,week):
        '''Updates a students program average.
        '''
        self.athletics = {'mon':week.mon,'tue':week.tue,'wed':week.wed,'thur':week.thur,'fri':week.fri, 'sat':week.sat,'sun':week.sun}
        
    def average(self,area):
        '''Returns a particular students program average.
        '''
        return singular_average(self.area)

    def print_avg(self):
        '''Prints a student's daily averages for the week.
        '''
        print('Monday: ' + str(self.athletics['mon']), 'Tuesday: ' + str(self.athletics['tue']),
              'Wednesday: ' + str(self.athletics['wed']),'Thursday: ' + str(self.athletics['thur'])
              , 'Friday: ' + str(self.athletics['fri']), 'Saturday: ' + str(self.athletics['sat']),
              'Sunday: ' + str(self.athletics['sun']))

    
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

