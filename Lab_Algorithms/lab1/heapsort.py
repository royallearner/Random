#Heap Sort
def heapify(arr, i):
    n =len(arr)
    root = i    
    l = 2 * i + 1    
    r = 2 * i + 2  

    if l < n and arr[l] > arr[root]:
        root = l

    if r < n and arr[r] > arr[root]:
        root = r

    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr, root)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i)
        print("Sorted array is:", arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap max to end
        heapify(arr, 0)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    print("Sorted array is:", arr)


######################
# import heapq

# arr = [12, 11, 13, 5, 6, 7]
# heapq.heapify(arr)
# print("Heapified array is:", arr)