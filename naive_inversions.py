def count(l: list) -> int:
    return sum(
        1 for (ind, first) in enumerate(l) for second in l[ind:] if first > second
    )
