word=input("Enter a word/s: ")
search_item=input("Enter the character or substring to find: ")
found_index=-1
for i in range(len(word)-len(search_item)+1):
    if word[i:i+len(search_item)]==search_item:
        found_index=i
        break
if found_index != -1:
    print("First occurrence at index:",found_index)
else:
    print("ValueError: substring not found")