def gcd(a, b):
    assert a >= b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def factorial(x):
    assert x >= 0
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def new_gcd(a, b):
    assert a >= b
    return a if b == 0 else new_gcd(b, a % b)


if __name__ == '__main__':
    a = 109032
    b = 4839
    print(f'{gcd(a, b)}')
    print(f'26!={factorial(26)}')
    print(f'{new_gcd(a, b)}')
