import math   

for a in range(1,501):
	for b in range(1,501):
		c = a**2 + b**2 
		c = math.sqrt(c)

		split_num = str(c).split('.')
		int(split_num[1])

		if int(split_num[1])==0 and a+b+c == 1000 and a<b<c:
			print ('a=' + str(a))
			print ('b=' + str(b))
			print ('c=' + str(c))
			print (a * b * c)
	
	
