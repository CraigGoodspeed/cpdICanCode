from flask import json
from dataObjects.saveable import saveable


class Client(saveable):
    def __init__(self, clientid, name, surname, password, idnumber):
        self.clientid = clientid
        self.name = name
        self.surname = surname
        self.password = password
        self.idnumber = idnumber

    def __init__(self):
        pass

    def save(self):
        cur = saveable.getCursor(self)
        cur.execute('insert into Client values (?,?,?,?,?)', [self.clientid, self.idnumber, self.name, self.password, self.surname])
        saveable.cleanup(self, cur)

    def logon(self, username, password):
        cur = saveable.getCursor(self)
        data = cur.execute('select clientid,idnumber,name,surname from client where name = ? and password = ?',[username,password])
        readHere = data.fetchone()
        self.clientid = readHere[0]
        self.idnumber = readHere[1]
        self.name = readHere[2]
        self.surname = readHere[3]
        saveable.cleanup(self, cur)

