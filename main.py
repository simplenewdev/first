# SETS SETS SETS SETS SETS SETS SETS SETS SETS


color = ['blue','green','red','yellow']

fruit = ['blueberry','apple','cherry','banana']

print (f"0 {color[1]} {fruit[1]}")
print (f"0 {color[2]} {fruit[2]}")
print (f"0 {color[3]} {fruit[3]}")
num = 0 

for i in range(4):
    print (f"{num} {color[(num)]} {fruit[(num)]}")
    num += 1 


test = {1,2,3,4,5,6}
print (type(test))
A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print (A.union(B))
print (B.difference(A)) # print the diffrent numbers numbers
print (A.symmetric_difference(B))
print (A.intersection(B)) # print the duplicated numbers
print (A.difference(B)) # B)) # print the diffrent numbers numbers ignoring the order of sets
c = {1, 2, 3, 4, 5}
d = {1, 2, 4}
print (c.issuperset(d)) # superset means the first set is the superset bc it has all the numbers in the other set
# outpussubset true
print (d.issubset(c)) # subset is true bc it doesnt have all the numbers in the other list
# output true
B = {1, 2, 4}
print(1 in B)
# Output: True

print(3 in B)
# output false

# pretty self explantory


empty_set = set() # set() is used to make empty sets


S = set()
 
S.add(2)
print(S)
#Output: {2}
 
S.remove(2)
print(S)
# Output: set()
 
# SELF EXPLANTORY

A = {1, 2, 3}
B = {3, 4, 5}
 
S = set()

S.update(A)
print(S)
# Output: {1, 2, 3}
 
S.update(B)
print(S)
# Output: {1, 2, 3, 4, 5}

# ADDING ANOTHER UPDATE DOES NOT RESET THE LIST IT JUST ADDS THE OTHER LISTS NUMBER



S1 = {1, 2, 3}
S2 = S1.copy()  # independent copy of S1
S1.clear()
 
print(S1)
#Output: set()
 
print(S2)
#Output: {1, 2, 3}

# also self explantory


S = {1, 7, 3, 9, 5}
for number in S:
    print(number)
 
# Output:
# 1
# 3
# 5
# 7
# 9

# IT COUNTS THE LIST NORMALLY BY ORDER OF THE NUMBERS NOT THE LIST LIKE 1 2 3 4 5 6 7 EVEN IF THE LIST IS 7 5 4 3 2 1 


values = [1, 2, 2, 1, 3, 4, 1, 2, 3, 4, 1]
unique_values = set(values)
print(unique_values)

 #USED TO REMOVE DUPLICTES FROM A LIST BC A SET ONLY HAS UNIQUE VALUES

# multiplycation @


import numpy as np
a = np.array([
[1, 2],
[3, 4]
])

b = np.array([
[-1, 0],
[2, -2]
])
result = (a @ b)
print (result)


A = [
    [1, 2],
    [3, 4]
]
B = [
    [-1, 0],
    [2, -2]
]
result = [
    [0, 0],
    [0, 0]
]
for i in range(len(A)):          # rows of A
    for j in range(len(B[0])):   # columns of B
        for k in range(len(B)):  # columns of A/rows of B
            result[i][j] += A[i][k]*B[k][j]
print(result)
# Expected result:
# [[3, -4], [5, -8]]


A = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([10, 20])
result = A + b  # add row vector b to each row of A
print(result)
# Expected result:
# [[11 22]
#  [13 24]]

# DICOTANRIES DICOTANRIES DICOTANRIES DICOTANRIES DICOTANRIES DICOTANRIES DICOTANRIES DICOTANRIES DICOTANRIES DICOTANRIES 

config = {
         "color": "green",
        "width": 42,
        "height": 100,
       "font": "Courier",
    }

 # Access a value through its key
print (config["color"])
print (config["font"])
print (config["height"])
print (config["width"])


# Update a value
config["font"] = "Helvetica"
print (config["font"])

user_data = {
"user_123": {"name": "Alice", "email": "alice@example.com"},
 "user_456": {"name": "Bob", "email": "bob@example.com"},
 "user_789": {"name": "Charlie", "email": "charlie@example.com"}
}
# Fast lookup - goes directly to the value
print(user_data["user_456"]) # {'name': 'Bob', 'email': 'bob@example.com'}

ppl = {
  "person1": {"orange": 12}
}
print (ppl)
ppl["person2"] = {"apple": 17}
print(ppl)
#del ppl["person2"]
#print (ppl)
items = ppl.items()
print (items)
keys = ppl.keys()
print (keys)
values = ppl.values()
print(values)

from collections import defaultdict
# Grouping items by category
products_by_category = defaultdict(list)
products = [
    ("Electronics", "Laptop"),
    ("Electronics", "Phone"),
    ("Clothing", "Shirt"),
    ("Electronics", "Tablet"),
    ("Clothing", "Pants")
]
# Loop through each (category, product) pair and 
# if the key does not exist create an empty list for it
for category, product in products:
    products_by_category[category].append(product)
print(dict(products_by_category))


example = [1,2,3, 3]
example1 = {1,2,3, 3}
example2= (1,2,3, 3)
example3= {"name": "1" "bob", "2": 2}
print (type(example))
print (type(example1))
print (type(example2))
print (type(example3))
print (example3["2"])

gender = defaultdict(list)
ppl = [
    ("gay", "mino"),
    ("straight", "suzuya"),
    ("gay", "sans"),
    ("demon", "rhe")
]
for gen, person in ppl:
    gender[gen].append(person)

print (dict(gender))
 
from collections import Counter

ppl_prof_views = ["sans","star","star","star","suzie","sans","suzie","vlad","vlad","star","star","sans","star","suzie","vlad",]
ppl_prof_views_count = Counter(ppl_prof_views)
print (ppl_prof_views_count)

from collections import ChainMap

defaults = {"debug": False}
env = {"debug": True}

config = ChainMap(env, defaults)


from types import MappingProxyType

d = {"a": 1, "age": 17, "id": 123456789}
readonly = MappingProxyType(d) #shows the dict but read only so incase of accidents
print (readonly)

# FUNCTIONS FUNCTIONS

def add(x,y):
    total = (x + y)
    print (total)

add(10,10)

def analyze_text(text):
    length = len(text)
    word_count = len(text.split())
    upper = text.upper()
    return length,word_count,upper
length, word_count, upper = analyze_text("bim bim bam bam")
print (f"there are {word_count} words in")