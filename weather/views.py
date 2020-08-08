from django.shortcuts import render
from .models import ForecastModel

# Create your views here.
def index(request):
    import json
    import requests

    if request.method == "POST":
        params = {
            'access_key': '6b29899627a709d4c44fe454c00676a5',
            'query': request.POST['city']
        }

        api_result = requests.get('http://api.weatherstack.com/current', params)

        try:
            api = json.loads(api_result.content)
        except Exception as e:
            api = "Error"
        return render(request, 'weather/index.html', {'api': api})

    else:
        return render(request, 'weather/index.html', {'city': 'Please enter the correct city'})

# for forecast
def forecast(request):
    import requests
    import json
    # dates for the week
    from datetime import datetime, timedelta
    d0 = datetime.now()
    d1 = d0 + timedelta(days=1)
    d2 = d1 + timedelta(days=1)
    d3 = d2 + timedelta(days=1)
    d4 = d3 + timedelta(days=1)
    d5 = d4 + timedelta(days=1)
    d6 = d5 + timedelta(days=1)
    d7 = d6 + timedelta(days=1)

    d0, d1, d2, d3, d4, d5, d6, d7 = d0.strftime('%d/%m/%Y'), d1.strftime('%d/%m/%Y'), d2.strftime('%d/%m/%Y'), d3.strftime('%d/%m/%Y'), d4.strftime('%d/%m/%Y'), d5.strftime('%d/%m/%Y'), d6.strftime('%d/%m/%Y'), d7.strftime('%d/%m/%Y')

    # api looping
    key = "efed36b5e33d24fdb6ca3336edfee5a4"
    # list of cities with latitude and longitude
    city = ForecastModel.objects.values()
    # loop through the cities and get temp and weather desc
    temp_output = []
    weather_output = []
    city_output = []
    for c in range(len(city)):
        lat = city[c]["lat"]
        lon = city[c]["lon"]
        name = city[c]["city"]
        api_result = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,current,minutely&units=metric&appid={key}")
        if api_result:
            try:
                api = json.loads(api_result.content)
                temp = []
                weather = []
                for v in range(len(api['daily'])):
                    temp.append(api['daily'][v]['temp']['day'])
                    weather.append(api['daily'][v]['weather'][0]['main'])
            except Exception as e:
                api = "Error"
        temp_output.append(temp)
        weather_output.append(weather)
        city_output.append(name)
    return render(request, 'weather/forecast.html', {'api': api,
                                                     'temp': temp,
                                                     'weather': weather,
                                                     'd0': d0,
                                                     'd1': d1,
                                                     'd2': d2,
                                                     'd3': d3,
                                                     'd4': d4,
                                                     'd5': d5,
                                                     'd6': d6,
                                                     'd7': d7,
                                                     'city': city_output,
                                                     'lat': lat,
                                                     'temp_output': temp_output,
                                                     'weather_output': weather_output})


