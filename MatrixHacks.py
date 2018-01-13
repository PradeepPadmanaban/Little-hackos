import random

def MatrixCreator(m,n):
    a = []
    for i in range(0,m):
        b=[]
        for j in range(0,n):
            b.append(random.randint(0,100))
        a.append(b)
    return a

def MatrixWriter(a,FileName="OutputFile.txt"):
    m = len(a)
    n = len(a[0])
    outputFile = open(FileName,"w")
    outputFile.write(str(m)+" "+str(n)+"\n")
    for i in range(0,m):
        for j in range(0,n):
            outputFile.write(str(a[i][j])+" ")
        outputFile.write("\n")
    outputFile.close()
    
def MatrixReader(FileName="OutputFile.txt"):
    InputFile = open(FileName,"r")
    m,n = InputFile.readline().split()
    a=[]
    for i in range(0,int(m)):
        a.append(InputFile.readline().split())
    InputFile.close()
    return a

MatrixWriter(MatrixCreator(7,8))
print(MatrixReader())
