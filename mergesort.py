def sort(l: list) -> list:
    return l if (mid := len(l) // 2) == 0 else merge(sort(l[:mid]), sort(l[mid:]))


def merge(l1: list, l2: list) -> list:
    l = []
    while l1 and l2:
        l.append(l1.pop(0) if l1[0] <= l2[0] else l2.pop(0))
    return l + (l1 if l1 else l2)
