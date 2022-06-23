def search_min_diff_element(arr, key):
  if arr[0] > key:
    return arr[0]
  if arr[-1] < key:
    return arr[-1]

  n = len(arr)
  start, end = 0, n-1

  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == key:
      return arr[mid]
    
    if arr[mid] > key:
      end = mid - 1

    if arr[mid] < key:
      start = mid + 1

  if abs(arr[start] - key) < abs(arr[end] - key):
    return arr[start]
  else:
    return arr[end]

def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()
