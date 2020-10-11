import re
pattern = r'\d{3}-\d{3}-\d{4}'
text = "the agent's phone number is 408-555-1234. Call soon!"
print(re.search(pattern, text))
print(re.search(pattern, text).group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results)
print(results.group())
print(results.group(1))