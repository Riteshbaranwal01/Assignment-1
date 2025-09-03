num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a Prime number.")
else:
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print(num, "is a Prime number.")
    else:
        print(num, "is NOT a Prime number.")
