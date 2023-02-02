from Truck import *

f = open('WGUPS Distance Table.csv', 'r')
reader = csv.reader(f)
distanceDictionary = {}
for row in reader:
    distanceDictionary[row[0]] = {'Address 1': row[1], 'Address 2': row[2],
                                  'Distance to/from Western Governors University': row[3],
                                  'Distance to/from International Peace Gardens': row[4],
                                  'Distance to/from Sugar House Park': row[5],
                                  'Distance to/from Taylorsville-Bennion Heritage City Gov Off': row[6],
                                  'Distance to/from Salt Lake City Division of Health Services': row[7],
                                  'Distance to/from South Salt Lake Public Works': row[8],
                                  'Distance to/from Salt Lake City Streets and Sanitation': row[9],
                                  'Distance to/from Deker Lake': row[10],
                                  'Distance to/from Salt Lake City Ottinger Hall': row[11],
                                  'Distance to/from Columbus Library': row[12],
                                  'Distance to/from Taylorsville City Hall': row[13],
                                  'Distance to/from South Salt Lake Police': row[14],
                                  'Distance to/from Council Hall': row[15],
                                  'Distance to/from Redwood Park': row[16],
                                  'Distance to/from Salt Lake County Mental Health': row[17],
                                  'Distance to/from Salt Lake County/United Police Dept': row[18],
                                  'Distance to/from West Valley Prosecutor': row[19],
                                  'Distance to/from Housing Auth. of Salt Lake County': row[20],
                                  'Distance to/from Utah DMV Administrative Office': row[21],
                                  'Distance to/from Third District Juvenile Court': row[22],
                                  'Distance to/from Cottonwood Regional Softball Complex': row[23],
                                  'Distance to/from Holiday City Office': row[24],
                                  'Distance to/from Murray City Museum': row[25],
                                  'Distance to/from Valley Regional Softball Complex': row[26],
                                  'Distance to/from City Center of Rock Springs': row[27],
                                  'Distance to/from Rice Terrace Pavilion Park': row[28],
                                  'Distance to/from Wheeler Historic Farm': row[29]}


packageListAddressesT1 = []
packageListAddressesT2 = []
packageListAddressesT3 = []
optimalPackageListAddressesT1 = []
optimalPackageListAddressesT2 = []
optimalPackageListAddressesT3 = []


addressKeyListT1 = []
addressKeyListT2 = []
addressKeyListT3 = []
optimalAddressKeyListT1 = []
optimalAddressKeyListT2 = []
optimalAddressKeyListT3 = []


uniqueAddressKeyListT1 = []
uniqueAddressKeyListT2 = []
uniqueAddressKeyListT3 = []


distanceFloatListT1 = []
distanceFloatListT2 = []
distanceFloatListT3 = []


shortestDistanceList = []


optimalPackageListT1 = []
optimalPackageListT2 = []
optimalPackageListT3 = []


rate = 18


def setPackageListAddressesT1():
    packageListAddressesT1.clear()
    for i in range(len(packageListT1)):
        loadedPackageID = packageListT1[i]
        for j in range(len(packageHashTable.table)):
            p = packageHashTable.search(j + 1)
            pID = int((getattr(p, 'ID')))
            pAddress = (getattr(p, 'address'))
            if loadedPackageID == pID:
                packageListAddressesT1.append(pAddress)
def setPackageListAddressesT2():
    packageListAddressesT2.clear()
    for i in range(len(packageListT2)):
        loadedPackageID = packageListT2[i]
        for j in range(len(packageHashTable.table)):
            p = packageHashTable.search(j + 1)
            pID = int((getattr(p, 'ID')))
            pAddress = (getattr(p, 'address'))
            if loadedPackageID == pID:
                packageListAddressesT2.append(pAddress)
def setPackageListAddressesT3():
    packageListAddressesT3.clear()
    for i in range(len(packageListT3)):
        loadedPackageID = packageListT3[i]
        for j in range(len(packageHashTable.table)):
            p = packageHashTable.search(j + 1)
            pID = int((getattr(p, 'ID')))
            pAddress = (getattr(p, 'address'))
            if loadedPackageID == pID:
                packageListAddressesT3.append(pAddress)
def setPackageListAddressesAllTrucks():
    setPackageListAddressesT1()
    setPackageListAddressesT2()
    setPackageListAddressesT3()
