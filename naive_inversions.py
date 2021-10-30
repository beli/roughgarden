def count(l: list) -> int:
    return sum(
        1 for (ind, earlier) in enumerate(l) for later in l[ind:] if earlier > later
    )
