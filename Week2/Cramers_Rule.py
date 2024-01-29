# R D Delahoussaye

# Solution of a set of equations using Cramer's Rule, 
# Suported by Determinants using the Rule of Minors
#
# Used to teach RECURSION

import numpy as np

from copy import deepcopy

def Submatrix(A, thisrow, thiscol):
    nrow = len(A)
    ncol = len(A[0])
    submat = np.zeros((nrow-1, ncol - 1))  # the SubMatrix matrix is reduced in size by 1
    for submatrow in range(nrow - 1):  # loop over all rows of cf
        if submatrow < thisrow:  # copy from the same row of A
            Arow = submatrow  # copy from the same row of A
        else:
            Arow = submatrow + 1  # copy from one row ahead in A
        # endif
        for submatcol in range(ncol - 1):  # loop over all columns of cf
            if submatcol < thiscol:
                Acol = submatcol  # copy from the same column of A
            else:
                Acol = submatcol + 1  # copy from one column ahead in A
            # endif
            submat[submatrow][submatcol] = A[Arow][Acol]  # copy the correct value from A to cf
        # next j
    # next i

    return submat

def SubmatrixV2(A,thisrow, thiscol):
    b=np.delete(A,thisrow,(0))
    b=np.delete(b,thiscol,(1))
    return b

def Determinant(A):  # using the Rule of Minors
    # Note:  this function is RECURSIVE!!!!!
    n = len(A)
    if n == 1:  # then the determinant is EASY!
        return A[0][0]
    sum = 0
    for col in range(n):  # for every column in A
        cf = SubmatrixV2(A, 0, col)  # get the SubMatrix matrix for that column
        M = Determinant(cf)  # here is where it is recursive!!!
        sign = (-1) ** col  # the sign alternates
        sum = sum + A[0][col] * sign * M  # add the terms for each column
    return sum

def Cramer(A, b):
    n = len(A)
    x = np.zeros(n)
    Astar = np.zeros((n, n))  # used as the Modified A matrix for each col
    detA = Determinant(A)
    for thiscol in range(n):  # generate Astar for each col
        # by making a copy of A, with column "thiscol" replaced by "b"
        for row in range(n):  # the row of the term to copy
            for col in range(n):  # the column of the term to copy
                if col == thiscol:  # then we copy from "b"
                    Astar[row][col] = b[row]
                else:  # otherwise we copy from "A"
                    Astar[row][col] = A[row][col]
                    # endif
            # next col
        # next row
        detAstar = Determinant(Astar)  # get the determinant of Astar
        x[thiscol] = detAstar / detA  # the essence of Cramer's Rule
    # next thiscol
    return x

def main():
    A = np.array([[1, -2, 3, 4], [5, 6, 7, 8], [-9, 10, -11, 6], [5, 4, -3, 2]])
    b = np.array([1, 2, 3, 4])

    print(Submatrix(A, 1, 2))
    print("\n", Determinant(A))
    print("\n", Cramer(A, b))

    A = np.array([[-5, 1, -5, 0, 1, -4], [5, 0, 3, 5, 3, 5], [-2, -2, 1, 4, 3, -5],
                  [4, 5, 0, 3, 4, -1], [-5, -2, -5, 5, -2, -2], [4, 5, 5, 0, 0, -2]])
    b = np.array([-95, -45, 49, -50, 90, 30])

    print("\n", Submatrix(A, 1, 2))
    print("\n", Determinant(A))
    print("\n", Cramer(A, b))

    print('\n',np.linalg.solve(A,b))

main()
