#print odd numbers
for v in range(1,100,2):
    print(v, end=" ")

#print even numbers
print(" ")
for v in range(2,100,2):
    print(v, end=" ")

print(" ")
words = ["cat","dog","elephant","ihateyou"]
for w in words[:]:
    if (len(w)>3):
        words.insert(2,w)
    print(w, len(w))