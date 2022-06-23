def make_squares(arr):
  n = len(arr)
  squares = [0 for _ in range(n)]
  left = 0
  right = n -1 
  while left < right:
    left_sq = arr[left] * arr[left]
    right_sq = arr[right] * arr[right]

    if left_sq > right_sq:
      squares[n-1] = left_sq
      left += 1
    else:
      squares[n - 1] = right_sq
      right -= 1
    n -= 1
  
  return squares
