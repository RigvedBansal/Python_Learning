square = lambda num: num ** 2
print(square(6))
mynums = [1,2,3,4,5,6,7,8,9,10]
mynums1 = list(map(lambda num: num**2,mynums))
print(mynums1)
check_even = lambda num: num%2==0
print(check_even(4))
list1 = list(filter(check_even,mynums))
print(list1)