ciphertext = input('Введите слово')
def encrypt_caesar(ciphertext):
	plaintext=''
	for i in range(len(ciphertext)):
		ch=ord(ciphertext[i])
		if ch<=99 and ch>=97 or ch<=67 and ch>=65:
			ch+=23
		else:
			ch-=3
		plaintext+=chr(ch)
	return plaintext
print(encrypt_caesar(ciphertext))
	
