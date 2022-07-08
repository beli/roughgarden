def select(sequence: list, order: int):
    # l is the current list, o is current order statistic
    pivot = sequence[0]
    left = [e for e in sequence[1:] if e <= pivot]
    right = [e for e in sequence[1:] if e > pivot]
    pivot_index = len(left)
    if pivot_index > order - 1:
        return select(left, order)
    elif pivot_index < order - 1:
        return select(right, (order - 1) - pivot_index)
    else:
        return pivot
