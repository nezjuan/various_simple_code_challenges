word=input("Enter a word/s: ")
output=""
for character in word:
    if "a" <= character <= "z":
        output+=chr(ord(character)-32)
    else:
        output+=character
print("upper cased:",output)