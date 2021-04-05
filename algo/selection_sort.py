# TC - O(n^2)

def ascending_sort(arr):
    n = len(arr)
    
    for i in range(0, n):
        largest_number_index = 0
        for j in range(0, n-i):
            if arr[j] > arr[largest_number_index]:
                largest_number_index = j
        
        # temp = arr[n-1-i]
        # arr[n-1-i] = arr[largest_number_index]
        # arr[largest_number_index] = temp
        arr[largest_number_index], arr[n-1-i] = arr[n-1-i], arr[largest_number_index]
        #print(arr)


def descending_sort(a):

    n = len(a)

    for i in range(0, n):
        max_num_index = i
        for j in range(i+1, n):
            if a[j] > a[max_num_index]:
                max_num_index = j

        a[i], a[max_num_index] = a[max_num_index], a[i]

if __name__ == '__main__':
    arr = [23, 43, 541, 12, 1, 12, 323]
    print(arr)
    ascending_sort(arr)
    print(arr)
    arr = [23, 43, 541, 12, 1, 323]
    print(arr)
    descending_sort(arr)
    print(arr)


                
