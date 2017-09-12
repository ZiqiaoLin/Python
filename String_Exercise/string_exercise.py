str1 = "Hello"
str2 = 'there'
john = str1 + str2
print(john)
str3 = "123"
x = int(str3) + 1 ## parse string as integer
print(x) ## expected as 124

fruit = "banana"
index = 0
while (index < len(fruit)):
    letter = fruit[index]
    print(index,letter)
    print("--------------")
    index = index + 1
print()

## another way to use loop
for letter in fruit:
    print(letter)

s = "Monty Python"
print(s[0:4]) #from index 0 up to index 4 but not including 4,expected "Mont"
print(s[6:20]) # from index 6 up to index 20,but beyond the index already
print(s[:2])
print(s[2:])
print(s[:])


##### String Concatenation Exercise

'n' in fruit
'm' in fruit
if 'a' in fruit:
    print("found it !")

##### String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
type(zap)
dir(zap)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])