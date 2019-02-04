from random import randint

is_valid = False

while is_valid == False:
    n = randint(100000000, 999999999)
    l = [int(i) for i in str(n)]
    checksum = []
    for i in l:
        if l.index(i) % 2 == 0:
            value = i * 1
        else:
            value = i * 2
            if value > 9:
                value += -9
        checksum.append(value)
    if sum(checksum) % 10 == 0:
        is_valid = True
        print('SIREN : ' + ' ' + str(n))
