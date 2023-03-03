import random
# 1024-bit RSA Encryption

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
        q = A // M
        t = M
        M = A % M
        A = t
        t = y
        y = x - q * y
        x = t

    if (x < 0):
        x = x + m0
 
    return x
def isPrime(n, k=5):
    if n < 2:
        return False
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1
        d //= 2
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
    def __init__(self, digits):
        self.p = 0
        self.q = 0

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
    
digitsForN = 154
alice = Person(digitsForN)
bob = Person(digitsForN)
eve = Person(digitsForN)

message = "encrypted message"

if (len(message) > int(2*digitsForN/3)):
    print("Message too long, will not encrypt properly\n")

encrypted = alice.encrypt(message, bob.public)
intercepted = eve.decrypt(encrypted)
decrypted = bob.decrypt(encrypted)

print("Encrypted Message: " + intToString(encrypted))
print("Intercepted Message: " + intercepted)
print("Decrypted Message: " + decrypted)
