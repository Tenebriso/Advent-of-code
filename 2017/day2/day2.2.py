def reader(filename):
    with open(filename) as f:
        for line in f:
            yield line

def find_evenly_divisible_values(row):
    n = len(row)
    for i in range(n):
        for j in range(i + 1, n):
            if row[i] % row[j] == 0:
                return row[i] / row[j]
            elif row[j] % row[i] == 0:
                return row[j] / row[i]

if __name__ == '__main__':
    r = reader('input_file')
    suma = 0
    while True:
        try:
            row = r.next().split()
            row = map(int, row)
        except StopIteration:
            break
        suma += find_evenly_divisible_values(row)
    print(suma)
