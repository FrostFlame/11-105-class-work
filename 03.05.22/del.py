import ctypes
import gc

x = 10
# print(x)

del x
# print(x)


class ToBeDeleted:
    def __del__(self):
        print('Меня собираются удалить')


# a = ToBeDeleted()
# del a


lst = []
lst.append(lst)
lst.append(1)
# print(lst[0])


class PyObject(ctypes.Structure):
    _fields_ = [('refcnt', ctypes.c_long)]


gc.disable()

lst_address = id(lst)

print(PyObject.from_address(lst_address).refcnt)
# del lst
# print(lst)
print(PyObject.from_address(lst_address).refcnt)

print(gc.get_threshold())
print(gc.get_referents(lst))
print(gc.get_referrers(lst))