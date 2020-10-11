import re
matches = re.search(r'cat|dog', 'The cat is here')
print(matches.group()) 
matches = re.findall(r'.at','The cat in the hat sat there.')
print(matches)
matches = re.findall(r'^\d','1 is a number')
print(matches)
matches = re.findall(r'\d$','number is 1')
print(matches)
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
matches = re.findall(pattern,phrase)
print(matches)