target = 100
for n in range(1, target + 1):
  if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 3 ==0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)