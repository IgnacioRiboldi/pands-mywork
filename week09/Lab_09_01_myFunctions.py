# My Functions
# This function should take in a number and return a list containing a Fibonacci sequence of that many numbers.
# By Ignacio Riboldi

import logging

def fibonacci(number):
    if number < 0:
        raise ValueError('number must be > 0')
    if number == 0:
        return []
    a = 0 
    b = 1
    fibonacciSequence = [0]

    for i in range(1,number):
        fibonacciSequence.append(b)
        a , b = b, a + b
    logging.debug("%d :%s", number, fibonacciSequence)


    return fibonacciSequence

if __name__ == '__main__':
    return7 = [0,1,1,2,3,5,8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    logging.debug("%s", fibonacci(7))
    assert fibonacci(7) == return7
    assert fibonacci(11) == return11
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    try:
        fibonacci(-1)
    except ValueError:

        pass
    else:
        assert False
        print("all good")