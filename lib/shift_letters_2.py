# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, n):
	new_str = ""
	for e in string:
		if e == " ":
			new_str += e
		elif (ord(e)+n) < 97:
			new_str += chr(ord(e)+n+26)
		elif (ord(e)+n) > 122:
			new_str += chr(ord(e)+n-26)
		else:
			new_str += chr(ord(e)+n)
	return new_str

print rotate ('sarah', 13)

print rotate('fnenu',13)

print rotate('dave',5)

print rotate('ifaj',-5)

print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)


