# На вход подаётся натуральное число N
# вернуть все натуральные чилса от 1 до N,
# которые можно разложить так
# 2^k * 3^m * 5^n, где k, m, n >= 0

# Пример 10: 1 2 3 4 5 6 8 9 10

def check235(x):
    while True:
        i = x
        if x % 2 == 0:
            x = x / 2
        if x % 3 == 0:
            x = x / 3
        if x % 5 == 0:
            x = x / 5
        if x == i:
            break
    return x == 1

result = list(filter(check235, range(int(input()))))
print(result)