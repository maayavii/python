n = 5

# Increasing pattern
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

# Decreasing pattern
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')