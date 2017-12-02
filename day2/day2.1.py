def reader(filename):
    with open(filename) as f:
        for line in f:
            yield line

if __name__ == '__main__':
    r = reader('input_file')
    suma = 0
    while True:
        try:
            row = r.next().split()
            row = map(int, row)
        except StopIteration:
            break
        max_val = max(row) 
        min_val = min(row) 
        suma += max_val - min_val
    print(suma)
