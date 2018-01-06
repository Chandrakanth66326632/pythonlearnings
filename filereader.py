fname = input("Enter the filename :")
try:
    fhand  = open(fname)
 except:
    print("Invalid filename. File not found")
    quit()

count =0
for I in fhand:
    count = count+1
print("No of I's :", count)
