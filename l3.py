# Read a sentence from the user
sentence = input("Enter a sentence: ")
words = sentence.split()

# Count frequency of each word using only lists
unique_words = []
frequencies = []
for word in words:
    if word in unique_words:
        idx = unique_words.index(word)
        frequencies[idx] += 1
    else:
        unique_words.append(word)
        frequencies.append(1)

print("Word frequencies:")
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {frequencies[i]}")
