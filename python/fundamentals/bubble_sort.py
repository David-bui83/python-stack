# Bubble Sort

myArr = [10,8,2,6,5,3,9,7,1,0]

def bubble_sort(arr):
  
  i = 0
  while i < len(arr) - 1:
    j = 0
    while j < len(arr) - 1 - i:
      if arr[j] < arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
      j+=1
    i+=1
  print(arr)

  # for j in range(len(arr)-1):
  #   for i in range(len(arr)-1):
  #     if arr[i] >  arr[i+1]:
  #       temp = arr[i]
  #       arr[i] = arr[i+1]
  #       arr[i+1] = temp
  # print(arr)
bubble_sort(myArr)