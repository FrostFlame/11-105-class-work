class A:
    pass

class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
class E(B, C):
    pass
class F(D):
    pass
class G(E, F):
    pass

print(G.mro())