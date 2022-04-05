# 24/05/2022 +
# 24.05.2022 +
# 24.05/2022 -


string = "45686F5464F1568 15a156a156 4545v45645b5485"
import re

print(re.findall(r'\d+(?P<delimiter>\w)\d+(?P=delimiter)\d+', string))
result = re.findall(r'(\d+(?P<delimiter>\w)\d+(?P=delimiter)\d+)', string)

for elem in result:
    print(elem[0])
