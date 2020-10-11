import collections
mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3]
print(collections.Counter(mylist))
mylist = ['a','a',10,10,10]
print(collections.Counter(mylist))
print(collections.Counter('aaaalkjdfhkjdnngbfjdsjfggnhdjfbdshtrjndxs'))
letters = 'aaaaaaaaaaaaaaaaabbbbbbbbbbbbccccccccccccccddddddddddddddd'
c  = collections.Counter(letters)
print(c)
print(c.most_common(1))
d = list(c)
print(d)
d = {'a':10}
print(d)
print(d['a'])
d = collections.defaultdict(lambda:0)
d['a']=10
print(d['a'])
print(d['b'])
mytuple = (10,20,30)
print(mytuple[0])
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(5,'Husky','Sam')
print(sammy.age)
print(sammy.breed)
print(sammy.name)