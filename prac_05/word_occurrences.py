"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
i swear i changed this part i started at 12.25 and finished at 12.57
"""

text = input("Text: ").split()
word_to_count = {}
for word in text:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_length = max((len(word) for word in text))

for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
