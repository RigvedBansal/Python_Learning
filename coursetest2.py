st = 'Print only the world that Start with s in this sentence'
mylist = st.split()
for word in mylist:
	if word[0] == 's' or word[0] == 'S':
		print(word)

for num in range(0,11,2):
	print(num)	

list1 = [x for x in range(1,51) if x%3==0]
print(list1)

st = 'Print every word in this sentence that has an even number of letters'

list2  = st.split()
for word in list2:
	if len(word)%2 == 0 :
		print("EVEN")
	else:
		print(word)

mylist = [x for x in range(1,101)]
for num in mylist:
	if num % 3 == 0 and num % 5 == 0:
		print("FizzBuzz")
	elif num % 5 == 0:
		print("Buzz")
	elif num % 3 == 0:
		print("Fizz")
	else:
		print(num)

st = 'Create a list of the first letters of every word in this string'
mylist = st.split()
mylist = [word[0] for word in mylist]
print(mylist)		