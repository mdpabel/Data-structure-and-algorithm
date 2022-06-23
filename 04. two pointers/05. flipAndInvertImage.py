class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for pixel in image:
            left = 0
            right = len(pixel) - 1
            
            while left <= right:
                if pixel[left] == pixel[right]:
                    if pixel[left] == 0:
                        pixel[left], pixel[right] = 1, 1
                    else:
                        pixel[left], pixel[right] = 0, 0
                left += 1
                right -= 1
                        
        return image