def b_sequences(n):
    if n == 0:
        return 0

    if n == 1:
        return 2

    if n == 2:
        return 3

    return b_sequences(n-1) + b_sequences(n-2)
