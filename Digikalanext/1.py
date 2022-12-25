def repeat_to_length(str, n):
    return (str * (n//len(str) + 1))[:n]


str='abcac'
n=10
print(repeat_to_length(str, n))