def setAddressKeyListT1(addressList):
    addressKeyListT1.clear()
    for address in addressList:
        for key in distanceDictionary:
            addressToCompare = distanceDictionary.get(key, {}).get('Address 1')
            addressToCompareF = addressToCompare.lstrip()
            if addressToCompareF == address:
                addressKeyListT1.append(key)
def setAddressKeyListT2(addressList):
    addressKeyListT2.clear()
    for address in addressList:
        for key in distanceDictionary:
            addressToCompare = distanceDictionary.get(key, {}).get('Address 1')
            addressToCompareF = addressToCompare.lstrip()
            if addressToCompareF == address:
                if addressToCompareF == address:
                    addressKeyListT2.append(key)
def setAddressKeyListT3(addressList):
    addressKeyListT3.clear()
    for address in addressList:
        for key in distanceDictionary:
            addressToCompare = distanceDictionary.get(key, {}).get('Address 1')
            addressToCompareF = addressToCompare.lstrip()
            if addressToCompareF == address:
                if addressToCompareF == address:
                    addressKeyListT3.append(key)
def setAddressKeyListAllTrucks():
    setAddressKeyListT1(packageListAddressesT1)
    setAddressKeyListT2(packageListAddressesT2)
    setAddressKeyListT3(packageListAddressesT3)

def setUniqueAddressKeyListT1():
    uniqueAddressKeyListT1.clear()
    for address in addressKeyListT1:
        if address not in uniqueAddressKeyListT1:
            uniqueAddressKeyListT1.append(address)
def setUniqueAddressKeyListT2():
    uniqueAddressKeyListT2.clear()
    for address in addressKeyListT2:
        if address not in uniqueAddressKeyListT2:
            uniqueAddressKeyListT2.append(address)
def setUniqueAddressKeyListT3():
    uniqueAddressKeyListT3.clear()
    for address in addressKeyListT3:
        if address not in uniqueAddressKeyListT3:
            uniqueAddressKeyListT3.append(address)
def setUniqueAddressKeyListAllTrucks():
    setUniqueAddressKeyListT1()
    setUniqueAddressKeyListT2()
    setUniqueAddressKeyListT3()

def getDistance(startLocation, endLocation):
    convertedEndLocation = 'Distance to/from ' + endLocation
    for location in distanceDictionary:
        if location == startLocation:
            distance = distanceDictionary.get(location, {}).get(convertedEndLocation)
            if distance == '':
                return getDistanceReversed(startLocation, endLocation)
            else:
                return distance
def getDistanceReversed(startLocation, endLocation):
    convertedStartLocation = 'Distance to/from ' + startLocation
    for location in distanceDictionary:
        if location == endLocation:
            distance = distanceDictionary.get(location, {}).get(convertedStartLocation)
            return distance

def getShortestDistanceFromHubT1():
    shortestDistance = 0
    nextAddress = ''
    for address in addressKeyListT1:
        shortestDistanceList.append(float(getDistance('Western Governors University', address)))
        shortestDistance = min(shortestDistanceList)
    for address in addressKeyListT1:
        if shortestDistance == float(getDistance('Western Governors University', address)):
            nextAddress = address
    shortestDistanceList.clear()
    return nextAddress
def getShortestDistanceFromHubT2():
    shortestDistance = 0
    nextAddress = ''
    for address in addressKeyListT2:
        shortestDistanceList.append(float(getDistance('Western Governors University', address)))
        shortestDistance = min(shortestDistanceList)
    for address in addressKeyListT2:
        if shortestDistance == float(getDistance('Western Governors University', address)):
            nextAddress = address
    shortestDistanceList.clear()
    return nextAddress
def getShortestDistanceFromHubT3():
    shortestDistance = 0
    nextAddress = ''
    for address in addressKeyListT3:
        shortestDistanceList.append(float(getDistance('Western Governors University', address)))
        shortestDistance = min(shortestDistanceList)
    for address in addressKeyListT3:
        if shortestDistance == float(getDistance('Western Governors University', address)):
            nextAddress = address
    shortestDistanceList.clear()
    return nextAddress

def getNextShortestDistanceForRouteListT1(previousAddress):
    shortestDistance = 0
    nextAddress = ''
    for address in addressKeyListT1:
        if address != previousAddress and address not in optimalAddressKeyListT1:
            shortestDistanceList.append(float(getDistance(previousAddress, address)))
            shortestDistance = min(shortestDistanceList)
    for address in addressKeyListT1:
        if address != previousAddress and address not in optimalAddressKeyListT1:
            if shortestDistance == float(getDistance(previousAddress, address)):
                nextAddress = address
    shortestDistanceList.clear()
    return nextAddress
