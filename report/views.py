from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from . import services
# Create your views here.
def index(request):
	services.insertProduct()
	services.insertProductDetail()
	context = {'result': services.calcMinMaxAvg()}
	return render(request,'report/index.html',context)