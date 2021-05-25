#PF-Tryout

def generate_next_date(day,month,year):
    if(month == 4 or month == 6 or month == 9 or month == 11):
        if(day >= 1 and day < 30):
            day = day + 1
        else:
            if(day == 30):
                month += 1
                day = 1
    elif(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
        if(day >= 1 and day < 31):
            day += 1
        else:
            if(day == 31):
                month += 1
                day += 1
    elif( month == 12):
        if(day >= 1 and day < 31):
            day += 1
        else:
            if(day == 31):
                month = 1
                day = 1
                year += 1
    else:
        if(day >= 1 and day < 28):
            day += 1
        else:
            month += 1
            day = 1
        
        

    print(day,"-",month,"-","20"+str(year))


generate_next_date(1,9,15)