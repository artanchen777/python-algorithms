def F(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        return 3

    a = 0
    b = 1
    c = 3

    for _ in range(3, n + 1):

        new = a + b + c

        a = b
        b = c
        c = new

    return c