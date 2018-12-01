
def count_passphrases(filename):
    count = 0
    with open('input_file') as f:
        for line in f:
            if len(set(line.strip().split())) == len(line.strip().split()):
                count += 1
    return count

if __name__ == '__main__':
    print(count_passphrases('input_file'))
