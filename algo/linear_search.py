#       best/worst
# TC    O(n)
# SC    O(1)


def search(arr, value):
    l = len(arr)
    for index, elem in enumerate(arr):
        if elem == value:
            return index
    
    return -1

if __name__ == '__main__':
    arr = [1,21,3,4,25]
    value = 21
    print(search(arr, value))
