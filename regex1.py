import re
text = "the agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)
pattern = 'phone'
print(re.search(pattern,text))
pattern = 'Not in text'
print(re.search(pattern,text))
pattern = 'phone'
match=re.search(pattern,text)
print(match.start())
print(match.end())
text = 'my phone once, my phone twice'
match = re.search(pattern,text)
print(match)
matches = re.findall(pattern,text)
print(matches)
for match in re.finditer('phone',text):
    print(match.span())