import numpy as np

def numerical_derivation(func,point):
    def calculation(point):
        h = 0.001
        output = func

        returnval = (output(point+h) + output(point-h)) / h

        return returnval
    return calculation()

@numerical_derivation(point)
def fuggveny(point):

    return point * 2

if __name__ == '__main__':
    print(fuggveny(1))