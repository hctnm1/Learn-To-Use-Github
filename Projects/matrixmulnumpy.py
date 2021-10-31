import numpy
def inp():#For input of matrix
    r,c=list(map(int,input("Enter number of rows and columns(separated by a space): ").split()))
    entries = list(map(int, input("Enter the entries in a single line (separated by space): ").split())) 
    matrix= numpy.array(entries).reshape(r,c) #Creates matrix
    return matrix

def disp(a):#To display matrix
    for i in a:
        print(*i,sep="\t")
    print()
    
matrix1=inp()#Creaates matrix 1
matrix2=inp()#Creates matrix 2
print("Matrix1=")
disp(matrix1)
print("Matrix2=") 
disp(matrix2)
try:#For multiplication
    print("Result:")
    matrix3=numpy.dot(matrix1,matrix2)#Matrix multiplication using numpy
    disp(matrix3)
except:#If matrices are not multiplicable
    print("Matrices cannot be multiplied")
