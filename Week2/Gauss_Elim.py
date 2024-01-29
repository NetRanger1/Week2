# region imports
import copy as CP
# endregion

# region functions
def FirstNonZero_Index(R):
    """
    Finds pivot for a row (i.e., first non-zero number in a row reading from left to right)
    :param R: a row vector
    :return: the index of the first non-zero number
    """
    m=-1
    for n in range(len(R)):
        if R[n] != 0.0:
            return n
    return m  #if the whole row is zeros, returns -1

# the elementary operations for Gauss elimination are
# 1. Swap the positions of two rows (I'll use pop and insert)
# 2. Multiply a row by a non-zero scalar
# 3. Add to one row, a scalar multiple of another row

def SwapRows(A, r1, r2):  #if I do this, it is known as a partial pivot
    '''
    One of the elementary row operations in Gaussian elimination.
    :param A: A matrix
    :param r1: index of row 1
    :param r2: index of row 2
    :return: The A matrix after the row swap is done.
    '''
    rmax=max(r1,r2) #the larger index
    rmin=min(r1,r2) #the smaller index
    RMax=A[rmax]  #temporarily store the row vector at rmax in a variable
    RMin=A.pop(rmin) #pop function removes this row from the matrix and shifts all larger indices by -1
    A.insert(rmin,RMax) #insert the row RMax at the location rmin.  All higher index rows increase index by +1
    A[rmax]=RMin  #now, replace row rmax with RMin
    return A  #done

def MultRow(R,s=1):
    '''
    used to multiply a row vector by a scalar value
    :param R: the row vector
    :param s: the scalar with default value = 1
    :return: a new row vector multiplied by the scalar (s*R)
    '''
    for i in range(len(R)):
        R[i] *= s  # short way to do R[i] = R[i]*s
    return R

def AddRows(R1, R2, s=1.0):
    '''
    Adds a scalar multiple of row vector R2 to row vector R1.
    R2 and R1 must be the same length
    :param R1: a row vector
    :param R2: another row vector
    :param s: a scalar
    :return: a new row vector (R1+s*R2)
    '''
    RNew=CP.deepcopy(R1)
    for i in range(len(R1)):
        RNew[i] += R2[i]*s
    return RNew
    #use a list comprehension to build the return list
    #https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    #zip function: Make an iterator that aggregates elements from each of the iterables.
    #https://docs.python.org/3.3/library/functions.html#zip
    #return [round(i+s*j,4) for i, j in zip(R1, R2)]

#the Echelon form of a matrix is when I produce an upper triangular matrix by Gaussian elimination
def EchelonForm(A):
    '''
    I'm expecting a Matrix of m rows by n columns.
    This function performs row operations (Gauss elimination) to produce echelon form matrix.
    :param Matrix: the matrix
    :return: the echelon form of the matrix
    '''
    m=len(A) #number of rows of A
    n=len(A[0])  #number of columns of A
    Ech = CP.deepcopy(A) #make a deep copy of A so that I don't actually change A

    #order the rows by first non-zero in each column
    for i in range(m):  #iterate through all rows
        for r in range(i,m):  #iterate through all rows below row i
            p=FirstNonZero_Index(Ech[r]) #find column index in row r that is non-zero
            if p==i:  #found a row with non-zero in ith position
                Ech = SwapRows(Ech, r,i) #move this row to the ith row
                break #stops iterating through rows below i since I found a suitable row to put in position i
        if(Ech[i][i] != 0.0): #if I found a non-zero value for the [i][i] pivot
            for r in range(i+1,m):  #now add multiples of row i to rows i+1 to m in order to make column i values zero below row i
                p=FirstNonZero_Index(Ech[r])
                if p==i:  #found row p has a nonzero element in column i
                    Row=Ech[r]
                    s=-Ech[r][p]/Ech[i][i]
                    Ech[r] = AddRows(Row,Ech[i],s)
    return Ech

