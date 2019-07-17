import datetime
import re


class DataHelper:
    @staticmethod
    def parsedate(datetoparse):
        '''
        :param datetoparse: string variable, the known formats are
            01-Jan
            02-Jan
            30-Nov
            13-Dec-16
            01-Jul
        :return: where no year is specified we can only assume the current year -- perhaps one should drill into transactions for those accounts.
        '''
        if DataHelper.containsyear(datetoparse):
            return datetime.datetime.strptime(datetoparse, '%d-%b-%y')
        toReturn = datetime.datetime.strptime(datetoparse+'-'+datetime.datetime.today().strftime('%y'), '%d-%b-%y')
        #we dont want to go into the future.
        if toReturn > datetime.datetime.today():
            toReturn = datetime.datetime.strptime(datetoparse+'-'+str(int(datetime.datetime.today().strftime('%y')) - 1), '%d-%b-%y')
        return toReturn

    @staticmethod
    def containsyear(checkme):
        '''
        :param checkme: date format is quite a little curve ball... items not checked for 00
        :return: does it match a valid date....
        this doesnt cater for date ranges -- 31-feb....
        '''
        return re.match('^(([0][1-9])|([1-2][0-9])|([3][0-1]))-((Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jun)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec))-[0-1][0-9]$',checkme)




