a = 0
b = 1
current_fib = 0
fib_sum = 0

while current_fib < 4e6:
    if current_fib%2 == 0:
        fib_sum += current_fib

    current_fib = a + b
    a, b = b, current_fib

print(fib_sum)
