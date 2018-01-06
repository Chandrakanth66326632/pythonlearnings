hrs = input("Enter hours : ")
rate = input("Enter rate : ")
h = float(hrs)
r = float(rate)
if h > 40.0 :
    p1 = 40 * r
    p2 = (h-40) * r
    pay = p1+p2
    print("Pay : ",pay)
elif hrs <= 40.0:
    pay = h * r
    print("Pay : ",pay)
    
