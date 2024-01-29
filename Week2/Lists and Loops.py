# region functions
def printlist(mylist):
    """
    Print the elements of mylist with each on a new line.
    :param mylist:
    :return: none
    """
    for val in mylist:
        print(val)
    return

def pl2(alist):
    """
    Prints a blank line and then length of alist.
    Then, prints the elements of alist each on a new line.
    :param alist:
    :return: none
    """
    print("\n",len(alist)," length of alist \n")
    for i in range(len(alist)):
        print(alist[i])

def printmat(mymat):
    """
    This function prints out the rows of a matrix where each element of each row is printed on a new line.
    :param mymat:
    :return: none
    """
    print("\n\nprinting mymat")
    for row in range(len(mymat)):
        print("row ", row)
        for col in range(len(mymat[row])):
            print(mymat[row][col])

def arraysum(thelist):
    """
    This function sums the elements of a list.
    :param thelist:
    :return: the sum of the elements in thelist
    """
    sum=0
    for num in thelist:
        #sum=sum+num
        sum += num
    return sum

def matrixsum(thematrix):
    """
    This function sums all the values in a matrix.
    :param thematrix:
    :return: the sum of thematrix
    """
    sum=0
    for rowvals in thematrix:
        for colval in rowvals:
            sum += colval
        #next colval
    #next rowvals
    return sum

def superbowl():
    """
    This was my prediction for the NFC and AFC championship games of 2021
    :return: none
    """
    NFC={'Packers':26, 'Bucs':31, 'Brady':'GOAT'}
    AFC={'Bills':24, 'Chiefs':38, 'Mahomes':'young enough to be Bradys son'}
    print('NFC Championship: Bucs {} to Packers {}. Brady is {}'.format(NFC['Bucs'],NFC['Packers'], NFC['Brady']))
    print('AFC Championship: Chiefs {} to Bills {}. Mahomes is {}'.format(AFC['Chiefs'], AFC['Bills'], AFC['Mahomes']))

def main():
    """
    This function is for teaching concepts of lists, functions and printing
    :return: nothing
    """
    ralph=[1,3,5,2,4,9,3,5,-2,11.7]  # the list named ralph (scope: local to main)
    gerald=[[1,2,3,4],[5,6,7],[5,6,7,8],[5,6,7,8],[4,3,2,1]]  # a matrix (list of lists) called gerald (scope:  local to main)
    #note row 1 only has 3 terms
    printlist(ralph)  # see function printlist
    pl2(ralph)
    print("\n",ralph)
    printmat(gerald)
    #a=arraysum(ralph)
    cc=matrixsum(gerald)

    print("matrixsum(gerald)={}".format(cc))

    superbowl()
# endregion

if __name__ == "__main__":
    main()





