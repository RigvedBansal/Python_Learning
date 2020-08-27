mylist = [x**2 for x in range(1,101)]
total = 0 
for item in mylist:
	total += item
total2 = 0
for num in range(1,101):
	total2 += num
print(total)
print(total2)
total2 = total2 ** 2
result = total2 - total
print(result)	