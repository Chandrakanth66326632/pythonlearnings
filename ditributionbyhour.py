name = input("Enter file:")
if len(name) < 5 :
    name = "mbox-short.txt"
handle = open(name)
wds = list()
di = dict()
timer = list()
final=list()

for line in handle:
    wds= line.rstrip()
    if not line.startswith("From") :
        continue
    else:
        wds = wds.split()
        timer.append(wds[5])
        timer= timer.split(":")
        hour = timer[0]
        di[hour] = di.get(hour,0)+1

for k,v in di.items():
    newtup = (k,v)
    final.append(newtup)


final= sorted(final)

for k,v in final:
    print(k,v)
    
