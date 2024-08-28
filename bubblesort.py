def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                v=arr[i]
                arr[i]=arr[j]
                arr[j]=v
    return arr
arr = []
m=int(input("Array Limit ="))
for i in range(m):
    b=int(input("Enter Array Element s="))
    arr.append(b)
print("Original Array =",arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
