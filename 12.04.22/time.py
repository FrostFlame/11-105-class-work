import re

# print(re.findall(r'\b(?:[01]\d|2[0-3]):[0-5]\d\b', '72:00 23:89 14:15 112:16 101:101'))
string = '31.12.2021 30.11.2021 31-12-2021 32-12-2021 32-11-2021 41-12/2021 28-02-2021 29-02-2021'

pattern1 = re.compile(
    r'('
        r'(?:'
            r'(?:0[1-9]|[12]\d|3[01])'
            r'([-./])'
            r'(?:0[13578]|1[02])'
            r'\2'
            r'\d{4}'
        r')|'
        r'(?:'
            r'(?:0[1-9]|[12]\d|30)'
            r'([-./])'
            r'(?:0[469]|11)'
            r'\3'
            r'\d{4}'
        r')|'
        r'(?:'
            r'(?:0[1-9]|1\d|2[0-8])'
            r'([-./])'
            r'02'
            r'\4'
            r'\d{4}'
        r')|'
        r'(?:'
            r'29'
            r'([-./])'
            r'02'
            r'\5'
            r'\d{2}(?:[02468][048]|[13579][26])'
        r')'
    r')')
pattern = re.compile(pattern1)

print([a[0] for a in pattern.findall(string)])