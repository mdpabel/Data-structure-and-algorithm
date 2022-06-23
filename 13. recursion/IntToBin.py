def convertBin(n, res):
    if n == 0:
        return res

    res = str(n % 2) + res
    n = n // 2
    return convertBin(n, res)


if __name__ == "__main__":
    print(convertBin(5, ''))
