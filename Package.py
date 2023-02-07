from Hash import *
import csv

packageHashTable = ChainingHashTable(40)

class Package:
    def __init__(self, ID, address, city, state, zipCode, deadline, weight, specialNotes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.specialNotes = specialNotes
        self.status = status

def setPackageData(fileName):
    with open(fileName) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')
        next(packageData)
        for package in packageData:
            if package[5] == '9:00 AM':
                package[5] = '0900'
            elif package[5] == '10:30 AM':
                package[5] = '1030'
            elif package[5] == 'EOD':
                package[5] = '1700'
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipCode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pSpecialNotes = package[7]
            pStatus = 'At the Hub'

            p = Package(pID, pAddress, pCity, pState, pZipCode, pDeadline, pWeight, pSpecialNotes, pStatus)

            packageHashTable.insert(pID, p)

def getPackageData():
    print('Package Data:')
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = int((getattr(p, 'ID')))
        pAddress = (getattr(p, 'address'))
        pCity = (getattr(p, 'city'))
        pState = (getattr(p, 'state'))
        pZipCode = (getattr(p, 'zipCode'))
        pDeadline = (getattr(p, 'deadline'))
        pWeight = (getattr(p, 'weight'))
        pSpecialNotes = (getattr(p, 'specialNotes'))
        if pSpecialNotes == '':
            pSpecialNotes = 'n/a'
        pStatus = (getattr(p, 'status'))
        print('Package ID:', pID, '| Address:', pAddress, '| City:', pCity, '| State:', pState, '| Zip:',
              pZipCode, '| Deadline:', pDeadline, '| Weight:', pWeight, '| Special Notes:', pSpecialNotes,
              '| Status:', pStatus)

def getPackageDataByID(userInput):
    print('\nRequested Package Data: ')
    p = (packageHashTable.search(userInput))
    pID = int((getattr(p, 'ID')))
    pAddress = (getattr(p, 'address'))
    pCity = (getattr(p, 'city'))
    pState = (getattr(p, 'state'))
    pZipCode = (getattr(p, 'zipCode'))
    pDeadline = (getattr(p, 'deadline'))
    pWeight = (getattr(p, 'weight'))
    pSpecialNotes = (getattr(p, 'specialNotes'))
    if pSpecialNotes == '':
        pSpecialNotes = 'n/a'
    pStatus = (getattr(p, 'status'))
    print('Package ID:', pID, '| Address:', pAddress, '| City:', pCity, '| State:', pState, '| Zip:',
          pZipCode, '| Deadline:', pDeadline, '| Weight:', pWeight, '| Special Notes:', pSpecialNotes,
          '| Status:', pStatus)
