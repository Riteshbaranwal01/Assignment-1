def is_prime(num):
  """Checks if a given number is prime."""
  if num <= 1:
    return False  # Numbers less than or equal to 1 are not prime
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False  # If divisible by any number from 2 to sqrt(num), it's not prime
  return True  # Otherwise, it's prime

# Get input from the user
while True:
    try:
        number = int(input("Enter an integer to check if it's prime: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Check and print if the number is prime
if is_prime(number):
  print(f"{number} is a prime number")
else:
  print(f"{number} is not a prime number")