def getNextShortestDistanceForRouteListT2(previousAddress):
    shortestDistance = 0
    nextAddress = ''
    for address in addressKeyListT2:
        if address != previousAddress and address not in optimalAddressKeyListT2:
            shortestDistanceList.append(float(getDistance(previousAddress, address)))
            shortestDistance = min(shortestDistanceList)
    for address in addressKeyListT2:
        if address != previousAddress and address not in optimalAddressKeyListT2:
            if shortestDistance == float(getDistance(previousAddress, address)):
                nextAddress = address
    shortestDistanceList.clear()
    return nextAddress
def getNextShortestDistanceForRouteListT3(previousAddress):
    shortestDistance = 0
    nextAddress = ''
    for address in addressKeyListT3:
        if address != previousAddress and address not in optimalAddressKeyListT3:
            shortestDistanceList.append(float(getDistance(previousAddress, address)))
            shortestDistance = min(shortestDistanceList)
    for address in addressKeyListT3:
        if address != previousAddress and address not in optimalAddressKeyListT3:
            if shortestDistance == float(getDistance(previousAddress, address)):
                nextAddress = address
    shortestDistanceList.clear()
    return nextAddress

def loopToSetAllAddressesInOptimalRouteOrderT1():
    optimalAddressKeyListT1.clear()
    addressToAppend = ''
    for i in range(len(uniqueAddressKeyListT1)):
        firstStop = getShortestDistanceFromHubT1()
        if len(optimalAddressKeyListT1) == 0:
            optimalAddressKeyListT1.append(firstStop)
        elif len(optimalAddressKeyListT1) == 1:
            addressToAppend = getNextShortestDistanceForRouteListT1(firstStop)
            optimalAddressKeyListT1.append(addressToAppend)
        elif len(optimalAddressKeyListT1) >= 2:
            addressToAppendL = getNextShortestDistanceForRouteListT1(addressToAppend)
            optimalAddressKeyListT1.append(addressToAppendL)
            addressToAppend = addressToAppendL
    for index1, value1 in enumerate(addressKeyListT1):
        for index2, value2 in enumerate(optimalAddressKeyListT1):
            if value1 == value2:
                while addressKeyListT1.count(value1) != optimalAddressKeyListT1.count(value2):
                    optimalAddressKeyListT1.insert(index1, value1)
def loopToSetAllAddressesInOptimalRouteOrderT2():
    optimalAddressKeyListT2.clear()
    addressToAppend = ''
    for i in range(len(uniqueAddressKeyListT2)):
        firstStop = getShortestDistanceFromHubT2()
        if len(optimalAddressKeyListT2) == 0:
            optimalAddressKeyListT2.append(firstStop)
        elif len(optimalAddressKeyListT2) == 1:
            addressToAppend = getNextShortestDistanceForRouteListT2(firstStop)
            optimalAddressKeyListT2.append(addressToAppend)
        elif len(optimalAddressKeyListT2) >= 2:
            addressToAppendL = getNextShortestDistanceForRouteListT2(addressToAppend)
            optimalAddressKeyListT2.append(addressToAppendL)
            addressToAppend = addressToAppendL
    for index1, value1 in enumerate(addressKeyListT2):
        for index2, value2 in enumerate(optimalAddressKeyListT2):
            if value1 == value2:
                while addressKeyListT2.count(value1) != optimalAddressKeyListT2.count(value2):
                    optimalAddressKeyListT2.insert(index1, value1)
def loopToSetAllAddressesInOptimalRouteOrderT3():
    optimalAddressKeyListT3.clear()
    addressToAppend = ''
    for i in range(len(uniqueAddressKeyListT3)):
        firstStop = getShortestDistanceFromHubT3()
        if len(optimalAddressKeyListT3) == 0:
            optimalAddressKeyListT3.append(firstStop)
        elif len(optimalAddressKeyListT3) == 1:
            addressToAppend = getNextShortestDistanceForRouteListT3(firstStop)
            optimalAddressKeyListT3.append(addressToAppend)
        elif len(optimalAddressKeyListT3) >= 2:
            addressToAppendL = getNextShortestDistanceForRouteListT3(addressToAppend)
            optimalAddressKeyListT3.append(addressToAppendL)
            addressToAppend = addressToAppendL
    for index1, value1 in enumerate(addressKeyListT3):
        for index2, value2 in enumerate(optimalAddressKeyListT3):
            if value1 == value2:
                while addressKeyListT3.count(value1) != optimalAddressKeyListT3.count(value2):
                    optimalAddressKeyListT3.insert(index1, value1)
