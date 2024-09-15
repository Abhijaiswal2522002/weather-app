from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = 'http://api.weatherapi.com/v1/current.json?key=fe80b22d99bc4f0bbe8201104241209&q=' + city + '&aqi=no'
        source = urllib.request.urlopen(url).read()
        list_of_data = json.loads(source)

        # Print data to console for debugging
        print(list_of_data)

        data = {
            "location_name": list_of_data['location']['name'],
            "description": list_of_data['current']['condition']['text'],
            "temp": str(list_of_data['current']['temp_c']) + '°C',
            "pressure": str(list_of_data['current']['pressure_mb']) + ' mb',
            "humidity": str(list_of_data['current']['humidity']) + '%',
            "icon_url": 'http:' + list_of_data['current']['condition']['icon'],  # Ensure URL is complete
            "forecast_hour": [
                {"time": "Now", "icon": 'http:' + list_of_data['current']['condition']['icon'], "temp": list_of_data['current']['temp_c']}
            ]
        }

        return render(request, "main/index.html", {'data': data})
    
    return render(request, "main/index.html", {'data': None})
