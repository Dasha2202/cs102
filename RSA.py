import math
import random


def multiplicative_inverse(a, b):
    vector = []
    c1 = max(a, b)
    a = min(a, b)
    b = c1
    while a % b != 0:
        c = a % b
        a = b
        b = c
        vector.append((a, b))
    result = [[0, 1] for i, x in enumerate(vector)]
    for i in range(len(vector) - 2, -1, -1):
        result[i][0] = result[i + 1][1]
        result[i][1] = result[i + 1][0]
        result[i][1] -= result[i + 1][1] * (vector[i][0] // vector[i][1])
    return result[0][1] % c1


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def is_prime(n):
    if n == 1:
        return False
    numb = (math.sqrt(n))
    for i in range(2, int(numb + 3)):
        if i == n:
            break
if n % i == 0:
            return False
return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number to generate keypair : "))
    q = int(input("Enter another prime number : "))
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    statement = input("Enter a statement to encrypt with your private key: ")
    encrypted_st = encrypt(private, statement)
    print("Your encrypted statement is: ")
    print(''.join(map(lambda x: str(x), encrypted_st)))
    print("Your statement is:")
    print(decrypt(public, encrypted_st))
