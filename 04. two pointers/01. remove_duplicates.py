def remove_duplicates(arr):
  n = len(arr)
  j = 0
  for i in range(1, n):
    if arr[i] != arr[i - 1]:
      arr[j] = arr[i]
      j += 1
  arr[j] = arr[n - 1]
  j += 1
  return j

