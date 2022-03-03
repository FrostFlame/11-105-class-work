from collections import deque

our_list = input().split()
total = 0

result = deque()

for elem in our_list:
    if elem not in ['+', '-', '/', '*']:
        result.append(elem)
    elif elem == '+':
        b = int(result.pop())
        a = int(result.pop())
        result.append(a + b)
    elif elem == '-':
        b = int(result.pop())
        a = int(result.pop())
        result.append(a - b)
    elif elem == '*':
        b = int(result.pop())
        a = int(result.pop())
        result.append(a * b)
    elif elem == '/':
        b = int(result.pop())
        a = int(result.pop())
        result.append(a / b)
print(result.pop())
