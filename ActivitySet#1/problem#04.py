# Conditional Execution

#hrs = input("Enter hours? ")
hrs = input("Enter Hours:")
h = float(hrs)
r = float(input("rate per hour :"))
#r=float(rate)
if(h>40) :
    pay=(40*r+(h-40)*(r*1.5))
else : 
    pay=h*r
print(pay)