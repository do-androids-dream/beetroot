"""
min()
len()
in()
sort() - *з зірочкою
"""


def custom_min(arr): # O(n)
    if arr:
        min_value = arr[0]

        i = 1
        while i < len(arr):
            if arr[i] < min_value:
                min_value = arr[i]
            i += 1
        return min_value
    return None


def custom_len(arr): # O(n)
    if arr:
        i = 0
        while i <= len(arr): # try except
            i += 1

        return i
    return 0


def custom_in(arr, el): # O(n)
    if arr:
        i = 0
        while i < len(arr):
            if el == arr[i]:
                return True
        return False
    return False


def custom_sort(arr): # O(n**2)
    length = len(arr) // 2
    while length:
        length -= 1
        i = 0
        k = i + 1

        while k < len(arr):
            if arr[i] > arr[k]:
                arr[i], arr[k] = arr[k], arr[i]
            k += 1
            i += 1
    return arr


print(custom_sort([6, 1, 2, 5, 4, 3]))
