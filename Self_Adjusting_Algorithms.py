from Package import *
from operator import itemgetter

# Initialization  ------------------------------------------------------------------------------------------------------
# list of packages in each truck
# packages placed based on project requirements (with consideration to optimal mileage)
# O(1) constant
packageListT1 = [13, 14, 15, 16, 19, 20]
packageListT2 = [3, 18, 36, 38]
packageListT3 = [6, 25, 28, 32, 9]

# list of packages already loaded
# O(1) constant
packagesAlreadyPlaced = ['3', '6', '13', '14', '15', '16', '18', '19', '20', '25', '28', '32', '36', '38']

# number of packages in list
# O(1) constant
packageNumberT1 = len(packageListT1)
packageNumberT2 = len(packageListT2)
packageNumberT3 = len(packageListT3)

# list of delivery deadlines to prioritize earlier times
# O(1) constant
deadlineList = []

# Self_Adjusting Algorithms  -------------------------------------------------------------------------------------------

# builds list of delivery deadlines and sorts by earliest time
# O(N log N) log-linear
def getPackageDeliveryDeadlineList():
    # list cleared to allow for multiple function calls
    deadlineList.clear()
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = str(getattr(p, 'ID'))
        pDeadline = (getattr(p, 'deadline'))
        pListObject = 'Package ID:', pID, 'Deadline:', pDeadline
        deadlineList.append(pListObject)
    sortedDeadlineList = sorted(deadlineList, key=itemgetter(3))
    return sortedDeadlineList

# Self-Adjusting Algorithm #1 - Greedy Algorithm
# setPackagesInTrucks()
# Overview: algorithm prioritizes earliest deadline times and fills up first two departing trucks (T1 and T2)
# 1) algorithm gets list of all packages sorted by earliest deadline from getPackageDeliveryDeadlineList()
# 2) algorithm places packages in first two trucks until they are full (# 14 package limit for equal distribution)
# 3) algorithm places remaining packages in truck departing latest (T3)
# 4) while placing packages, algorithm appends each package to packagesAlreadyPlaced list to prevent duplicates
    # in event that algorithm needs to be called again (if deadlines change, if total number of packages change, etc.)
# O(N^2) quadratic
def setPackagesInTrucks():
    sortedDeadlineList = getPackageDeliveryDeadlineList()
    for package in sortedDeadlineList:
        # package [1] = pID
        if package[1] not in packagesAlreadyPlaced:
            if len(packageListT1) < 14:
                packageListT1.append(int(package[1]))
                packagesAlreadyPlaced.append(package[1])
            elif len(packageListT2) < 14:
                packageListT2.append(int(package[1]))
                packagesAlreadyPlaced.append(package[1])
            else:
                packageListT3.append(int(package[1]))
                packagesAlreadyPlaced.append(package[1])
