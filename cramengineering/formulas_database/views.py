from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home(requests):
    context = {}

    return render(requests, "formulas_database/formulas-home.html", context)
