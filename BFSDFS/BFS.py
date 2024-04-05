import time

words= set(word.strip().upper() for word in open(r'C:\Users\danie\Desktop\Coding Spring 2024\Computer-Programming-III\BFSDFS\20k.txt'))
prefixes=set(word[:i+1] for word in words for i in range(len(word)))
prefixes.add("")
# print(len(prefixes))


def possible_word(word):
    possible_words = set()
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        
        #Add character to the front
        new_word = char + word
        if new_word in words:
            possible_words.add(new_word)
            # print(possible_words)
    
        #Add a character to the end
        new_word = word + char
        if new_word in words:
            possible_words.add(new_word)
            # print(possible_words)

        #Replace character
        for i in range(0, len(word)):
            new_word = word[:i] + char + word[i+1:]
            if new_word in words:
                if new_word != word:
                    possible_words.add(new_word)
                    # print(possible_words)
        
        #Remove character
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            if new_word in words:
                possible_words.add(new_word)
                # print(possible_words)

        #Add character in middle
        for i in range(len(word)):
            new_word = word[:i] + char + word[i:]
            if new_word in words:
                possible_words.add(new_word)
                # print(possible_words)
    return possible_words

startTime = time.time()
#Manual boundaries
start = "fox"
start = start.upper()
target = "ground"
# target = "fond"
target = target.upper()

#How long is the queue
queue = [(start,)]
solutions = []
depth = {}
max_depth = 999_999
count = 0
while queue:
    chain = queue.pop(0)
    # chain = queue.pop()
    count += 1
    print(chain)
    for word in possible_word(chain[-1]):
        new_chain = chain+(word,)
        if len(new_chain) > max_depth: 
            continue
        if word == target:
            solutions.append(new_chain)
            max_depth = len(new_chain)
            # print(new_chain)
        if word not in depth: 
            depth[word] = len(new_chain)
        elif depth[word] < len(new_chain):
            continue
        queue.append(new_chain)

print(solutions)
print(len(solutions))
print(count)
print(time.time() - startTime)