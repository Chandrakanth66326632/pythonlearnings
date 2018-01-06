import re

file = input("Enter filename :")
handler = open(file)
count = 0
lst = list()
di = dict()
for line in handler:
    line = line.rstrip()
    if re.search("^From:", line):
        count = count +1
        lst = line.split()
        for word in lst:
            di[word]= di.get(word,0)+1
        print(di)
    else:
        continue

print("I am done")
