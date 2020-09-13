from django.shortcuts import render,  get_object_or_404
from django.http import JsonResponse

from django.http import HttpResponse, HttpResponseNotFound
from .models import UserInfo
from .models import Product

USERID = "user_id"
ORDERID = "order_id"

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

def index(request):
    return HttpResponse("Kukkeliskuu")
