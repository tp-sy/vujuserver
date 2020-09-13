import pytz

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import UserInfo, Product, Song

from datetime import datetime, timedelta

USERID = "user_id"
ORDERID = "product_id"
SONGID = "song_id"
TIMESTAMP = "time"

def user_login(request):
    uid = request.GET.get(USERID)
    uinfo = get_object_or_404(UserInfo,
                              user_id__iexact=uid)
    uinfo.present = True
    uinfo.save()
    return HttpResponse("Ok")

def order(request):
    uid = request.GET.get(USERID)
    productid = request.GET.get(ORDERID)
    print(productid, type(productid))
    if not list(Product.objects.filter(drink_id__iexact=productid)):
        return HttpResponseNotFound("None")
    user = get_object_or_404(UserInfo,
                             user_id__iexact=uid)
    user.order_status = productid
    user.save()
    return HttpResponse("Ok")

def received_order(request):
    uid = request.GET.get(USERID)
    user = get_object_or_404(UserInfo,
                             user_id__iexact=uid)
    user.order_status = 0
    return HttpResponse("Ok")

def request_song(request):
    uid = request.GET.get(USERID)
    sid = request.GET.get(SONGID)
    tstamp = request.GET.get(TIMESTAMP)
    get_object_or_404(UserInfo, user_id__iexact=uid)
    if list(Song.objects.filter(tstamp__iexact=tstamp)):
        return HttpResponseNotFound("Time slot already taken")
    song = Song(song_id=sid, tstamp=tstamp, user_id=uid)
    song.save()
    return HttpResponse("Ok")

def get_upcoming_songs(request):
    uid = request.GET.get(USERID)
    get_object_or_404(UserInfo, user_id__iexact=uid)
    data = {'results': []}
    time = datetime.now(pytz.timezone("Europe/Helsinki"))
    songs = Song.objects.all()
    for song in songs:
        hour, minute = song.tstamp.split(":")
        try:
            hour = int(hour)
            minute = int(minute)
        except ValueError:
            return HttpResponseNotFound("Bad timestamps")
        songtime = time.replace(hour=hour, minute=minute)
        if songtime > (time - timedelta(minutes=6)):
            data['results'].append(
                {
                    "song_id": song.song_id,
                    "song_time": song.tstamp,
                    "user_id": song.user_id
                }
            )
    return JsonResponse(data)

def create_song(request):
    pass

def index(request):
    return HttpResponse("Kukkeliskuu")
