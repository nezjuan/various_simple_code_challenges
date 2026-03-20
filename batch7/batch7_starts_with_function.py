word=input("Enter a word/s: ")
prefix = input("Enter the prefix to check: ")
if len(prefix)>0 and word[:len(prefix)]==prefix:
    print("The string starts with the given prefix.")
else:
    print("The string does NOT start with the given prefix.")