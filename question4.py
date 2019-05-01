import csv
import datetime
import sys

filename = sys.argv[1]
dictionary = sys.argv[-1]

commTypeName = [1172172,437025,981745,160091,758683,447025,1371959,713743,732897,369655]
information = [[0 for x in range(11)] for y in range(11)] 
sourceID = []
commType = []
desinationID = []
time = []
clean = []
nSourceID = []
nCommType = []
nDesinationID = []
nTime = []
name = []
EmployeeIDs = []

with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row1 = int(row[0])
        row2 = int(row[1])
        row3 = int(row[2])
        row4 = int(row[3])

        sourceID.append(row1)
        commType.append(row2)
        desinationID.append(row3)
        time.append(row4)

with open(dictionary) as dic:
    readCSV = csv.reader(dic, delimiter=',')
    for row in readCSV:
        fullName = row[0] + " " + row[1]
        IDOP = row[2]

        name.append(fullName)
        EmployeeIDs.append(IDOP)

for x in range(0,len(time)):
    if time[x-1] == time[x] and sourceID[x-1] == sourceID[x] and desinationID[x-1] == desinationID[x] and commType[x-1] == commType[x]:
    #if nSourceID[y] == sourceID[x] and nCommType[y] == commType[x] and nDesinationID[y] == desinationID[x] and nTime[y] == time[x]:
        value = 0;
    else:
        nSourceID.append(sourceID[x])
        nCommType.append(commType[x])
        nDesinationID.append(desinationID[x])
        nTime.append(time[x])

for x in range(0,len(commTypeName)):
    information[x+1][0] = commTypeName[x]
    information[0][x+1] = commTypeName[x]

indeX = 0;
indeY = 0;
counter = 0;
for x in range(0,len(nTime)):
    source = nSourceID[x]
    dest = nDesinationID[x]
    if source in commTypeName and dest in commTypeName:
        if dest in commTypeName:
            indeX = commTypeName.index(dest) + 1
        if source in commTypeName:
            indeY = commTypeName.index(source) + 1
        information[indeX][indeY] += 1
        information[indeY][indeX] += 1    
    counter += 1

empName = "";
empIndex = 0;
empIndexIndex = 0;
for x in range(0,len(commTypeName)):
    empIndex = commTypeName[x]
    if str(empIndex) in EmployeeIDs:
        empIndexIndex = EmployeeIDs.index(str(empIndex))
        empName = name[empIndexIndex]
    information[x+1][0] = empName
    information[0][x+1] = empName
    commTypeName[x] = empName

buffr = 1
for x in range(1, len(information)):
    sys.stdout.flush()
    for y in range(1,buffr):
        if y == buffr - 1:
            sys.stdout.write(str(information[x][y]))
        else:
            sys.stdout.write(str(information[x][y]) + ',')
    buffr += 1
    sys.stdout.write('\n')

for x in range(0,len(commTypeName)):
    sys.stdout.flush()
    sys.stdout.write('[')
    for y in range(0,len(commTypeName)):
        sys.stdout.write(str(information[x][y]) + ",")
    sys.stdout.write(']\n')

lastIndeX = 0;
lastIndeY = 0;
buffr = 1
for x in range(1, len(information)):
    for y in range(1,buffr):
        if information[x][y] != 0:
            lastIndeX = x;
            lastIndeY = y;
    buffr += 1

sys.stdout.write('{ "nodes": [\n')
for x in range(0,len(commTypeName)):
    sys.stdout.flush()
    if x == len(commTypeName) - 1:
        sys.stdout.write('    { "id": ' + str(x + 1) + ', "name": "' + str(commTypeName[x]) + '" }\n')
    else:
        sys.stdout.write('    { "id": ' + str(x + 1) + ', "name": "' + str(commTypeName[x]) + '" },\n')
sys.stdout.write('  ],\n')
sys.stdout.write('  "links": [\n')
buffr = 1
for x in range(1, len(information)):
    sys.stdout.flush()
    for y in range(1,buffr):
        if information[x][y] != 0:
            sender = commTypeName.index(information[x][0]) + 1
            reciever = commTypeName.index(information[0][y]) + 1
            if x == lastIndeX and y == lastIndeY:
                sys.stdout.write('    { "source": ' + str(sender) + ', "target": ' + str(reciever) + ', "weight": ' + str(information[x][y]) + ' }\n')
            else:
               sys.stdout.write('    { "source": ' + str(sender) + ', "target": ' + str(reciever) + ', "weight": ' + str(information[x][y]) + ' },\n')   
    buffr += 1
sys.stdout.write('  ]\n')
sys.stdout.write('}\n')

# first time: 1432057447000
# last time:  1514044013000
# inbtw:        81986566000
# -20 /20 =      4099328299
