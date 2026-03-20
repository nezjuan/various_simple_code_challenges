word = input("Enter a word/s: ")
output = ""
for character in word:
    if "A" <= character <= "Z":
        output+=chr(ord(character) + 32)
    else:
        output+=character
print("lower cased:",output)