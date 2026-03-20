word = input("Enter Word: ")
word_count = 0
while word_count < len(word) and word[word_count] == " ":
    word_count += 1
output = word[word_count:]
print("lstrip output:", output)