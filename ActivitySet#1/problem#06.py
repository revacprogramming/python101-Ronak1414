# Loops & Iterators
'''
largest = None
smallest = None

while True:
    num = input("Enter a number? ")

y        break

    # ...

    print(num)

print("Maximum", largest)
'''
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        num=int(num)
    except :
        print("Invalid input")
        continue
    if   num > largest:
        largest=num
    if  smallest is None or num < smallest:
           smallest=num
   # print(num)

print("Maximum", largest)
print("Minimum",smallest)
print("done")