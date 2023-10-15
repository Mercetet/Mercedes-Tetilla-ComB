def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if (arr[j+1] < arr[j]):
                aux = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = aux
    return arr

def selection(arr):
    for i in range(len(arr)):
        pos = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[pos]:
                pos = j
        if pos != i:
            tmp = arr[i]
            arr[i]=arr[pos]
            arr[pos] = tmp
    return arr

def insert(arr):
    for i in range(len(arr)):
            aux = arr[i]
            j = i - 1
            while (j >= 0) and (aux < arr[j]):
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = aux
    return arr

def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge(left_half)
        merge(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def lineal(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

def binary(arr, element):
    arr = bubble(arr)
    start = 0
    end = len(arr) - 1

    while start <= end:
        midd = (start + end) // 2
        if arr[midd] == element:
            return midd
        elif arr[midd] < element:
            start = midd + 1
        else:
            end = midd - 1

    return -1
