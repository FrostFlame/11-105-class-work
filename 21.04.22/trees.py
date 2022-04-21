arr = [4, 2, 6, 1, 3, 5, 7, 0]


def is_binary_tree(arr):
    for i in range(len(arr)):
        if ((2 * i + 1 < len(arr) and arr[2 * i + 1] > arr[i]) or
                (2 * i + 2 < len(arr) and arr[2 * i + 2] < arr[i])):
            return False
    return True


def is_binary_heap(arr):
    for i in range(len(arr)):
        if ((2 * i + 1 < len(arr) and arr[2 * i + 1] > arr[i]) or
                (2 * i + 2 < len(arr) and arr[2 * i + 2] > arr[i])):
            return False
    return True


print(is_binary_tree(arr))
print(is_binary_heap([7, 5, 6, 1, 2, 3, 4, 0]))
