def partition(arr, s, e):
    pivot = arr[s]
    i=s+1
    j=e-1
    while (i <= j):
        while (i<=j and pivot >= arr[i]):
            # print(arr[i],"i",i)
            i = i + 1
        while (i<=j and pivot <=arr[j]):
            # print(arr[j],j)
            j = j - 1
        if (i <= j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[s], arr[j] = arr[j], arr[s]
            return j

def quicksort(arr, s, e):
    if len(arr) == 1:
        return arr
    if e-s>1:
        p = partition(arr, s, e)
        quicksort(arr, s, p)
        quicksort(arr, p + 1, e)
    return arr

n = int(input("enter the no. of elements:"))
arr = []
for i in range(n):
    a = int(input("enter the element:"))
    arr.append(a)
print(arr)
print("IN Progress")
print(partition(arr, 0, n))
print(arr)
print(quicksort(arr, 0, n))
print("END")
print("List in sorted form")
print(quicksort(arr,0,n))
#display top five score
print("Top five score:",arr[-5:n])
