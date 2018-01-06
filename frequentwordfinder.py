file = input("Enter filename :")
if len(file) < 5:
    file = "mbox-short.txt"

handler = open(file)
piece = list()
di = dict()

for line in handler:
    line = line.rstrip()
    wds = line.split()
    for word in wds:
        di[word] = di.get(word,0)+1




bigword = None
bigcount = 0

for k,v in di.items():
    if v > bigcount:
        bigcount = v
        bigword = k


print("Bigword is", bigword, "Count is  ",bigcount)
