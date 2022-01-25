import re

class RegexOperations():
    '''
    Regex Functions
    '''
    def getBirthDay(element):
        '''
        :param element: str date format
        :returns: index[2] of listed date elements
        '''
        return re.findall('\d+',element)[2]

    def getBirthMonth(element):
        '''
        :param element: str date format
        :returns: index[1] of listed date elements
        '''
        return re.findall('\d+',element)[1]

    def getBirthYear(element):
        '''
        :param element: str date format
        :returns: index[0] of listed date elements
        '''
        return re.findall('\d+',element)[0]

    def verifyEmailUser(username,email):
        '''
        Checks character counts from left to right 
        :param username,email: takes full data
        :returns: Boolean 
        '''
        email = re.split(r'@', email)[0]
        c=0
        for i in username:
            if re.search(i,email):
                c=c+1
        if c >= 3: return 1 
        else: return 0

    def verifyUserName(username,name):
        '''
        Checks character counts from left to right 
        :param username,name: takes full data
        :returns: Boolean 
        '''
        c=0
        for i in name.replace(' ', '').lower():
            if re.search(i,username):
                c=c+1
        if c >= 3: return 1 
        else: return 0
