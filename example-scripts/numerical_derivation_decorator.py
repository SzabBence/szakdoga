import numpy as np

def numerical_derivation(func):
    def calculation(point):
        h = 0.001
        return (func(point+h) - func(point-h)) / h
    return calculation

@numerical_derivation
def fuggveny(point):

    return point * 2

if __name__ == '__main__':
    print(fuggveny(1))