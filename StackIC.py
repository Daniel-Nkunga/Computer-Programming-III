#Depth First Search: We go deep first
# stack = [""]
# count = 0
# max_stack_size = len(stack)
# while stack:
#     max_stack_size = max(max_stack_size, len(stack))
#     elem = stack.pop()
#     print(elem)
#     if len(elem) == 8:
#         continue
#     for letter in "ab":
#         new_elem = elem+letter
#         stack.append(new_elem)
#         #stack+=new_elem,
# print(max_stack_size)

#Breadth First Search: We go layer by layer [We go wide]
deque = [""] #Deque is a Double Ended Que
max_deque_size = len(deque)
while deque:
    max_deque_size = max(max_deque_size, len(deque))
    elem = deque.pop(0) #this is the only thing change becuase we're in a stack
    print(elem)
    if len(elem) == 8:
        continue
    for letter in "ab":
        new_elem = elem+letter
        deque.append(new_elem)
        #stack+=new_elem,
print(max_deque_size)

#Looking for bbb
deque = [""] #Deque is a Double Ended Que
max_deque_size = len(deque)
count = 0
while deque:
    max_deque_size = max(max_deque_size, len(deque))
    elem = deque.pop(0) #this is the only thing change becuase we're in a stack
    print(elem)
    count+="bbb" in elem
    if len(elem) == 8:
        continue
    for letter in "ab":
        new_elem = elem+letter
        deque.append(new_elem)
        #stack+=new_elem,
print(max_deque_size)
print(count)

#DFS
    #PROS
        #Uses less memory
    #CONS
        #Can't handle infinite trees
#BRF
    #PROS
        #Finds solutions closer to gome
    #CONS
        #Uses more memory