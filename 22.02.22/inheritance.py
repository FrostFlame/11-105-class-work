class A:
    def foo(self):
        print('A')

class B(A):
    pass

class C(A):
    def foo(self):
        print('C')

class D(B, C):
    pass

d = D()
d.foo()