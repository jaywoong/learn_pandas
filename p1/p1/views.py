import json
import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import myanalysis.p108
from myanalysis.part4 import P109


def home(request):
    return render(request, 'home.html')

def c1(request):
    return render(request, 'c1.html')

def c1data(request):
    data = myanalysis.p108.P108().p108()
    print(data)
    return HttpResponse(json.dumps(data), content_type='application/json');

def iots(request):
    speed = request.GET['speed']
    rpm = request.GET['rpm']
    temp = request.GET['temp']
    logger = logging.getLogger('users')
    logger.debug(',' + speed + ',' + rpm + ',' + temp)
    return render(request, 'iotsresult.html')

def jpgs(request):
    P109().mat01()
    return render(request, 'jpgs.html')

def maps(request):
    P109().mat07()
    return render(request, 'seoul_map.html')