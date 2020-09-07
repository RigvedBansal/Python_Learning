s = 'hello'
print(s[1])
s = 'hello'
print(s[::-1])
s = 'hello'
print(s[4])
print(s[-1])
mylist = [0,0,0]
mylist = [0] * 3
list3 = [1,2,[3,4,'hello']]
list3 [2][2] = 'goodbye'
list4  = [5,3,4,6,1]
list4.sort()
print(list4)
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])