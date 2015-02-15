from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(  
        required = True,  
        label = u"Username",  
        error_messages = {'required': 'please input the username'},  
        widget = forms.TextInput(  
            attrs={  
                'placeholder':u"Username",  
            }  
        ),  
    )      
    password = forms.CharField(  
        required = True,  
        label = u"password",  
        error_messages = {'required': u'please input the password'},  
        widget = forms.PasswordInput(  
            attrs={  
                'placeholder':u"password",  
            }
        ),
    )  
    def clean(self):  
        if not self.is_valid():  
            raise forms.ValidationError(u"Username and password must not null!")
        else:  
            cleaned_data = super(LoginForm, self).clean()
    
    
class LoginForm_old(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']