#the reduced echelon form of a matrix is when the numbers along the diagonal are all 1's and rows above all other
#numbers in the column are zero
def ReducedEchelonForm(A):
    """
    This functions first creates an echelon form matrix from A and then calculates a reduced echelon form of A
    by subsequent row operations.
    :param A: The matrix to work on
    :return: The reduced echelon form of the matrix A
    """
    REF=EchelonForm(A) #first reduce to echelon form
    for i in range(len(A)-1,-1,-1): #iterate from last row to row 0
        R=REF[i]
        j=FirstNonZero_Index(R) #find the first non-zero column in r
        R=MultRow(R,1.0/R[j]) #make jth value equal to 1.0
        REF[i]=R
        for ii in range(i-1,-1,-1): #remember, end index in range is non-inclusive
            RR=REF[ii]
            if(RR[j]!=0):
                RR = AddRows(RR,R,-RR[j])
                REF[ii]=RR
    return REF

#produce and identity matrix of the same size as A
def IDMatrix(A):
    '''
    Create and return an identity matrix of same dimensions as A
    :param A:
    :return:
    '''
    m=len(A) #number of rows
    n=len(A[0]) #number of cols
    IM=[]
    for i in range(m):
        IM.append([1 if j==i else 0 for j in range(n)])
    return IM

#produce an augmented matrix from A and B
def AugmentMatrix(A,B):
    '''
    Create an augmented matrix from two matrices
    :param A: a matrix
    :param B: another matrix
    :return:
    '''
    C=CP.deepcopy(A)
    for i in range(len(C)):
        C[i] += B[i]  #this is called concatonating a list
    return C

#remove the jth column from matrix A
def RemoveColumn(A,j):
    '''
    I want to remove column j from matrix A.  I'm using slicing to cut out the column j
    :param A: The matrix
    :param j: Index of the column I want to remove
    :return:  The matrix with column j removed
    '''
    B=[]
    for r in A: #iterate through rows of A
        B.append(r[:j]+r[j+1:])
    return B

#uses the matrix A augmented with the identity matrix and Gaussian elimination
def InvertMatrix(A):
    """
    Finds the inverse of matrix A by forming the augment matrix AI and using Gauss elimination
    to move the identity matrix to the left yielding IAinv, where Ainv is the inverse matrix
    :param A:  the matrix to invert
    :return:  the inverted matrix
    """
    ID = IDMatrix(A)
    Ainv = AugmentMatrix(A, ID)
    IAinv = ReducedEchelonForm(Ainv)
    for j in range(len(ID[0])-1, -1, -1):
        IAinv = RemoveColumn(IAinv, j)
    return IAinv

#use this to multiply matrices of correct dimensions
def MatrixMultiply(A,B):
    '''
    For multiplication of matrices, I need mXn * nXp to give a mXp matrix.
    So, must first check number of cols of A equals number of rows of B.
    Then, do matrix multiplication.
    :param A: A mxn matrix
    :param B: A nxp matrix
    :return: A matrix of shape mxp
    '''
    m=len(A)
    n=len(A[0])
    nn=len(B)
    p=len(B[0])
    SizeOk = n == nn
    if not SizeOk:
        return A
    C=[0]*m
    for i in range(p):
        C[i] = [0]*p
    #below is a shorter notation for building a list called a list comrehension
    #C=[[0 for j in range(p)] for m in range(m)] #build an initial array full of zeros of size ARowsXBCols

    for i in range(len(C)):  # i is my row counting variable in C
        for j in range(len(C[i])):  # j is my column counting variable in C
            for k in range(len(A[i])): #multiply row i from A with column j from B
                C[i][j] +=A[i][k]*B[k][j]
            C[i][j] = round(C[i][j], 3)
    return C

def main():
    #assuming [A][x]=[b] and augmented matrix is [M]=[A|b]
    #M=[[0,5,0,3,2],[0,0,2,4,3],[0,2,0,0,4],[1,0,0,7,5]]
    M=[[4, -1, -1, 3], [-2, -3, 1, 9], [-1, 1, 7, -6]]
    print("Original matrix:")
    for r in M:
        print(r)

    E = EchelonForm(M)  # just puts M in echelon form
    print("Echelon form:")
    for r in E:
        print(r)

    RREF = ReducedEchelonForm(M)  # puts M in reduced echelon form
    print("Reduced Echelon Form")
    for r in RREF:
        print(r)

    #for solving [A][x]=[b]
    A=RemoveColumn(M,len(M[0])-1) #remove last column of augmented matrix M

    MI=InvertMatrix(A)

    print("Inverted Matrix")
    for r in MI:
        print(r)

    B=MatrixMultiply(A,MI)

    print("A^-1*A")
    for r in B:
        print(r)
# endregion

if __name__ == "__main__":
    main()






