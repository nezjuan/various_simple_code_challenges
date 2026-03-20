word=input("Enter a word/s: ")
end_index=len(word)-1
while end_index>=0 and word[end_index]==" ":
    end_index-=1
output=word[:end_index+1]
print("Rstrip output:",repr(output))