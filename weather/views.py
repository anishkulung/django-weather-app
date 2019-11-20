from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import requests
from .models import City 
from .forms import CityForm
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=024999d595bb257de136477fb55acc00'
    #City is global varible and city is local varible
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city))#request the API data and convert the JSON to Python data types
        print(r.text) #print JSON file in terminal
        city_weather = r.json()
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'weather/index.html',context)