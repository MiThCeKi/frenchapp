
from django.shortcuts import render
from django.http import HttpResponse
import inflect
from googletrans import Translator
import random

# Create your views here.

def index(request):
    p = inflect.engine()
    english_number = p.number_to_words(random.randint(1,50))
    print(type(english_number))
    print(english_number)
    translator = Translator()
    french_number = translator.translate(english_number, src='en', dest='fr')
    # french_number_text = french_number.text

    context = {
        'english_number': english_number,
        'french_number': french_number,
        }
    return render(request, 'index.html', context)