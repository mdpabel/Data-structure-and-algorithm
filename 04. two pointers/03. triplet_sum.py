class Solution:
    def search_pair(self, arr, target, left, triplets):
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                triplets.append([target * -1, arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            if current_sum > target:
                right -= 1
            if current_sum < target:
                left += 1


    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        triplets = []
        
        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            target = arr[i] * -1
            self.search_pair(arr, target, i + 1, triplets)
            
        return triplets