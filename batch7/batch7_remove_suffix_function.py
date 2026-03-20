word=input("Enter a word/s: ")
suffix=input("Enter the suffix to remove: ")
if word[-len(suffix):]==suffix and len(suffix)>0:
    output=word[:-len(suffix)]
else:
    output=word
print("Removed Suffix:",output)