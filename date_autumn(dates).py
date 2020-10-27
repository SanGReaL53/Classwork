def date_autumn(dates):
    b = []
    gd = []
    for x in dates:
        y = x.split('-')
        if y[0] == '09' or y[0] == '10' or y[0] == '11':
            z = int(y[1]) * 1000000 + int(y[0]) * 10000 + int(y[2])
            b.append(z)
            gd.append(x)
    for i in range(len(gd) - 1):
        if abs(b[i + 1] - 22102020) < abs(b[i] - 22102020):
            temp = b[i + 1]
            b[i + 1] = b[i]
            b[i] = temp
            d = gd[i + 1]
            gd[i + 1] = gd[i]
            gd[i] = d
    return gd[0]

