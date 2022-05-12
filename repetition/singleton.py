class Singleton:
    __obj = None

    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            cls.__obj = super().__new__(cls)
        return cls.__obj


s1 = Singleton()
s2 = Singleton()
print(s1)
print(s2)
print(s1 == s2)
