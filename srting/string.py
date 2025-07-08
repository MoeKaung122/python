name = 'Moe Kaung' #srting
text = "Hello, World!" #srting

message = """
hello word 
hello word
hello word
"""
# print(name)
# print(len(name)) # length of string

# print(text)     
# print(message)

# sequence string
print(text[0]) # first character of string
print(text[-1]) # last character of string



# string slicing
print(text[0:5]) # first 5 characters of string

# concatenate string
print(name + " " + text) # concatenate name and text

# formatted string
channel = "{} says: {}".format(name, text) # formatted string using format method
print(channel)
print(f"{name} says: {text}") # formatted string using f-string

# string methods
print(text.lower()) # convert string to lowercase
print(text.upper()) # convert string to uppercase   
print(text.title()) # convert string to title case
print(text.find("World")) # find substring in string
print(text.replace("World", "Python")) # replace substring in string    