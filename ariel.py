from random import randint

is_valid = False
while is_valid == False:
    n = randint(100000000, 999999999)
    l = [int(i) for i in str(n)]
    lp = []
    checksum = 0
    for i in l:
        if l.index(i) % 2 == 0:
            pond = i * 1
        else:
            pond = i * 2
            if pond > 9:
                sum_p = 0
                p = [int(i) for i in str(pond)]
                for v in p:
                    sum_p += v

                pond = sum_p
        lp.append(pond)
        checksum += pond
    if checksum % 10 == 0:
        is_valid = True
        print('SIREN : ' + ' ' + str(n))
    else:
        pass
