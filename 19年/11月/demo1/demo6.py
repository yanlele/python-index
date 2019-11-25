def isprime(n):
    count = 0
    for i in range(1, int(n // 2 + 1)):
        if n % i == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


def main():
    num = eval(input())
    a = int(num)
    i = 2
    formula = ''
    while not isprime(num):
        if isprime(i) and num % i == 0:
            formula += str(i) + ' '
            num /= i
        else:
            i += 1
    formula += str(int(num))
    print(formula)


main()
