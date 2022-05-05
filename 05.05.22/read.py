import configparser

with open('users.csv', 'r', encoding='utf8') as file:
    print([word for line in file for word in line.strip().split(',')])

import csv
with open('users.csv', 'r', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        print(row)

with open('new_users.csv', 'w', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile, delimiter='%')
    writer.writerows([[1, 2, 3], [12, 45, 67]])


config = configparser.ConfigParser()
config.read('users.ini')


for var in config['NAMES']:
    print(config['NAMES'][var])

config['NAMES']['name1'] = 'new name'

with open('users.ini', 'w', encoding='utf-8') as file:
    config.write(file)


with open('new_file.txt', 'r+', encoding='utf-8') as file:
    text = file.read()
    file.seek(0)
    file.write('first line\n' + text)
