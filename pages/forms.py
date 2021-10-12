from django import forms

class Attempt_Form(forms.Form):
    attempt = forms.CharField(max_length=200)
    def clean_attempt(self):
        attempt = self.cleaned_data.get("attempt")
        if len(attempt) > 10:
            raise forms.ValidationError("you're typing way too much - just a printed number please")
        
        
    
    