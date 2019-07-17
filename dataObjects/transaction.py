from flask import json

from dataObjects.saveable import saveable
from dataObjects.parser import DataHelper as p

class Transaction(saveable):
    def __init__(self, transactionid, accountid, amount, date):
        self.transactionid = transactionid
        self.accountid = accountid
        self.amount = amount
        if isinstance(date, str):
            self.date = p.parsedate(date)
        else:
            self.date = date

    def __init__(self):
        pass

    def save(self):
        cur = saveable.getCursor(self)
        cur.execute('insert into `Transaction`(DATE,AMOUNT, ACCOUNTID) values (?,?,?)', [self.date,  self.amount,self.accountid])
        saveable.cleanup(self, cur)

    def save(self, date, amount, accountid):
        cur = saveable.getCursor(self)
        cur.execute('insert into `Transaction`(DATE,AMOUNT, ACCOUNTID) values (?,?,?)',
                    [date, amount, accountid])
        saveable.cleanup(self, cur)