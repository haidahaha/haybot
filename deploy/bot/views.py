# -- coding: utf-8 --

from django.shortcuts import render
from django.http import JsonResponse
from pb_py import main as API
import os
from django.conf import settings
import forecastio
import random


def talk(request):
    context_dict = {}

    if request.method == 'GET':
        session_id = 's1'
        message = request.GET.get('query')
        result = API.talk(settings.AI_KEY, settings.AI_ID, settings.AI_HOST, settings.AI_NAME, message, session_id, recent=True)
        context_dict['response'] = result['response']

    return JsonResponse(context_dict, safe=False)


def greeting(request):
    context_dict = {}
    GREETINGS = [
        {"en": "Ahoy there", "fi": "Morjensta"},
        {"en": "Hey again", "fi": "Täällä jälleen"},
        {"en": "Welcome back", "fi": "Terve taas"},
        {"en": "It is time to tango", "fi": "Nonniin"},
        {"en": "Rise and shine", "fi": "Täältä pesee"},
        {"en": "Wakey wakey", "fi": "Se on lets gou nyt"},
    ]
    RAINS = [
        {"en": "It is raining, but let's do this!", "fi": "Siellä vissiin sataa, mutta ei anneta sen haitata!"},
        {"en": "A little pour never hurt anyone, so here we go.", "fi": "Foreca sanoo että vettä tulee, mutta mehän ei olla sokerista."},
        {"en": "Darn, it's wet. Anyway, here's an exercise", "fi": "Sataako siellä? Tässä sadetanssi!"},
    ]
    SNOWS = [
        {"en": "Oh god, where did spring go? Still, you gotta work out!", "fi": "Eiii, takatalvi! Siitä huolimatta, tässä jumppaa."},
        {"en": "Yay! Snow! I hope you'll stay indoors for the exercise.", "fi": "Nyt ilmeisesti tulee lunta. Kannattaa siis jumpata sisällä."},
        {"en": "Let's exercise and hope spring comes back.", "fi": "Tehdäänpä tämä liike ja toivotaan että kevät tulee takaisin."},
    ]
    CLEARS = [
        {"en": "Solar power!", "fi": " Wuhuu, aurinkovoimaa!"},
        {"en": "It's sunny! Let's go!", "fi": "Foreca kertoo että nyt paistaa! Täältä pesee!"},
        {"en": "I hope you can still see the screen from all the sunshine!", "fi": "Kirkasta! Toivottavasti näyttö näkyy yhä!"},
    ]
    message = ''

    if request.method == 'GET':
        language = request.GET.get('lang', 'en')

        message = "{0}{1}\n".format(random.choice(GREETINGS).get(language), random.choice(['.', '!']))
        longitude = request.GET.get('longitude', '')
        latitude = request.GET.get('latitude', '')
        if longitude and latitude:
            forecast = forecastio.load_forecast(settings.WEATHER_KEY, longitude, latitude)
            c = forecast.currently()
            print c.summary
            print c.icon
            print c.time
            print c.temperature
            if c.icon == "rain":
                message += "{0}\n".format(random.choice(RAINS).get(language),)
            elif c.icon == "snow":
                message += "{0}\n".format(random.choice(SNOWS).get(language),)
            elif c.icon == "clear-day":
                message += "{0}\n".format(random.choice(CLEARS).get(language),)

    context_dict['response'] = message
    return JsonResponse(context_dict, safe=False)


def doing(request):
    context_dict = {}
    DOINGS = [
        {"en": "Let's go, let's go!", "fi": "Jes, anna mennä!"},
        {"en": "That's the spirit. Let me know how it went when you finish", "fi": "Nonniin, tästä lähtee!"},
        {"en": "Do iiiit!", "fi": "Hyvä hyvä!"},
    ]
    message = ''

    if request.method == 'GET':
        language = request.GET.get('lang', 'en')
        message += "{0}\n".format(random.choice(DOINGS).get(language),)

    context_dict['response'] = message
    return JsonResponse(context_dict, safe=False)

def done(request):
    context_dict = {}
    DONES = [
        {"en": "Well done!", "fi" : " Loistavaa!"},
        {"en": "Rock n roll!", "fi" : "Rock n roll!"},
    ]
    message = ''

    if request.method == 'GET':
        language = request.GET.get('lang', 'en')
        message += "{0}\n".format(random.choice(DONES).get(language),)

    context_dict['response'] = message
    return JsonResponse(context_dict, safe=False)

def skipping(request):
    context_dict = {}
    SKIPPINGS = [
        {"en": "Okay, hope you can do it next time.", "fi": "No höh, toivottavasti seuraavalla kerralla onnistuu."},
        {"en": "Alright, till next time then!", "fi": "Ok, ensi kertaan siis!"},
        {"en": "Sure thing, enjoy the rest!", "fi": "Tokkiisa, nauti levosta!"},
    ]
    message = ''

    if request.method == 'GET':
        language = request.GET.get('lang', 'en')
        message += "{0}\n".format(random.choice(SKIPPINGS).get(language),)

    context_dict['response'] = message
    return JsonResponse(context_dict, safe=False)
