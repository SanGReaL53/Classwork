def date_autumn(dates):
    ml = []
    for day in dates:
        day = day.split('-')
        if day[0] == '11' or day[0] == '10' or day[0] == '9':
            ml.append(day)
    day = ml[0]
    maximum = int(day[0]) * 30 + int(day[1]) + int(day[2]) * 365
    for i in range(len(ml)):
        if int(ml[i][0]) * 30 + int(ml[i][1]) \
                + int(ml[i][2]) * 365 > maximum:
            maximum = int(ml[i][0]) * 30 + \
                int(ml[i][1]) + int(ml[i][2]) * 365
            day = ml[i]
    return '-'.join(day)
