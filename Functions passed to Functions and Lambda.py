# region functions
def domath(func,z):
    """
    This function executes the callback and returns the result of the callback
    :param func: A callback function that takes one argument z
    :param z: a numerical value for the argument of the callback
    :return: the result of the callback
    """
    y=func(z) #func(z) is calculated and assigned to y
    return y  # am I returning y or the value of y?

def mathfunc1(x):
    """
    This is a defined function with the name mathfunc1 and takes one positional argument
    :param x: numerical, real value
    :return: square of argument
    """
    return  (x ** 2)  # scope of x?  What gets returned?

def main():
    """
    this main function is illustrating the use of callback functions.
    :return: nothing
    """
    def mathfunc2(z):
        """
        This function uses one argument and the variable b defined in function main.
        :param z: a real number
        :return: b*(z**3)
        """
        return b * (z ** 3)  # scope of b?  scope of z?

    a=5
    b=3
    answer=domath(mathfunc1,3.1)
    print(answer)
    answer2=domath(mathfunc2,4.8)

    print(answer2)
    answer3=domath(lambda x: a*x**3,4.8) #the lambda function takes one positional argument; format lambda arguments: expression
    print(answer3)
#endregion

main()

