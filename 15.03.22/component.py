class MyComponent:
    pass

class MyComposit:
    def __init__(self, arg1, arg2):
        self.component = MyComponent()

class Element:
    pass

class FullClass:
    def __init__(self, element):
        self.element = element


element = Element()
fc = FullClass(element)
