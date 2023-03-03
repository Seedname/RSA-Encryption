import math
import random

def stringToInt(string):
    integer = ""
    for char in string:
        integer += str(ord(char)).zfill(3)
    return int(integer)
    # binary = ""
    # for char in string:
    #     binary += bin(ord(char))[2:].zfill(8)
    # return int(binary, 2)
def intToString(num):
    plaintext = ""
    
    string = str(num)
    length = len(string)
    string = string.zfill(length + 3 - length % 3)
    codes = [string[i:i+3] for i in range(0, len(string), 3)]

    for code in codes:
        plaintext += chr(int(code))
    return plaintext

string = "asdfasdfasdfsfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf"
integer = stringToInt(string)
# print(integer)
# print(intToString(integer))

# Testing if it's prime with probabilites
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

# Bad version of prime number checking
# def isPrime(n):
#     if n > 1:
#         for i in range(2, int(math.sqrt(n))):
#             if n % i == 0: return False
#         return True
#     return False

# Just generates a range of primes
# def primeRange(n, m, max):
#     primes = []
#     for i in range(n, m):
#         if isPrime(i): primes.append(i)
#         if len(primes) > max: break
#     return primes

# calculates inverse multiplicative modulus if it's coprime
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

# much faster method to produce modulo exponentiation
def exp(a, m, n):
    result = 1
    for i in bin(m)[2:]:
        result = (result * result) % n
        if i == '1':
            result = (result * a) % n
    return result

# generates a random integer depending on how many digits you use
def randomNum(digits):
    num = str(random.randint(1, 9))
    for i in range(digits-1):
        num += str(random.randint(0, 9))
    return int(num)

digits = max(3, int(math.log10(integer)))

p = 0
q = 0

# generate random prime number p
while True:
    p1 = randomNum(digits)
    if isPrime(p1):
        p = p1
        break

# generate random prime number q
while True:
    q1 = randomNum(digits)
    if isPrime(q1):
        q = q1
        break

n = p * q
totient = (p-1) * (q-1)

e = (2 << 15) + 1

if e > n:
    while True:
        num = randomNum(digits-1)
        if isPrime(num): 
            e = num
            break

d = modInverse(e, totient)

public = (n, e)
private = (n, d)

C = exp(integer, e, n)
M = exp(C, d, n)

# next steps:
# add two clients with different public and private keys
# encrypt the message with my private and the other person's public key
# they decrypt the message with their private and my public key

print("Encrypted: " + intToString(C))
print("Decrypted: " + intToString(M))

