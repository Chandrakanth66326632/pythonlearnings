

file = input("Enter filename :")
if len(file)  5:
    file = "mbox-short.txt"
 
handler = open(file)
piece = list()
di = dict()
print(" Sorting based on the value") 
for line in handler:
    line = line.rstrip()
    wds = line.split()
    for word in wds:
        di[word] = di.get(word,0)+1


for k,v in di.items():
    newtup = (v,k)
    piece.append(newtup)

piece = sorted(piece, reverse= True)

for v,k in piece[:10]:
    print(k,v)

