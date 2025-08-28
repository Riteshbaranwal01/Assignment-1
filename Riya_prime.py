//python program to check if the given number is prime or not
#import math
num = int(input("Enter an integer: "))
if num <= 1:
    print(f"{num} is not prime")
else:
    result = True
   for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
        result = False
        break
    if result :
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
