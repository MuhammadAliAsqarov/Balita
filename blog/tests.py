def sqrt(num):
    first = 0
    last = num
    while first <= last:
        mid = first + (last - first) // 2
        if mid == num // mid:
            return mid
        elif mid > num // mid:
            last = mid - 1
        else:
            first = mid + 1
    return last
