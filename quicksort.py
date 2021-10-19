def sort(l: list, start: int, end: int):
    if end - start > 1:
        i = j = start
        while j < end:
            if l[j] < l[start]:
                i += 1
                l[i], l[j] = l[j], l[i]
            j += 1

        l[start], l[i] = l[i], l[start]

        sort(l, start, i)
        sort(l, i + 1, end)


def qsort(l):
    sort(l, 0, len(l))
