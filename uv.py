import sys
import math

inp = sys.argv[1]
n = int(sys.argv[2])
m = int(sys.argv[3])
f = int(sys.argv[4])
b = int(sys.argv[5])

inputFile = open(inp,"r")
line = inputFile.readline()
count = 0


M = [[-1 for x in range(m)] for y in range(n)]

while line:
    line = line.strip().split(',')
    M[int(line[0])-1][int(line[1])-1] = int(line[2])
    line = inputFile.readline()
    count += 1

U = [[1 for x in range(f)] for y in range(n)]
V = [[1 for x in range(m)] for y in range(f)]

for a in xrange(0,b):
    #print a

    for i in range(0,len(U)):
        for j in range(0, len(U[0])):
            U[i][j] = 0
            mRow = M[i]
            denList = V[j]
            #numList =

            result = [0 for x in range(len(mRow))]
            for l in range(len(V[0])):
                for k in range(len(V)):
                    result[l] += U[i][k] * V[k][l]

            numerator = 0
            denominator = 0
            for m in xrange(0, len(mRow)):
                if mRow[m] == -1:
                    continue
                else:
                    numerator += (mRow[m] - result[m])*denList[m]
                    denominator += denList[m]*denList[m]
            if denominator==0:
                x=0
            else:
                x = float(numerator) / float(denominator)
            U[i][j] = x
    #print U

    for i in range(0,len(V[0])):
        for j in range(0, len(V)):
            V[j][i] = 0
            mCol = [M[x][i] for x in range(len(M))]
            denList = [U[x][j] for x in range(len(U))]

            result = [0 for x in range(len(mCol))]
            for l in range(len(U)):
                for k in range(len(V)):
                    result[l] += U[l][k] * V[k][i]

            numerator = 0
            denominator = 0
            for m in xrange(0, len(mCol)):
                if mCol[m] == -1:
                    continue
                else:
                    numerator += (mCol[m] - result[m]) * denList[m]
                    denominator += denList[m] * denList[m]

            if denominator==0:
                y=0
            else:
                y = float(numerator) / float(denominator)
            #print denominator

            V[j][i] = y
    #print V

    result = [[0 for x in range(len(V[0]))] for y in range(len(U))]

    for i in range(len(U)):
       for j in range(len(V[0])):
           for k in range(len(V)):
               result[i][j] += U[i][k] * V[k][j]

    sum = 0
    for i in xrange(len(result)):
        for j in range(len(result[0])):
            if M[i][j]==-1:
                continue
            else:
                sum += math.pow(M[i][j]-result[i][j],2)

    print "%.4f"%math.sqrt(float(sum)/count)
