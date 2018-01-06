a = input("Enter a string :")
print(a)
try:
    b=int(a)
    print("it is in try block")
except:
    b=-1
    print("it is in except block")

if b > 0:
    print("user gave a number, it worked")
elif b < 0:
    print("User gave a string, it dint worked")
