def reader():
    with open('input') as f:
        line = f.readline().strip()
    return list(line)
