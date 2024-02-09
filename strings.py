text = "hello"
texttwo = "THERE"
a: int = 24
print(a)
print(text)

# Accessing an element in a string
print(text[0])

# Modifying a string
print(text.upper())
print(texttwo.lower())

# Size/Length of a string
print(len(text))
# String Concatenation - Combining/Joining of string
print(text, texttwo)
print(text + "", texttwo)

# Assignment
# 1. Reassigning a value to variable
new_text = text.replace("hello", "hi")
print(new_text)
# 2. Delete a variable
del a
print(a)
