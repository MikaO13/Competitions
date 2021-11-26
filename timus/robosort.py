n = int(input())
s = []

for i in range(n):
    s.append(int(input()))

def partition(arr, low, high):
    i = low-1 #index of the lower element
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1] # moving the pivot to the middle
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi-1) #recursively sorting
        quicksort(arr, pi+1, high)

def insertionSort(arr): 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 

#quicksort(s, 0, n-1)
insertionSort(s)
s.reverse()

for i in s:
    print(i)