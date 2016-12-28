import random


def rsa_keygen_p():
    primes = []
    primes_in = open("primes.txt").read()
    n = primes_in.count(" ")
    for i in range(n+1):
        if i < n-1:
            prime = int(primes_in[:primes_in.find(" ")])
            primes.append(prime)
            primes_in = primes_in[primes_in.find(" ")+1:]
        else:
            prime = int(primes_in)
            primes.append(prime)
    primebool = False
    while primebool != True:
        p = random.randint(1, 1000)
        for i in range(len(primes)):
            if p == primes[i]:
                primebool = True
    return p


def rsa_keygen_q():
    primes = []
    primes_in = open("primes.txt").read()
    n = primes_in.count(" ")
    for i in range(n+1):
        if i < n-1:
            prime = int(primes_in[:primes_in.find(" ")])
            primes.append(prime)
            primes_in = primes_in[primes_in.find(" ")+1:]
        else:
            prime = int(primes_in)
            primes.append(prime)
    primebool = False
    while primebool != True:
        q = random.randint(1, 1000)
        for i in range(len(primes)):
            if q == primes[i]:
                primebool = True
    return q


def rsa_keygen_n(p,q):
    n = p*q
    return n


def rsa_keygen_eiler(p,q):
    eiler = (p-1)*(q-1)
    return eiler

def rsa_keygen_e(eiler):
    primes = []
    primes_in = open("primes.txt").read()
    n = primes_in.count(" ")
    for i in range(n + 1):
        if i < n - 1:
            prime = int(primes_in[:primes_in.find(" ")])
            primes.append(prime)
            primes_in = primes_in[primes_in.find(" ") + 1:]
        else:
            prime = int(primes_in)
            primes.append(prime)
    primebool = False
    while primebool != True:
        e = random.randint(1, eiler)
        for i in range(len(primes)):
            if e == primes[i] and (e % eiler != 0):
                primebool = True
    return e


def rsa_keygen_d(eiler,e):
    d = 1
    while True:
        if (d*e) % eiler == 1:
            break
        else:
            d += 1
    return d
