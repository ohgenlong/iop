from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(min_length=5)
    email = forms.EmailField()
    #email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message)
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
        