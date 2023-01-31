from math import log2, ceil

def to_bin(n: int) -> str:
    return f'{n:b}'


def to_oct(n: int) -> str:
    return f'{n:o}'


def to_hex(n: int) -> str:
    return f'{n:x}'


def from_ca2(n:str) -> int:
    l = len(n)
    return int(n[1:], 2) - 2 ** l


def to_ca2(n: int, l: int) -> str:
    if n < 0:
        o = to_bin(2 ** (l-1) + n)
        return '1' + '0'* (l-len(o)-1) + o
    else:
        o = to_bin(n)
        return '0'*(l-len(o)) + o