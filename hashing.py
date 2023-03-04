def md5(string):
    binary = ""
    for letter in string: binary += bin(ord(letter))[2:]
    length = len(binary)
    if length % 512 != 0: binary += "1"
    n = ((len(binary)-1) | 15)+1
    binary = binary.ljust(n, '0')
    blocks = [binary[i:i+16] for i in range(0, len(binary), 16)]

    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476

    print(blocks)

md5("this is a test")