#looping through string

a = "hello world"
for letter in a:
    print(letter)

#string slicing
b = a[3:20]
print(b)

#string comparisons
if "hello"=="Hello":
    print("size doesn't matter")
else:
    print("size matters")

#string functions
print(b.lower())
print(b.upper())
print(b.replace("l","A"))
print(b.capitalize())
print(b.find("l"))