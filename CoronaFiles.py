import csv
def openInputFile():
    return open('CoronaData.csv','r')

def main():
    inFile = openInputFile()
    first = inFile.readline()

    #second = inFile.readline()
    #second = second.strip()
    #parts = second.split(',')
    #d = {parts[1]:parts[48]}
    d = {} 
    for line in inFile:
        line = line.strip()
        parts = line.split(',')
        if parts[1] in d:
            d[parts[1]] += int(parts[48])
        else:
            d[parts[1]]= int(parts[48])
        if line == 200:
            break
    print(d)
main()