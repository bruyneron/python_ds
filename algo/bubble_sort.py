# TC - O(n^2)

def ascending_sort(a):
    n = len(a)

    for i in range(0, n):
        for j in range(0, n-1-i): 
            # (n-1)-i => n-1 becuase we are doing a[j] & a[j+1]. We don't want to go over the limit of j and get index out of range error.
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def descending_sort(a):
    n = len(a)

    for i in range(0, n):
        for j in range(0, n-1-i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

if __name__ == '__main__':
    arr = [23, 43, 541, 12, 1, 12, 323]
    print(arr)
    descending_sort(arr)
    print(arr)