    #Ian Harwell 000683773

    # all main segments of program included in line
    # entire program = O(N^2) quadratic

from Time import *
from Self_Adjusting_Algorithms import *

# Initialization
# sets package data
setPackageData('WGUPS Package File.csv')                                                # O(N) linear

# Main Functions

# initial function
# O(N^2) quadratic
def mainUserInterfaceInit():
    # sets packages in trucks - prioritizes the delivery deadlines and follows other project requirements
    setPackagesInTrucks()  # sets packageList                                           # O(N^2) quadratic

    # sets distance data
    setPackageListAddressesAllTrucks()  # sets street addresses list                    # O(N^2) quadratic
    setAddressKeyListAllTrucks()  # sets address list for keys/names                    # O(N^2) quadratic
    setUniqueAddressKeyListAllTrucks()  # sets unique address keys/names                # O(N) linear
    setAllAddressesInOptimalRouteOrderAllTrucks()  # sets optimal address keys/names    # O(N^2) quadratic
    setOptimalPackageListAddressesAllTrucks()  # sets optimal street addresses list     # O(N^2) quadratic
    setOptimalPackageListAllTrucks()  # sets optimal package list                       # O(N^2) quadratic
    setTotalRouteMileageAllTrucks()  # sets total route mileage                         # O(N^2) quadratic

    # sets time data
    setTimeBetweenLocationsListAllTrucks()  # sets time between locations               # 0(N) linear
    setDeliveryTimeStampAllTrucks()  # sets delivery timestamp as package status        # 0(N^2) quadratic

# updates package delivery address of package 9 as long as its later than 10:20 per project requirements
# O(N^2) quadratic -- due to mainUserInterfaceInit() call
def deliveryAddressUpdateCheck(userInputTime):
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = int((getattr(p, 'ID')))
        if pID == 9 and userInputTime > '1020':
            # update to correct address
            setattr(p, 'address', '410 S State St')
    mainUserInterfaceInit()

# User Interface
# O(N^2) quadratic

# validates entered time before moving to main form
# O(1) constant
def mainUserInterface():
    print('\nEnter a time after 08:00 (in 24 hour format, no colons. For example: 0900 instead of 9:30 AM)')
    userInputTime = input()
    # time formatting check
    if len(userInputTime) != 4:
        print('Only a four digit number is allowed. Please try again')
        mainUserInterface()
    if userInputTime >= '2400' or '-' in userInputTime:
        print('A number between 0000 and 2359 is required')
        mainUserInterface()

    # user interface main form
    # O(N^2) quadratic
    def mainForm():
        print('\nEnter an Option:')
        print('1: View ALL info (all trucks + all packages)')
        print('2: View TRUCK info')
        print('3: View PACKAGE info')
        userInputMain = input()
        if userInputMain == '1':
            deliveryAddressUpdateCheck(userInputTime)                # O(N^2) quadratic
            getAllDataAtSetTime(userInputTime)                       # O(N) linear
            endProgram()                                             # O(1) constant
        elif userInputMain == '2':
            deliveryAddressUpdateCheck(userInputTime)                # O(N^2) quadratic
            getAllTruckDataAtSetTime(userInputTime)                  # O(N) linear
            endProgram()                                             # O(1) constant
        elif userInputMain == '3':
            # O(N^2) quadratic
            def packageSearch():
                print('\nEnter an Option:')
                print('1: View All Package Data')
                print('2: View Specific Package Data by ID')
                userInputPackageSearch = int(input())
                if userInputPackageSearch == 1:
                    deliveryAddressUpdateCheck(userInputTime)         # O(N^2) quadratic
                    getAllPackageDataAtSetTime(userInputTime)         # O(N) linear
                    endProgram()                                      # O(1) constant
                elif userInputPackageSearch == 2:
                    deliveryAddressUpdateCheck(userInputTime)         # O(N^2) quadratic
                    getSpecificPackageDataAtSetTime(userInputTime)    # O(N) linear
                    endProgram()                                      # O(1) constant
                else:
                    print('Please enter a number 1-2')
                    packageSearch()                                   # O(N^2) quadratic
            packageSearch()                                           # O(N^2) quadratic
        else:
            print('Please enter a number 1-3')
            mainForm()                                                # O(N^2) quadratic
    mainForm()                                                        # O(N^2) quadratic

# quits program
# O(1) constant
def endProgram():
    print('\nStart over for new search')
    quit()

# Main Function Calls

mainUserInterfaceInit()                                                # O(N^2) quadratic
mainUserInterface()                                                    # O(N^2) quadratic