def setAllAddressesInOptimalRouteOrderAllTrucks():
    loopToSetAllAddressesInOptimalRouteOrderT1()
    loopToSetAllAddressesInOptimalRouteOrderT2()
    loopToSetAllAddressesInOptimalRouteOrderT3()

def setOptimalPackageListAddressesT1():
    optimalPackageListAddressesT1.clear()
    for address in optimalAddressKeyListT1:
        for key in distanceDictionary.keys():
            if key == address:
                addressToAppend = distanceDictionary.get(key, {}).get('Address 1')
                addressToAppendF = addressToAppend.lstrip()
                optimalPackageListAddressesT1.append(addressToAppendF)
def setOptimalPackageListAddressesT2():
    optimalPackageListAddressesT2.clear()
    for address in optimalAddressKeyListT2:
        for key in distanceDictionary.keys():
            if key == address:
                addressToAppend = distanceDictionary.get(key, {}).get('Address 1')
                addressToAppendF = addressToAppend.lstrip()
                optimalPackageListAddressesT2.append(addressToAppendF)
def setOptimalPackageListAddressesT3():
    optimalPackageListAddressesT3.clear()
    for address in optimalAddressKeyListT3:
        for key in distanceDictionary.keys():
            if key == address:
                addressToAppend = distanceDictionary.get(key, {}).get('Address 1')
                addressToAppendF = addressToAppend.lstrip()
                optimalPackageListAddressesT3.append(addressToAppendF)
def setOptimalPackageListAddressesAllTrucks():
    setOptimalPackageListAddressesT1()
    setOptimalPackageListAddressesT2()
    setOptimalPackageListAddressesT3()

def setOptimalPackageListT1():
    optimalPackageListT1.clear()
    for address in optimalPackageListAddressesT1:
        for package in range(len(packageHashTable.table)):
            p = packageHashTable.search(package + 1)
            pID = int((getattr(p, 'ID')))
            pAddress = (getattr(p, 'address'))
            if address == pAddress and pID in packageListT1 and pID not in optimalPackageListT1:
                optimalPackageListT1.append(pID)
    setattr(truck1, 'packageList', optimalPackageListT1)
def setOptimalPackageListT2():
    optimalPackageListT2.clear()
    for address in optimalPackageListAddressesT2:
        for package in range(len(packageHashTable.table)):
            p = packageHashTable.search(package + 1)
            pID = int((getattr(p, 'ID')))
            pAddress = (getattr(p, 'address'))
            if address == pAddress and pID in packageListT2 and pID not in optimalPackageListT2:
                optimalPackageListT2.append(pID)
    setattr(truck2, 'packageList', optimalPackageListT2)
def setOptimalPackageListT3():
    optimalPackageListT3.clear()
    for address in optimalPackageListAddressesT3:
        for package in range(len(packageHashTable.table)):
            p = packageHashTable.search(package + 1)
            pID = int((getattr(p, 'ID')))
            pAddress = (getattr(p, 'address'))
            if address == pAddress and pID in packageListT3 and pID not in optimalPackageListT3:
                optimalPackageListT3.append(pID)
    setattr(truck3, 'packageList', optimalPackageListT3)
def setOptimalPackageListAllTrucks():
    setOptimalPackageListT1()
    setOptimalPackageListT2()
    setOptimalPackageListT3()
def updateTotalMilesAndPopulateDistancesT1():
    distanceFloatListT1.clear()
    distanceListT1 = [getDistance('Western Governors University', optimalAddressKeyListT1[0])]
    for index, location in enumerate(optimalAddressKeyListT1):
        for index2, location2 in enumerate(optimalAddressKeyListT1):
            if index2 == index + 1:
                distanceListT1.append(getDistance(location, location2))
    distanceListT1.append(getDistance(optimalAddressKeyListT1[-1], 'Western Governors University'))
    for i in distanceListT1:
        distanceFloatListT1.append(round(float(i), 2))
    total = sum(distanceFloatListT1)
    roundedTotal = round(total, 2)
    return roundedTotal
