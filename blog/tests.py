class Sqrt:
    def sqrt(self, number):
        first = 0
        last = number
        while first <= last:
            middle = first + (last - first) // 2
            if middle == number // middle:
                return middle
            elif middle > number // middle:
                last = middle - 1
            else:
                first = middle + 1
        return last

jdfgj
print(Sqrt().sqrt(5))
