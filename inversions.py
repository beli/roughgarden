def count(l):
    mid = len(l)//2
    if mid == 0: return 0, l
    (left, l1), (right, l2) = count(l[:mid]), count(l[mid:])
    splits, l = merge(l1, l2)
    return left + right + splits, l

def merge(l1, l2):
    splits, l = 0, []
    while l1 and l2: 
        n, n_split = (l1.pop(0), 0) if l1[0] <= l2[0] else (l2.pop(0), len(l1)) 
        l.append(n)
        splits += n_split
    l += l1 if l1 else l2
    return splits, l 

assert(count([1, 3, 5, 2, 4, 6]) == (3, [1, 2, 3, 4, 5, 6]))