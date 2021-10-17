from typing import Tuple


def count(l: list) -> Tuple[int, list]:
    if (mid := len(l) // 2) == 0:
        return 0, l
    (left, l1), (right, l2) = count(l[:mid]), count(l[mid:])
    cross, l = merge(l1, l2)
    return left + right + cross, l


def merge(l1: list, l2: list) -> Tuple[int, list]:
    cross, l = 0, []
    while l1 and l2:
        n, cross_n = (l1.pop(0), 0) if l1[0] <= l2[0] else (l2.pop(0), len(l1))
        l.append(n)
        cross += cross_n
    return cross, l + (l1 if l1 else l2)
