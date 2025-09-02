def fizzBuzz(n):
    i = 1  # Start from 1
    while i <= n:  # Loop until n (inclusive)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1  # Increment inside the loop

fizzBuzz(15)