# What Is Sets
#collection of well defined things or elements
#or
# Unorderd collection of distinct hashable elements

#In First Create a set
s={1,2,3}
print(s)
print(type(s))
t={'M','K','R'}
print(t)
print(type(t))
# How you can declare Empty Set using below here
# empty_set=set()
# it will convert list to string below example
set_from_list=set([1,2,1,4,3])

basket={"apple","orange","apple","pear","banana"}
len(basket) # Output is 4 Because it detects only distinct ones

orange in basket #check membership functions

for fruit in basket:
    print(fruit,end='/')
    
a=set('abracadabra')
b=set('alacazam')
print(a)
print(b)
 a-b # means common between two sets a is not showing
# Output above command a-b {'d', 'b', 'r'}
>>> a|b # It means union
# Output of both sets {'l', 'z', 'r', 'b', 'a', 'd', 'c', 'm'}

a&b # letters in both a and b
a^b # letters in a or b but not both (a-b U b-a)


a=set('missippi') # its Output is in sets {'m','i','s','p'}
a.add('r') # its add in a set
a.remove('r') # its remove r in the set
a.pop() # it removes the set value from the first
