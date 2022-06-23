def reverse_str(str):
    if str == '':
        return ''
    return reverse_str(str[1:]) + str[0]


print(reverse_str('Hello'))
