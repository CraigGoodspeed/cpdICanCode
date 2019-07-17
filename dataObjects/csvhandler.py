import csv
from dataObjects import account, client, transaction, saveable


class csvhandler:
    @staticmethod
    def createSaveable(itemName, row):
        name = csvhandler.cleanFileName(itemName)
        if name == 'Account':
            return account.Account(row[0], row[1], row[2], row[3], row[4])
        elif name == 'Client':
            return client.Client(row[0], row[1], row[2], row[3], row[4])
        elif name == 'Transaction':
            return transaction.Transaction(row[0], row[1], row[2], row[3])
        return "error"

    @staticmethod
    def parseItem(filename):
        with open(filename, 'r') as handle:
            reader = csv.reader(handle)
            next(reader, None)
            for row in reader:
                item = csvhandler.createSaveable(filename, row)
                item.save()

    @staticmethod
    def cleanFileName(filename):
        itemArr = str(filename).split('/')
        return itemArr[len(itemArr)-1][0:len((itemArr[len(itemArr) -1])) -4]


