#script to process log file of nvprof to get average time of execution of each kernel
import sys
import csv

path = sys.argv

attlines = []

filepath = path[1]+"humanred.log"

with open(filepath, "rb") as logfile:
    attlines = logfile.readlines()

for i in xrange(len(attlines)):
    attlines[i] = attlines[i].split()


datToRead = []
flag = 0



for i in xrange(len(attlines)):

    if flag == 1 :
        if '[CUDA' in attlines[i]:
            continue
        else:
            datToRead.append(attlines[i])
    if attlines[i]==[]:
        break
    if 'Time(%)' in attlines[i]:
        flag = 1
        continue

datToRead.remove([])
datToWrite=[]
for i in xrange(len(datToRead)):
    datToWrite.append([path[1][20:], ''.join(datToRead[i][6:]).replace(",", ""), float(datToRead[i][3][-3::-1][::-1])])

with open("actual.csv", "a") as actualfile:
    datawriter = csv.writer(actualfile)
    for data in datToWrite:
        datawriter.writerow(data)
