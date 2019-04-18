import csv
import sys

filename = sys.argv[1]
dictionary = sys.argv[-1]

sus = [28520,51780,175354,234164,292073,387200,387676,505444,623027,696047,701055,711648,712620,712810,712948,713020,713336,713410,713444,713468,713474,713489,713639,713701,713725,713743,713767,713814,713876,713892,713979,714016,714105,714191,714361,714853,715373,716472,716478,721312,728286,786361,857138,944354,969089,981554,1023940,1039322,1108217,1376868,1642962,1663285,1690582,1847246,1886447,1981017,2037156,2038003]
information = [[0 for x in range(21)] for y in range(59)] 
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

start = nTime[0]
splitTime = 4099328299
end = start + splitTime
n = 0
i = 0
indexOf = 0
information[0][0] = "       "
for c in range(0,len(sus)):
    information[c+1][0] = sus[c]
    if c < 21 and c != 0:
        information[0][c] = c
while i < 20:
    for x in range(0,len(nTime)):
        if nTime[x] >= long(start) and nTime[x] <= long(end):
            for y in range(0,len(sus)):
                if information[y][0] == nSourceID[x]:
                    indexOf = y
            information[indexOf][i+1] += 1
            for y in range(0,len(sus)):
                if information[y][0] == nDesinationID[x]:
                    indexOf = y
            information[indexOf][i+1] += 1

    i+=1
    start = end + 1
    if i == 19:
        end += splitTime + 2
    else:
        end += splitTime + 1

for x in range(1,len(information)):
    sys.stdout.flush()
    sys.stdout.write('var ds' + str(x) + ' = [')
    for y in range(1,20):
        if y > 0 and y < 19:
            sys.stdout.write(str(information[x][y]) + ',')
        else:
            sys.stdout.write(str(information[x][y]))
    sys.stdout.write(']\n')

with open('question3Fin.csv', mode='w') as csv_file:
    employee_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for x in range(0,len(information)):
        employee_writer.writerow(information[x])
# first time: 1432057447000
# last time:  1514044013000
# inbtw:        81986566000
# -20 /20 =      4099328299
