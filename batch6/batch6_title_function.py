word=input("Enter a word/s: ")
letters=word.split()
output=[]
for letter in letters:
    first=word[0].upper()
    rest=word[1:].lower()
    output.append(first+rest)
print("Titled Output:",output)