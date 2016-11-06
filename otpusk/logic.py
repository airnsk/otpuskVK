
def TakeYearDay(Year):

    holidays = [1, 2, 3, 4, 5, 6, 7, 8, 54, 67, 121, 129, 163, 308]

    if Year == 2014:
        allday = 366 # all day in year +1
        smesh = 4 # smeshenie for first holiday
        perenesennyevyhodnye = [122, 164, 307] # perenesennye holydays

    if Year==2015:
        allday = 366
        smesh =3
        perenesennyevyhodnye = [9, 124]

    if Year == 2016:
        allday = 367
        smesh = 2
        perenesennyevyhodnye = [53, 67, 124]

    if Year == 2017:
        allday = 366
        smesh = 0
        perenesennyevyhodnye = [55, 128]

    vsevyhodnyevgodu = [x for x in set(xrange(smesh, allday, 7)).difference(range(-7,1)) ] +[x for x in xrange(smesh+1, allday, 7)]+perenesennyevyhodnye
    rabochiedni = [x for x in set(xrange(1, allday)).difference(holidays+vsevyhodnyevgodu)]

    return holidays, rabochiedni

def takeDayOtpusk(rangemp, holidays):
    otpusk_bez_prazdnikov_no_s_vihodnymy = [x for x in set(rangemp).difference(holidays)]
    return otpusk_bez_prazdnikov_no_s_vihodnymy


def months1 (year):

    month = [31, 28, 31,
              30, 31, 30,
              31, 31, 30,
              31, 30, 31]
    if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
        month[1] = 29
    return month

def inmonth(numberday,year):

    months = months1(year)
    i = 0
    while numberday > months[i]:
        numberday -= months[i]
        i += 1
    return i,months[i]

def takelenmonth(month,year):
    months = months1(year)
    return months[month]

def takefirstday(month,year):
    months = months1(year)
    firstday=1
    for i in range(1,month+1):
        firstday+=months[i-1]
    return firstday


def getyarrange(mdStart,mdEnd):
    if mdStart<mdEnd:
        return range(mdStart,mdEnd)
    else:
        return range(mdStart,366)+range(1,mdEnd)

def getmonth(mmrange,year):
    months = months1(year)
    otpuskmonth=[]
    a = 1
    for i in range(12):
        rx = range(a, months[i]+a)

        if filter(lambda x: x in rx, mmrange):
            otpuskmonth.append(i)
        a += months[i]
    return otpuskmonth

