import re
string = 'Мария Анна-Мария ананас Иван иван Ибаа- ' \
         '-Ненио Даеран_ Арушелае Ростов-На-Дону ' \
         'Торонто-токио По-Панда'

pattern = re.compile(r'(?<!-)[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?(?!-)\b')
# print(pattern.findall(string))

print(re.findall(r'\b(?<!\")\w+(?=\')\b', '"First" "Asdadsad\' \'Second\' "Dsdasdad"'))
# '''\w = [a-zA-Z0-9_а-яёА-ЯЁ]'''