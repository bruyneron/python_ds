
# Note: To do binary search array has to be sorted (ascending/descending)
#       best/worst
# TC    O(logn)
# SC    O(1)

def search(arr, value):
    start = 0
    end = len(arr)-1

    while start<=end:
        mid = start + (end - start) // 2
        # print(mid, start, end)
        if arr[mid] == value:
            return mid
        # Assuming array is in ascending order
        elif arr[mid]>value:
            end = mid - 1
        elif arr[mid]<value:
            start = mid + 1
    
    return -1

if __name__ == '__main__':
    a = [3, 5, 2323, 10000]
    print(search(a, 122222))