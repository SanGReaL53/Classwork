def date_autumn(dates):
    my_list = []
    for date in dates:
        date = date.split('-')
        if date[0] == '11' or date[0] == '10' or date[0] == '9':
            my_list.append(date)
    date = my_list[0]
    maximum = int(date[0]) * 30 + int(date[1]) + int(date[2]) * 365
    for i in range(len(my_list)):
        if int(my_list[i][0]) * 30 + int(my_list[i][1]) \
            + int(my_list[i][2]) * 365 > maximum:
            maximum = int(my_list[i][0]) * 30 + \
                int(my_list[i][1]) + int(my_list[i][2]) * 365
            date = my_list[i]
    return '-'.join(date)

