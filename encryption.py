import math
import random

def stringToInt(string):
    integer = ""
    for char in string:
        integer += str(ord(char)).zfill(3)
    return int(integer)
def intToString(num):
    plaintext = ""
    
    string = str(num)
    length = len(string)
    string = string.zfill(length + 3 - length % 3)
    codes = [string[i:i+3] for i in range(0, len(string), 3)]

    for code in codes:
        plaintext += chr(int(code))
    return plaintext
def modInverse(A, M):
    m0 = M
    y = 0
    x = 1
 
    if (M == 1):
        return 0
 
    while (A > 1):
 
        # q is quotient
        q = A // M
 
        t = M
 
        # m is remainder now, process
        # same as Euclid's algo
        M = A % M
        A = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x
def isPrime(n, k=5):
    if n < 2:
        return False
    # Write n-1 as 2^r * d
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Test primality with k random values of a
    for i in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for j in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True
def exp(a, m, n):
    result = 1
    for i in bin(m)[2:]:
        result = (result * result) % n
        if i == '1':
            result = (result * a) % n
    return result
def randomNum(digits):
    num = str(random.randint(1, 9))
    for i in range(digits-1):
        num += str(random.randint(0, 9))
    return int(num)


class Person:
    def __init__(self):
        self.p = 0
        self.q = 0
        digits = 12

        while True:
            p1 = randomNum(digits)
            if isPrime(p1):
                self.p = p1
                break
        while True:
            q1 = randomNum(digits)
            if isPrime(q1):
                self.q = q1
                break

        self.n = self.p * self.q
        self.totient = (self.p-1) * (self.q-1)

        self.e = (1 << 16) + 1

        if self.e > self.n:
            while True:
                num = randomNum(digits-1)
                if isPrime(num):
                    self.e = num
                    break

        self.d = modInverse(self.e, self.totient)

        self.public = (self.e, self.n)
        self.private = (self.d, self.n)

    def encrypt (self, message, public):
        integer = stringToInt(message)
        C = exp(integer, public[0], public[1])
        return C

    def decrypt (self, message):
        M = exp(message, self.private[0], self.private[1])
        return intToString(M)
    
alice = Person()
bob = Person()

encrypted = alice.encrypt("Hello", bob.public)
eve = Person()
intercepted = eve.decrypt(encrypted)
decrypted = bob.decrypt(encrypted)

print("Intercepted Message: " + intercepted)
print("Decrypted Message: " + decrypted)
