def binary_search(array, target):
    min = 0
    max = len(array) - 1

    while max >= min:
        mid = (max + min) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            min = mid + 1
        else:
            max = mid - 1

    return -1


def binary_search_recursive(array, target):
    if len(array) == 0:
        return False

    mid = len(array) // 2
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search_recursive(array[mid + 1:], target)
    else:
        return binary_search_recursive(array[:mid - 1], target)


arr = [0, 5, 13, 19, 22, 41, 55, 68, 72, 81, 98]
print('binary search 72: ' + str(binary_search(arr, 72)))
print('binary search recursive 72: ' + str(binary_search_recursive(arr, 72)))