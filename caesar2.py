plaintext = input('Введите слово')


def encrypt_caesar(plaintext):
    ciphertext = ''
for i in range(len(plaintext)):
        ch = ord(plaintext[i])
if ch <= 122 and ch >= 120 or ch <= 90 and ch >= 88:
    ch -= 23
else:
    ch += 3
    ciphertext += chr(ch)
    return ciphertext
print(encrypt_caesar(plaintext))
