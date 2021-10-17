def count(l):
    if (mid := len(l)//2) == 0: return 0, l
    (left, l1), (right, l2) = count(l[:mid]), count(l[mid:])
    cross, l = merge(l1, l2)
    return left + right + cross, l  # inversions: on the left half, the right half, and across

def merge(l1, l2):
    cross, l = 0, []
    while l1 and l2: 
        n, cross_n = (l1.pop(0), 0) if l1[0] <= l2[0] else (l2.pop(0), len(l1)) 
        l.append(n)
        cross += cross_n
    return cross, l + (l1 if l1 else l2)

assert(count([1, 3, 5, 2, 4, 6]) == (3, [1, 2, 3, 4, 5, 6]))