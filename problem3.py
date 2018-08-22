'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
number = int(input('Enter a number: '))

for i in range(number+1,1):
    diviser = 2
    while (diviser > i) and (i % diviser != 0):
        diviser += 1

    if diviser == i:
    	if number % i == 0:
    		largest_prime_factor=i
    		print i
    		break 

print largest_prime_factor