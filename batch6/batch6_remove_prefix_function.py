word=input("Enter a word/s:",)
prefix=input("Enter the prefix to remove: ")
if word[:len(prefix)]==prefix:
    output=word[len(prefix):]
else:
    output=word
print("Removed Prefix:",output)