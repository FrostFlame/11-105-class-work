a = [1, 2, 3, 4, 4, 5, 9, 10]
b = [4, 4, 4, 5, 99, 100]


def foo(a, b):
    res_list = []
    for _ in range(len(a)+len(b)):
        if not a:
            res_list.extend(b)
            return res_list
        elif not b:
            res_list.extend(a)
            return res_list
        elif a[0] < b[0]:
            res_list.append(a.pop(0))
        elif a[0] >= b[0]:
            res_list.append(b.pop(0))
    return res_list

c = foo(a, b)
print(c)

# [1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 9, 10, 99, 100]