word=input("Enter a word/s: ")
item_to_count=input("Enter item to count: ")
count_total=0
counter=0
while counter<=len(word)-len(item_to_count):
    if word[counter:counter+len(item_to_count)]==item_to_count:
        count_total+=1
    counter+=1
print("Item/Word/Element Count:",count_total)