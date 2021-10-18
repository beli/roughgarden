def count(l: list) -> int:
    return sum(
        1 for (ind, before) in enumerate(l) for after in l[ind:] if before > after
    )
