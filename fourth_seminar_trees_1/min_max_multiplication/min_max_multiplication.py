def min_max_multiplication(data):
    if len(data) < 3:
        return -1

    min_index = 1
    max_index = 2

    for i in range(len(data)):
        if 2 * i + 1 > len(data):
            break

        min_index = 2 * i + 1

    for i in range(len(data)):
        if 2 * i + 2 >= len(data):
            break

        max_index = 2 * i + 2

    return data[min_index] * data[max_index]