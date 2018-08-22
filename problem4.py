'''
myinteger=raw_input('Enter the number: ')
first_three_digits = myinteger[:3] # first two digits
last_three_digits = myinteger[-3:] # last three digits

if first_three_digits == last_three_digits[::-1]:
	print ('This is a palindrome number')
else:
	print ('This is a NOT palindrome number')
'''
# Last three number vs First Three Number Palindrome

myinteger=raw_input('Enter the number: ')
if myinteger[:3] == (myinteger[-3:])[::-1]:
	print ('This is a palindrome number')
else:
	print ('This is a NOT palindrome number')
