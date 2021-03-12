from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.


def index(request):
    return render(request, "app/main.html")

def cars(request):

    cars = []

    cars.append({"make":"Lexus", "model":"NX200t", "year": 2017})
    cars.append({"make":"Toyota", "model":"Land Cruiser", "year": 2021})
    cars.append({"make":"Tesla", "model":"Model S", "year": 2018})

    return JsonResponse(cars, safe=False)

