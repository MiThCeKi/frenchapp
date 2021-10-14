
from django.shortcuts import render
import inflect
from googletrans import Translator
import random
from pages.forms import Attempt_Form

# Create your views here.
#######----Plan----#######
#1)It looks like I have to set up a dynamic URL in the main urls.py file. 
# This is set with <parameter name here> and also a type is specified before it. The
# syntax is <int: guessednumber> where guessednumber is the parameter.
#2)Then I have to make sure the name of this parameter is specified in the view. To
# do this this parameter is included as an argument along side the request.

# (a) There should be a submit button to put this in the url maybe?
# (b) Decided to use Django Forms and making progress but not completely understanding
# what is happenening yet. 

#3)This parameter should be saved in the database so it can be called on in the template.
# The purpose of calling on the guess is to show the student what they guessed vs the correct
# answer. There is some possibility that I'll create a username and password so users can
# have a record of their correct and incorrect answers. 
#4) I wonder if it would be cool to have record of correct guesses in their profile.

counter = 0
done_already = [1]
def index(request, datahere):
    global counter
    random_number = random.randint(1,50)
    print(random_number)
    form = Attempt_Form(request.POST)
    p = inflect.engine()
    english_number = p.number_to_words(random_number)
    translator = Translator()
    english_number = english_number.capitalize()
    french_number = translator.translate(english_number, src='en', dest='fr')
    french_number_text = french_number.text
    counter += 1
    
    #these parts are rendered in the webpage 
    context = {
        'datahere': datahere,
        'form':form,
        'english_number': english_number,
        'french_number_text': french_number_text,
        'counter': counter,
        }
    
    if request.method == 'POST':
        form = Attempt_Form(request.POST)
        if form.is_valid():
            print(f"the cleaned data is : {form.cleaned_data}")
            return render(request, 'index.html', context)
    else:
        form = Attempt_Form
        print(f"the french number is : {french_number_text}")
        return render(request, 'index.html', context)
        
    #this part generates the random number, the translation, and times played counter.
    
    return render(request, 'index.html', context)