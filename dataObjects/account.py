import parser
from dataObjects import accounttype as AccountType
from dataObjects import parser as p
from flask import json

from dataObjects.saveable import saveable



class Account(saveable):
    def __init__(self, accountID, clientID, accountNumber, accountType, dateCreated):
        self.accountID = accountID
        self.clientID = clientID
        self.accountNumber = accountNumber
        self.accountType = AccountType.AccountType.parse(accountType)
        self.dateCreated = p.DataHelper.parsedate(dateCreated)

    def __init__(self):
        pass



    def save(self):
        cur = saveable.getCursor(self)
        cur.execute('insert into Account values (?,?,?,?,?)', [self.accountID,self.accountNumber, self.accountType, self.clientID, self.dateCreated])
        saveable.cleanup(self, cur)

    def create(self, accountID, clientID, accountNumber, accountType, dateCreated):
        self.accountID = accountID
        self.clientID = clientID
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.dateCreated = dateCreated

    def serialize(self):
        type = AccountType.AccountType(self.accountType)
        return {
            'accountID': self.accountID,
            'clientID': self.clientID,
            'accountNumber': self.accountNumber,
            'accountType': type.name,
            'dateCreated': self.dateCreated,
        }


    def getAccountsByClientID(self, cid):
        toReturn = []
        cur = saveable.getCursor(self)
        toItterate = cur.execute("select accountID,clientID,accountNumber,accountType,dateCreated from account where clientID = ?",[cid]).fetchall()
        for item in toItterate:
            addMe = Account()
            addMe.create(item[0],item[1],item[2],item[3],item[4])
            toReturn.append(addMe)
        saveable.cleanup(self,cur)
        return toReturn


    def queryBalance(self, accountID):
        cur = saveable.getCursor(self)
        data = cur.execute("select sum(amount) from `transaction` where accountID = ?", [accountID]).fetchone()
        saveable.cleanup(self, cur)
        toReturn = data[0]
        if toReturn is None:
            toReturn = 0

        return toReturn
