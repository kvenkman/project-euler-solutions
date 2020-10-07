def check_prime(num):
    for i in range(num//2, 1, -1):
        if num%2 == 0:
            return False

    return True


def main():
    target_num = 600851475143

    largest_divisor = target_num//2
    largest_divisor = largest_divisor - 1 if (largest_divisor%2 == 0) else largest_divisor

    for i in range(largest_divisor, 1, -1):
        if check_prime(i) and (target_num % i == 0):
            print(i)
            break

main()
