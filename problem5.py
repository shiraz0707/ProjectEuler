'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any 
remainder. What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?
'''
'''
divisable = "true"
number = 1
while divisable == "true":
	for i in range (1,10): 
		if number % i == 0:
			print number
		else:
			divisable = "false"
			
	if divisable == "false":
		number = number + 1
		print number
		divisable = "true"
'''

candidate = 10
found = "false"

while found == "false":
	divisable=2
	while divisable<=10 and candidate % divisable == 0:
		divisable = divisable + 1
	if divisable>10:
		found="true"
		print candidate
	else:
		candidate = candidate + 1


		
