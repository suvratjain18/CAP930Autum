# In this we can Sort the Order of the roll number
roll=[1,5,6,2,10,4,3,8,7,9]
roll.sort();
print(roll);
# in this case if we want to reverse order
roll=[1,5,6,2,10,4,3,8,7,9]
roll.reverse()
print(roll)
empty={}
print(type(empty))
#output of empty <class 'dict'>
print(empty==dict())
#Output True
a=dict(one=1,two=2,three=3)
b={"one":1,"two":2,"three":3}
print(a==b)
#Check the a==b is or not True
#Dictionary Creation
info={"Name":"Suvrat Jain","Reg":"11714694","Achievements":"Bharat Ratan"}
d1=dict(Name="Suvrat Jain",Reg=11714694,Achievements="Bharat Ratan")
#your Dictionary Values
d['two']=22
d['four']=4
# Create a Dictionary using List
d={"CS":[106,107,110],"MATH":[51,115]}
d["COMPSCI"]
d.get("CS")
d.get("PHIL") # Using get we can't Show the output of Key Value error
# With This we can create empty List in using get method
 english_classes=d.get("ENGLISH",[])
 num_english=len(english_classes)
 print(num_english) # It shows the output 0
 # It works even there is no english_classes in the dictionary
 
#////////////
 #how to delete a key in dictionary
 
del d['three']
del d['four']
#If there is not key value then it shows
#default value if not in the map

d.pop('three')

d.popitem() # it removes last item in the list

# DICTIONARIES
d={"one":1,"two":2,"three":3}
d.keys()# Output is (one,two,three)
d.values()# output is (1,2,3)
d.items()# Output is (one:1,two:2,three:3)
#These dictionary views are dynamic reflecting changes in the
# underlying dictionary;

('one',1) in d.items() # This is membership Functions

for value in d.values(); # Create a dictionary print output Using for loop
    print(value)

#Common Dict Operations
 len(d)
 key in d
     # equiv. to key in d.keys()
 value in d.values()
 d.copy()
 d.clear()

#Tuples
 #Immutable Sequences
t = (1,"cat")

fish=(1,2,"red","blue")
fish[0]
fish[0]=7 # Raises a tyeError

len(fish) # 4
fish[:2] # (1,2)
"red" in fish # true

# IN this if we write without any Braces or brackets then its also created in tuples
 gd=("Suvrat Jain","MCA","22-10-1996")
 gd #('Suvrat Jain', 'MCA', '22-10-1996')
# Packed and Unpacked values
x,y,z = gd
print(x)
print(y)
print(z)

# Swap Values in Python
x=10,y=9
x,y=y,x
print(x,y)


# Example




 







