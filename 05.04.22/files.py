import pickle


class MyTextClass:
    def __init__(self, text):
        self.text = text
        self.length = len(text)

with open('my_lambdas.py', 'r', encoding='utf-8') as file:
    my_text_obj = MyTextClass(file.read())

pickle.dump(my_text_obj, open('my_simple_pickle.pkl', 'wb'))

my_deserialized_obj = pickle.load(open('my_simple_pickle.pkl', 'rb'))
print(my_deserialized_obj.text)