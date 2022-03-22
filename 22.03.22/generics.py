from typing import Optional, Union, List, Tuple, Any, Dict, NoReturn, Iterable, Generator, Callable, Generic, TypeVar, \
    get_type_hints, cast

x: Optional[str] = 5  #  Union[int, None]

# x = 'string'
x = 10

x = None


y: Union[int, str]
y = 'asdas'
y = 5


# x.startswith('a')


# def foo(x: Union[int, bool]) -> str:
#     return None


# foo('asdsa')


titles: List[str]
# titles.append(5)
# titles.append('asdasd')
# titles = ['asdada', 5]


container: Tuple[int] = (1,)
container = ('asdas',)
container = (1, 2)

container1: Tuple[int, ...] = (1, )
container1 = (2, 3, 4, 5)

containe2: Tuple[Any, int]


my_dict: Dict[str, int] = dict()

my_dict['asda'] = 'asdas'
my_dict[1] = 2


def forever() -> NoReturn:
    while True:
        pass


def generate_two() -> Iterable[int]:
    yield 1
    yield 2


def generate() -> Generator[int, str, str]:
    x = 0
    while True:
        # if x == 7:
        #     return 'Stop iteration'
        x = yield x * 2

gen = generate()
print(next(gen))
print(gen.send(10))
print(gen.send(5))
print(gen.send(7))
print(gen.send(4))

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def foo(arg1: int, arg2: str) -> bool:
    pass


def bar(func: Callable[..., bool]):
    pass


T = TypeVar('T')


class GenericLinkedList(Generic[T]):
    data: T
    next_node: 'GenericLinkedList[T]'

    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        node = self
        while node is not None:
            result += str(node.data) + ' '
            node = node.next_node if hasattr(node, 'next_node') else None
        return result


head_int: GenericLinkedList[int] = GenericLinkedList(2)
head_int.next_node = GenericLinkedList(3)
print(head_int)

head_int.next_node = 2

head_str: GenericLinkedList[str] = GenericLinkedList('one')
head_str.next_node = GenericLinkedList('two')
print(head_str)

head_str.next_node = GenericLinkedList(2)

print(head_str)

print(GenericLinkedList.__annotations__)
print(get_type_hints(GenericLinkedList))
print(foo.__annotations__)
print(get_type_hints(foo))


def find_first_str(a: List[object]) -> int:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    print(a[index])
    print(cast(str, a[index]))
    return a[index]


a = [1, 2, b'dasd', True, 'string', 'second_string']
find_first_str(a)
