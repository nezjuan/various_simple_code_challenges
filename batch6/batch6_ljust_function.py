try:
    word=input("Enter word/s: ")
    width=int(input("Width: "))
    print(f"Output: '{word+' '*max(0,width-len(word))}'")
except ValueError:
    print("Invalid Input.")