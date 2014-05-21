# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. 

#This script checks if word or phrase is palindrome

def remove_char(string):
	new_str = ""
	for char in string:
		if char not in " ?.,-:;!/":
			new_str += char
		else:
			None
	return new_str.lower()

def palindrome(string):
	if string == string[::-1]:
		return True
	else:
		return False

		

print palindrome(remove_char("Hello, World"))

print palindrome(remove_char("Madam"))

print palindrome(remove_char("A man, a plan, a canal: Panama"))


