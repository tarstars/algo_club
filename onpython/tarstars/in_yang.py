for p in range(-23, 24):
    for q in range(-23, 24):
        dp1, dq1 = p - 10, q
        dp2, dq2 = p + 10, q
        ds1 = dp1 ** 2 + dq1 ** 2
        ds2 = dp2 ** 2 + dq2 ** 2
        c1 = ds1 <= 100
        c2 = ds2 <= 100
        c3 = (p**2 + q**2) < 400
        c4 = (p**2 + q**2) < 529
        c5 = (p - 10)**2 + q**2 <=16
        c6 = (p + 10)**2 + q**2 <=16
        
        if ((c2 or ((q > 0) and c3 and not c1)) or (not c3 and c4)) and not c6 or c5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
