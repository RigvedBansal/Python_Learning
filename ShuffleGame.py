from random import shuffle

def shuffle_list(ex_list):
	shuffle(ex_list)
	return ex_list

def correct_or_not(ex_list): 
	list = shuffle_list(ex_list)
	cup_no = ''
	while cup_no not in [1,2,3]:
		cup_no = int(input("Enter Your Guess: "))
	str1 = 'Yay Right Guess'
	str2 = 'Oops You are wrong'

	if ex_list[cup_no - 1] =='O':
		return str1
	elif ex_list[cup_no - 1] == ' ':
		return str2 	

gameList = [' ','O',' ']
result = correct_or_not(gameList)
print(result)
print(gameList)