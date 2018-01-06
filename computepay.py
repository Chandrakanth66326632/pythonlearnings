def computepay(h,r):
    if h > 40:
        p1 = 40 * r
        p2 = (h-40)*1.5*r
        p = p1+p2
    elif h <= 40:
        p = h*r
    return p

hrs = input("Enter Hours:")
rate = input("Enter rate:")
h= float(hrs)
r=float(rate)
p = computepay(h,r)
print("Pay",p)
