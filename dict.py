file = input("Enter file name: ")
fh = open(file)
words = list()
counts = dict()

for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)


bigword = None
bigcount = 0
for word, count in counts.items():
    if count > bigcount or bigcount is None :
        bigcount = count
        bigword = word
print(bigword, bigcount)
