from django import forms

class Attempt_Form(forms.Form):
    attempt = forms.CharField(label = '', max_length=200, )
    def clean_attempt(self):
        attempt_clean = self.cleaned_data.get("attempt")
        if len(attempt_clean) > 10:
            raise forms.ValidationError("you're typing way too much - just a printed number please")
        
        
    
    