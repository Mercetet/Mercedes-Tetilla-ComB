def add_digits(n):
    auxd = 0
    add=0

    while n != 0:
        digit = n % 10
        add += digit
        auxd += digit
        n //= 10
    return add