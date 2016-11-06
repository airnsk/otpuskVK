# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import json
from otpusk.logic import *
from main.models import zapros

def home(request):
    ua_string = request.META['HTTP_USER_AGENT'].lower()

    try:
        r=request.GET['user_id']

    except:
        r=request.META['REMOTE_ADDR']
    request.session['muserid'] =r
    c = {'ua': ua_string,}
    return render_to_response('main.html', c, context_instance=RequestContext(request))


def calculation(request):

    r=request.session['muserid']
    mprequest=json.loads(request.body)
    zarplata=      int(mprequest["zarplata"])
    mdStart=       mprequest["startDate"]
    mdEnd=         mprequest["endDate"]
    startYear=     mprequest["startYear"]
    endYear=       mprequest["endYear"]
    mprange=getyarrange(mdStart, mdEnd) #отрезок отпуска в номерах дней
    mpmonth=getmonth(mprange,startYear) #список месяцев отпуска

    z=zapros(muser_id=r,
             zarp_jan=zarplata,
             mdStart=mdStart,
             mdEnd=mdEnd,
             startYear=startYear,
             endYear=endYear
             )
    z.save()

    mpmonthyear=[]
    if startYear != endYear:
        for i, m in enumerate(sorted(mpmonth)):
            if i == m:
                mpmonthyear.append({'month': m, 'year': endYear, 'days': takelenmonth(m, endYear), 'firstday': takefirstday(m, endYear)})
            else:
                mpmonthyear.append({'month': m, 'year': startYear, 'days': takelenmonth(m, startYear), 'firstday': takefirstday(m, startYear)})
    else:
        for i, m in enumerate(sorted(mpmonth)):
            mpmonthyear.append({'month': m, 'year': endYear, 'days': takelenmonth(m, endYear), 'firstday': takefirstday(m, endYear)})

    viewotpusk = []

    for mpm in mpmonthyear:
        holidays,workDay =TakeYearDay(mpm['year'])
        otpusk_bez_prazdnikov_no_s_vihodnymy = takeDayOtpusk(mprange,holidays)
        rabdnyixdney=[x for x in set(xrange(mpm['firstday'], mpm['firstday']+mpm['days'])).intersection(workDay)]
        ostatokrabochihdney=len([x for x in set(rabdnyixdney).difference(mprange)])
        otpuskniedni=len([x for x in set(xrange(mpm['firstday'], mpm['firstday']+mpm['days'])).intersection(otpusk_bez_prazdnikov_no_s_vihodnymy)])
        cenarabdnya = zarplata/len(rabdnyixdney)
        summarabdey = cenarabdnya * ostatokrabochihdney
        cenaotpusknogodnya=int(zarplata/29.4)
        viewotpusk.append({ 'ostatokrabochihdney':ostatokrabochihdney,
                            'cenarabdnya':cenarabdnya,
                            'summarabdey':summarabdey,
                            'cenaotpusknogodnya':cenaotpusknogodnya,
                            'otpuskniedni':otpuskniedni,
                            'summaotpusknyx':otpuskniedni * cenaotpusknogodnya,
                            'numbermonth':mpm['month'],
                            'year':mpm['year'],
                            'lenotpusk':len(mpmonth),
                            'allotpusk':len(otpusk_bez_prazdnikov_no_s_vihodnymy)
        })

    response_data = {}

    try:
        response_data['message']=zarplata
        response_data['viewotpusk']=viewotpusk

    except:
        response_data['month']='nope'
        response_data['message']='NO'

    return HttpResponse(json.dumps(response_data),content_type="application/json")


