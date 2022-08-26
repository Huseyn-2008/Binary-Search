def search(array, x, low, high):
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("There given a list\n[1, 2, 3, 4, 5, 6, 7, 8, 9]")
x = int(input("Which number's index you want to find: "))
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

binarysearc = search(array, x, 0, len(array) - 1)
print(binarysearc)
