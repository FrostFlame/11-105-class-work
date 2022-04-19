with open('task5.txt', 'w', encoding='utf-8') as file:
    file.write('01 111\n')
    file.write('10 11 101 111 100 1011 1001\n')
    file.write('0010 0110 1110 10')

# 1) \b(0|11)1\b                01 111
# 2) \b10?[01]1?\b              10 11 101 111 100 1011 1001
# 3) \b(00|01|11)?10\b          0010 0110 1110 10