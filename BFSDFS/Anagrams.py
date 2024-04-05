words = [word.strip().upper() for word in open("20k.txt")]

# Create a set of all prefixes for all words
prefixes = set()
for word in words:
    for i in range(len(word) + 1):
        prefixes.add(word[:i])

def possible_anagram(possible_word, haystack):
    for letter in possible_word:
        if haystack.count(letter) < possible_word.count(letter):
            return False
    return True

letters = "kaabpdewueptonsabasngsdipcenialobsasclttnsmsunireruuielkwreilaemblageteaceeipbdgaslstecrplwgrnudala"
letter_set = set(letters)

anagrams = set()
explored = set()

deque = [""]
while deque:
    seq = deque.pop()

    if not possible_anagram(seq, letters):
        continue
    if seq not in prefixes:
        continue

    if seq in words:
        anagrams.add(seq)

    for letter in letter_set:
        deque.append(seq + letter)

print(anagrams)