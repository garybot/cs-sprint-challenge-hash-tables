
def finder(files, queries):
    table = {}

    for path in files:
        parts = path.split("/")
        
        if table.get(parts[-1]):
            table[parts[-1]].append(path)
        else:
            table[parts[-1]] = [path]

    result = []

    for val in queries:
        if table.get(val):
            result.extend(table.get(val))

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
