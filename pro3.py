import random
n=int(input("Enter the size of password: "))
s=" "
for i in range(0,n):
    r=random.randint(33,126)
    s=s+chr(r)
print("The password is: ")
print(s)
