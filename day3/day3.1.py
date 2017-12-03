def get_layer(number):
    i = 1
    while True:
        if i * i >= number:
            return(i - 2, i)
        i += 2

if __name__ == '__main__':
    lower, upper = get_layer(289326)
    print("{} -> {}".format(lower, upper))
    result = upper / 2
    count = lower * lower + 1
    step = 1
    for i in range(lower* lower + 1, upper * upper + 1):
        if count == 289326:
            break
        count += 1
        step += 1
    result += step % upper +1 - upper/2
    print(result)