def updateTotalMilesAndPopulateDistancesT2():
    distanceFloatListT2.clear()
    distanceListT2 = [getDistance('Western Governors University', optimalAddressKeyListT2[0])]
    for index, location in enumerate(optimalAddressKeyListT2):
        for index2, location2 in enumerate(optimalAddressKeyListT2):
            if index2 == index + 1:
                distanceListT2.append(getDistance(location, location2))
    distanceListT2.append(getDistance(optimalAddressKeyListT2[-1], 'Western Governors University'))
    for i in distanceListT2:
        distanceFloatListT2.append(round(float(i), 2))
    total = sum(distanceFloatListT2)
    roundedTotal = round(total, 2)
    return roundedTotal
def updateTotalMilesAndPopulateDistancesT3():
    distanceFloatListT3.clear()
    distanceListT3 = [getDistance('Western Governors University', optimalAddressKeyListT3[0])]
    for index, location in enumerate(optimalAddressKeyListT3):
        for index2, location2 in enumerate(optimalAddressKeyListT3):
            if index2 == index + 1:
                distanceListT3.append(getDistance(location, location2))
    distanceListT3.append(getDistance(optimalAddressKeyListT3[-1], 'Western Governors University'))
    for i in distanceListT3:
        distanceFloatListT3.append(round(float(i), 2))
    total = sum(distanceFloatListT3)
    roundedTotal = round(total, 2)
    return roundedTotal
def setTotalRouteMileageAllTrucks():
    mileageToSetT1 = updateTotalMilesAndPopulateDistancesT1()
    setattr(truck1, 'totalRouteMileage', mileageToSetT1)
    mileageToSetT2 = updateTotalMilesAndPopulateDistancesT2()
    setattr(truck2, 'totalRouteMileage', mileageToSetT2)
    mileageToSetT3 = updateTotalMilesAndPopulateDistancesT3()
    setattr(truck3, 'totalRouteMileage', mileageToSetT3)
def getTotalMilesAndRefreshLocationStatusT1(userInputTime):
    if userInputTime[-2:] >= '60':
        revertedIntTime = int(userInputTime)
        newIntTime = revertedIntTime + 40
        userInputTime = str(newIntTime)
    totalMileage = rate * (((int(userInputTime)) - (int(timeLeftHubT1))) / 100)
    if totalMileage < 0:
        totalMileage = 0
    if userInputTime > timeLeftHubT1:
        setattr(truck1, 'location', 'En Route')
    totalRouteMileage = getattr(truck1, 'totalRouteMileage')
    if totalMileage > totalRouteMileage:
        totalMileage = totalRouteMileage
        setattr(truck1, 'location', 'Returned To Hub')
    return float(totalMileage)
def getTotalMilesAndRefreshLocationStatusT2(userInputTime):
    if userInputTime[-2:] >= '60':
        revertedIntTime = int(userInputTime)
        newIntTime = revertedIntTime + 40
        userInputTime = str(newIntTime)
    totalMileage = rate * (((int(userInputTime)) - (int(timeLeftHubT2))) / 100)
    if totalMileage < 0:
        totalMileage = 0
    if userInputTime > timeLeftHubT2:
        setattr(truck2, 'location', 'En Route')
    totalRouteMileage = getattr(truck2, 'totalRouteMileage')
    if totalMileage > totalRouteMileage:
        # change total mileage to total of route mileage
        totalMileage = totalRouteMileage
        setattr(truck2, 'location', 'Returned To Hub')
    return float(totalMileage)
def getTotalMilesAndRefreshLocationStatusT3(userInputTime):
    if userInputTime[-2:] >= '60':
        revertedIntTime = int(userInputTime)
        newIntTime = revertedIntTime + 40
        userInputTime = str(newIntTime)
    totalMileage = rate * (((int(userInputTime)) - (int(timeLeftHubT3))) / 100)
    if totalMileage < 0:
        totalMileage = 0
    if userInputTime > timeLeftHubT3:
        setattr(truck3, 'location', 'En Route')
    totalRouteMileage = getattr(truck3, 'totalRouteMileage')
    if totalMileage > totalRouteMileage:
        # change total mileage to total of route mileage
        totalMileage = totalRouteMileage
        setattr(truck3, 'location', 'Returned To Hub')
    return float(totalMileage)

