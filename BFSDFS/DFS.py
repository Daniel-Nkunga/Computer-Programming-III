import time

words = set(word.strip().upper() for word in open(r'C:\Users\danie\Desktop\Coding Spring 2024\Computer-Programming-III\BFSDFS\20k.txt'))

# # Create a set of all prefixes for all words
prefixes = set()
for word in words:
    for i in range(len(word) + 1):
        prefixes.add(word[:i])

# prefixes=set(word[:i+1] for word in words for i in range(len(word)))

def possible_anagram(possible_word, haystack):
    for letter in possible_word:
        if haystack.count(letter) < possible_word.count(letter):
            return False
    return True

letters = "kapdewustonbiglcmlg"
# kaabpdewueptonsabasngsdipcenialobsasclttnsmsunireruuielkwreilaemblageteaceeipbdgaslstecrplwgrnudala
# kapdewustonbiglcmlg
letters = letters.upper()
letter_set = set(letters)

board = [["e", "g", "e", "c", "r", "r", "h", "a", "n", "h"],
         ["f", "n", "u", "p", "p", "r", "s", "b", "s", "s"],
         ["e", "r", "n", "o", "y", "e", "i", "p", "o", "t"],
         ["s", "n", "c", "a", "r", "s", "f", "h", "r", "s"],
         ["s", "r", "e", "e", "k", "c", "i", "a", "a", "s"],
         ["e", "a", "s", "c", "s", "c", "a", "o", "o", "e"],
         ["m", "o", "r", "p", "u", "g", "h", "n", "n", "a"],
         ["n", "i", "o", "c", "e", "d", "e", "e", "n", "c"],
         ["g", "h", "y", "t", "i", "t", "o", "e", "d", "w"],
         ["o", "b", "o", "o", "u", "g", "h", "s", "s", "s"]]
for i in range(len(board)):
    for j in range(len(board)):
        board[i][j] = board[i][j].upper()

# anagrams = set()
# explored = set()

# deque = [""]
# while deque:
#     seq = deque.pop()

#     if not possible_anagram(seq, letters):
#         continue
#     if seq not in prefixes:
#         continue

#     if seq in words and len(seq) > 9:  # Add the condition to check word length
#         anagrams.add(seq)

#     for letter in letter_set:
#         deque.append(seq + letter)

# print(anagrams)
# print(prefixes)
start = time.time()
stack = [[(i,j)] for i in range(10) for j in range(10)]
count = 0
longest = ""
lower, upper = 0, 10
seen = set()
while stack:
    chain = stack.pop()
    print(chain)
    newWord = ""
    for coordinate in chain:
        newWord += board[coordinate[0]][coordinate[1]]
    # print(newWord)
    if newWord in words and newWord not in seen:
        seen.add(newWord)
        count += 1
        if len(chain) > len(longest):
            longest = newWord
            longestChain = chain
    last_coord = chain[-1]
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            x = last_coord[0] + i
            y = last_coord[1] + j
            if x >= upper or x < lower or y >= upper or y < lower:
                continue
            if (x,y) in chain:
                continue
            newWord2 = newWord + board[x][y]
            # print(newWord2)
            if newWord2 in prefixes:
                new_chain = chain + [(x,y)]
                stack.append(new_chain)



print(count)
print(longestChain)
print(longest)
print(time.time() - start)

                