def intersection(arrays):
    counts = {}
    for array in arrays:
        for item in array:
            if counts.get(item):
                counts[item] += 1
            else:
                counts[item] = 1
    return [x for x in counts if counts[x] == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

