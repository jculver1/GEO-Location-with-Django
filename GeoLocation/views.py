from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/128.177.113.102?access_key=8c4dd55d5364d50bb49314b9a31b3969&format=1')
    geodata = response.json()
    print(geodata)
    return render(request, 'home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    })