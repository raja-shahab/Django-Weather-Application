from django.shortcuts import render
import requests
def get_weather(city):
    api_key = "ea038413c1bbc036651fa818d5269548";
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    return response.json()

def weather_view(request):
    weather_data = None
    city = request.GET.get('city')

    if city:
        weather_data = get_weather(city)

    context = {
        'weather_data' : weather_data,
        'city' : city
    }

    return render(request, 'home.html', context)