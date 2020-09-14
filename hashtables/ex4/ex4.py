def has_negatives(a):
    table = {}
    for i in a:
        table[i] = True
    result = [i for i in a if i > 0 and table.get(i*-1)]
    return result

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
