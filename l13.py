# Read text from the user
text = input("Enter text: ")

char_freq = {}
for ch in text:
    if ch.isalnum(): 
        ch = ch.lower()
        if ch in char_freq:
            char_freq[ch] += 1
        else:
            char_freq[ch] = 1

print("Character frequencies:")
for ch, freq in char_freq.items():
    print(f"{ch}: {freq}")
