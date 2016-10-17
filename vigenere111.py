ciphertext = input('Введите слово')
keyword = input('Введите слово-ключ')


def ecrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    keywordplus = keyword
    while len(ciphertext) > len(keywordplus):
        keywordplus += keyword
    for i in range(len(ciphertext)):
        ch_plain = ord(ciphertext[i])
        ch_key = ord(keywordplus[i])
        ch = 0
        if ch_key >= 65 and ch_key <= 90:
                ch = ch_key-65
                elif ch_key >= 97 and ch_key <= 122:
                    ch = ch_key-97
        if ch_plain <= 90:
            ch_plain += ch
            if ch_plain > 90:
                ch_plain -= 26
        else:
            ch_plain += ch
            if ch_plain > 122:
                ch_plain -= 26
        plaintext += chr(ch_plain)
    return plaintext
print(ecrypt_vigenere(ciphertext, keyword))


ciphertext = input('Введите слово')
keyword = input('Введите слово-ключ')


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    keywordplus = keyword
    while len(ciphertext) > len(keywordplus):
        keywordplus += keyword
    for i in range(len(ciphertext)):
        ch_plain = ord(ciphertext[i])
        ch_key = ord(keywordplus[i])
        ch = 0
        if ch_key >= 65 and ch_key <= 90:
                ch = ch_key-65
        elif ch_key >= 97 and ch_key <= 122:
                ch = ch_key-97
        if ch_plain <= 90:
            ch_plain -= ch
            if ch_plain < 65:
                ch_plain += 26
        else:
            ch_plain -= ch
            if ch_plain < 97:
                ch_plain += 26
        plaintext += chr(ch_plain)
    return plaintext
print(decrypt_vigenere(ciphertext, keyword))
