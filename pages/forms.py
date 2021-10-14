from django import forms

class Attempt_Form(forms.Form):
    attempt = forms.CharField(label = '', max_length=200, )
    def clean_attempt(self):
        attempt_clean = self.cleaned_data.get("attempt")
        #for self.cleaned_data.get("attempt") - does "attempt refer to the instance of the form above?"
        if len(attempt_clean) > 50:
            raise forms.ValidationError("Your answer is too long - type less please :) ")
        
        
    
    