word=input("Enter a word/s: ")
width=int(input("Enter the total width: "))
padding=width-len(word)
if padding>0:
    output=" "*padding+word
else:
    output=word
print("Rjust output:",output)