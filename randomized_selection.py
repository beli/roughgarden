def select(l: list, o: int):
    # l is the current list, o is current order statistic
    pivot = l[0]
    left = [e for e in l[1:] if e <= pivot]
    right = [e for e in l[1:] if e > pivot]
    pivot_index = len(left)
    if pivot_index > o - 1:
        return select(left, o)
    elif pivot_index < o - 1:
        return select(right, (o - 1) - pivot_index)
    else:
        return pivot
