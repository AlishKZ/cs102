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


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    (x, y, g) = bezout_recursive(phi, e)
    d = y % phi            
    return d;


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p*q
    phi = (p-1)*(q-1)
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
return ((e, n), (d, n))
