word=input("Enter a word/s: ")
output=True
for character in word:
    if "A"<=character<="Z":
        output = False
        break
if output and word!="":
    print("All characters are lowercase.")
else:
    print("Not all characters are lowercase.")