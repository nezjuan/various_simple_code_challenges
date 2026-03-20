word=input("Enter a word/s: ")
suffix=input("Enter the suffix to check: ")
print(f"Ends With: {word[len(word) - len(suffix):] == suffix}")