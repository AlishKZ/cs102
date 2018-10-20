import random


def is_prime(n):
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    determinator = 2;
    count = 0;
    while determinator < n:
        if n%determinator == 0:
            return False;
        determinator+=1;
    return True;


def gcd(a, b):
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return(a + b)

def bezout_recursive(a, b):
    '''A recursive implementation of extended Euclidean algorithm.
    Returns integer x, y and gcd(a, b) for Bezout equation:
        ax + by = gcd(a, b).
    '''
    if not b:
        return (1, 0, a)
    y, x, g = bezout_recursive(b, a%b)
return (x, y - (a // b) * x, g)
