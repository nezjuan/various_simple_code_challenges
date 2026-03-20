try:
    word=input("Enter word/s:")
    width=int(input("width:"))
    padding=max(0,(width-len(word))//2)
    print(f"Result: '{' ' *padding+word+' '*padding}'")
except ValueError:
    print("invalid Input")