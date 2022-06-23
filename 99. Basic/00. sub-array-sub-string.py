""" 
nums[0:1+0] -> 1
nums[1:1+1] -> 2
nums[2:1+2] -> 3

nums[0:2+0] => 1,2
nums[1:2+1] -> 2,3

"""


def generateSubArray(array):
    n = len(array)

    for l in range(1, n+1):
        for i in range(n - l + 1):
            print(array[i:l+i])


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    generateSubArray(nums)

    str = 'abcd'
    generateSubArray(str)
