import math   # This will import math module

a = 200
b = 375

c = a**2 + b**2 
print c

c = math.sqrt(c)
print c

split_num = str(c).split('.')
int_part = int(split_num[0])
decimal_part = int(split_num[1])

print int_part
print decimal_part
result = a + b + c
print result

