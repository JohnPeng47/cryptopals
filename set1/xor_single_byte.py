from collections import OrderedDict, Counter
import string
hex_str = bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

xor_str = []
scores = {}

for char in string.ascii_letters:
	for i in range(len(hex_str)):
		xor_str.append(hex_str[i] ^ ord(char))
	char_str = [chr(x) for x in xor_str] #byte array so can directly convert each element to char
	points = 0
	for l in "etaoinshrdlu":
		if l in char_str:
			points += 1
	scores[points] = "".join(char_str)
	xor_str = []

for key, value in sorted(scores.items(), key = lambda x: x[0], reverse=True): #convert dict to tuples then sort according to first tuple value ie. the key
	print key, value
