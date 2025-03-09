word = str(input("Write the message to be encrypted:"))

letters = list(word)
asc = [ ord(i) for i in letters]

shifted_value =[i << 1 for i in asc]

new_letters = "".join([chr(i) for i in shifted_value])
print(word)
print(new_letters)
