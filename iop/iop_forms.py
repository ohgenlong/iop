from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(  
        required=True,  
        label=u"�û���",  
        error_messages={'required': '�������û���'},  
        widget=forms.TextInput(  
            attrs={  
                'placeholder':u"�û���",  
            }  
        ),  
    )      
    password = forms.CharField(  
        required=True,  
        label=u"����",  
        error_messages={'required': u'����������'},  
        widget=forms.PasswordInput(  
            attrs={  
                'placeholder':u"����",  
            }
        ),
    )  
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"�û���������Ϊ������")
        else:  
            cleaned_data = super(LoginForm, self).clean() 