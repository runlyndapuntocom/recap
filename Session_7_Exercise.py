s = "aceebdfz"
long = ''
solution = ''
pre = 'a'
for c in s:
    if c >= pre:
        solution = solution + c
    else:
        if len(solution) > len(long):
            long = solution
        solution = c
    pre = c
print(long)
