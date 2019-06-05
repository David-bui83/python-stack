# Selection Sort
myArr = [9,5,2,0,1,6,7,3,8]

def selection_sort(arr):

  for j in range(len(arr)):
    min_idx = j
    for i in range(j+1, len(arr)):
      if arr[min_idx] > arr[i]:
        min_idx = i
    temp = arr[j]
    arr[j] = arr[min_idx]
    arr[min_idx] = temp
  print(arr)
selection_sort(myArr)