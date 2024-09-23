def sqrt(x: int) -> int:
    first = 0
    last = x
    if x == 0:
        return 0
    while first <= last:
        mid = first + (last - first) // 2
        if mid == x // mid:
            return mid
        elif mid > x // mid:
            last = mid - 1
        else:
            first = mid + 1
    return last


print(sqrt(121))
