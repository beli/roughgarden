def sort(l):
    mid = len(l)//2
    if mid == 0:
        return l
    return merge(sort(l[:mid]), sort(l[mid:]))

def merge(l1, l2):
    l = []
    while l1 and l2:
        l.append( l1.pop(0) if l1[0] < l2[0] else l2.pop(0) )
    l += l1 if l1 else l2
    return l 

print(sort(list(range(20)[::-1])))