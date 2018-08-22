'''
Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
'''
# Find the sum of the squares of the first hundred natural numbers

sum_of_squares = 0
for i in range (1,101): 
	sum_of_squares=sum_of_squares + (i**2)
# Find the square of the sum of the first hundred natural numbers

square_of_sums=0
sum = 0
for i in range (1,1001): 
	sum=sum + i
	square_of_sums= sum ** 2

print (square_of_sums - sum_of_squares)