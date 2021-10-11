
from django.shortcuts import render
from django.http import HttpResponse
import inflect
from googletrans import Translator
import random

# Create your views here.
counter = 0
done_already = [1]

def index(request):
    global counter
    random_number = random.randint(1,50)
    print(random_number)
    p = inflect.engine()
    english_number = p.number_to_words(random_number)
    translator = Translator()
    english_number = english_number.capitalize()
    french_number = translator.translate(english_number, src='en', dest='fr')
    french_number_text = french_number.text
    counter += 1
    context = {
        'english_number': english_number,
        'french_number_text': french_number_text,
        'counter': counter,
        }
    return render(request, 'index.html', context)