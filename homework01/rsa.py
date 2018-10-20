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
