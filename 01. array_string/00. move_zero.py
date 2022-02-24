def moveZeros(li):
    n = len(li)

    pointer = 0
    for item in li:
        if item != 0:
            li[pointer] = item
            pointer += 1

    for i in range(pointer, n):
        li[i] = 0

li = [1,0,2,5,0,5,2]
moveZeros(li)

print(li)