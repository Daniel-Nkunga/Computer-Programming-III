import time

words= [word.strip().upper() for word in open(r"C:\Users\danie\Desktop\Coding Spring 2024\Computer-Programming-III\DFBFS In Class\20k.txt")]

prefixes=set(word[:i+1] for word in words for i in range(len(word)))
prefixes.add("")
print(len(prefixes))


def possible_anagram(possible_word,haystack):
	for letter in possible_word:
		if haystack.count(letter)<possible_word.count(letter):
			return False
	return True

letters="STXRBQ3EADOUS"
letter_set=set(letters)
# ~ print(letter_set)
anagrams=set()
explored=set()

deque=[""]
start = time.time()

#BFS
while deque:
	# seq=deque.pop()
	seq=deque.pop(0)
	# if seq in explored:
	# 	continue
	# explored.add(seq)
	if not possible_anagram(seq,letters):
		continue
	if seq not in prefixes:
		continue
	if seq in words:
		anagrams.add(seq)
	for letter in letter_set:
		deque.append(seq+letter)
	#BFS Time: 0.29581451416015625
	#DFS Time: 0.27121806144714355
		
print(anagrams)	
end = time.time()
print(len(anagrams))
print(end - start)