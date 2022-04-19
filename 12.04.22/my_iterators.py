class MyIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.lst):
            self.index += 1
            return self.lst[self.index - 1]


for i in MyIterator('Kenobi'):
    print(i)
