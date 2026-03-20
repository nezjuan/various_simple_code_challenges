word=input("Enter a word/s: ")
is_uppercase=True
for character in word:
    if "a" <= character <= "z":
        is_uppercase = False
        break
if is_uppercase and word!="":
    print("All characters are uppercased.")
else:
    print("Not all characters are uppercased.")