def getTotalMilesAndRefreshLocationStatusAllTrucksAndAllPackages(userInputTime):
    totalMileage1 = round(getTotalMilesAndRefreshLocationStatusT1(userInputTime), 2)
    totalMileage2 = round(getTotalMilesAndRefreshLocationStatusT2(userInputTime), 2)
    totalMileage3 = round(getTotalMilesAndRefreshLocationStatusT3(userInputTime), 2)
    totalMileageAll = totalMileage1 + totalMileage2 + totalMileage3
    totalMileageAllRounded = round(totalMileageAll, 2)
    currentTruckLocationStatusT1 = getattr(truck1, 'location')
    currentTruckLocationStatusT2 = getattr(truck2, 'location')
    currentTruckLocationStatusT3 = getattr(truck3, 'location')
    print('\nTruck Data: ')
    print('Truck 1:', 'Mileage =', totalMileage1, 'miles |', 'Location =', currentTruckLocationStatusT1)
    print('Truck 2:', 'Mileage =', totalMileage2, 'miles |', 'Location =', currentTruckLocationStatusT2)
    print('Truck 3:', 'Mileage =', totalMileage3, 'miles |', 'Location =', currentTruckLocationStatusT3)
    print('ALl Trucks: Total Mileage = ', totalMileageAllRounded, 'miles\n')
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = int((getattr(p, 'ID')))
        pDeliveryTimestampString = getattr(p, 'status')
        pDeliveryTimestampTimeUnformatted = pDeliveryTimestampString[-5:]
        pDeliveryTimestampTimeFormatted = str(pDeliveryTimestampTimeUnformatted).replace(':', '')
        if pID in optimalPackageListT1:
            if userInputTime < timeLeftHubT1:
                setattr(p, 'status', 'At the Hub')
            if timeLeftHubT1 <= userInputTime < pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'En Route')
            if userInputTime >= pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'Delivered at ' + pDeliveryTimestampTimeUnformatted)
        if pID in optimalPackageListT2:
            if userInputTime < timeLeftHubT2:
                setattr(p, 'status', 'At the Hub')
            if timeLeftHubT2 <= userInputTime < pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'En Route')
            if userInputTime >= pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'Delivered at ' + pDeliveryTimestampTimeUnformatted)
        if pID in optimalPackageListT3:
            if userInputTime < timeLeftHubT3:
                setattr(p, 'status', 'At the Hub')
            if timeLeftHubT3 <= userInputTime < pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'En Route')
            if userInputTime >= pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'Delivered at ' + pDeliveryTimestampTimeUnformatted)

def getTotalMilesAndRefreshLocationStatusAllPackages(userInputTime):
    for i in range(len(packageHashTable.table)):
        p = (packageHashTable.search(i + 1))
        pID = int((getattr(p, 'ID')))
        pDeliveryTimestampString = getattr(p, 'status')
        pDeliveryTimestampTimeUnformatted = pDeliveryTimestampString[-5:]
        pDeliveryTimestampTimeFormatted = str(pDeliveryTimestampTimeUnformatted).replace(':', '')
        if pID in packageListT1:
            if userInputTime < timeLeftHubT1:
                setattr(p, 'status', 'At the Hub')
            if timeLeftHubT1 <= userInputTime < pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'En Route')
            if userInputTime >= pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'Delivered at ' + pDeliveryTimestampTimeUnformatted)
        if pID in packageListT2:
            if userInputTime < timeLeftHubT2:
                setattr(p, 'status', 'At the Hub')
            if timeLeftHubT2 <= userInputTime < pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'En Route')
            if userInputTime >= pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'Delivered at ' + pDeliveryTimestampTimeUnformatted)
        if pID in packageListT3:
            if userInputTime < timeLeftHubT3:
                setattr(p, 'status', 'At the Hub')
            if timeLeftHubT3 <= userInputTime < pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'En Route')
            if userInputTime >= pDeliveryTimestampTimeFormatted:
                setattr(p, 'status', 'Delivered at ' + pDeliveryTimestampTimeUnformatted)

def getAllDataAtSetTime(userInputTime):
    getTotalMilesAndRefreshLocationStatusAllTrucksAndAllPackages(userInputTime)
    getPackageData()

def getAllTruckDataAtSetTime(userInputTime):
    getTotalMilesAndRefreshLocationStatusAllTrucksAndAllPackages(userInputTime)

def getAllPackageDataAtSetTime(userInputTime):
    getTotalMilesAndRefreshLocationStatusAllPackages(userInputTime)
    getPackageData()

def getSpecificPackageDataAtSetTime(userInputTime):
    getTotalMilesAndRefreshLocationStatusAllPackages(userInputTime)
    print('\nEnter Package ID (1-40):')
    userInput = int(input())
    while userInput > 40 or userInput < 1:
        print('ID must be between 1 and 40')
        userInput = int(input())
    getPackageDataByID(userInput)
