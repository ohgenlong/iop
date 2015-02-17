from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from website.models import TaskList

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
        
        
        
class TaskForm(ModelForm):
    class Meta:
        model = TaskList
        fields = ['name','description','created_by','task_type','hosts','content','groups','kick_off_at']
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['hosts'].widget.attrs.update({'class' : 'form-control','placeholder':'Hosts'})
        self.fields['groups'].widget.attrs.update({'class' : 'form-control','placeholder':'Groups'})
        self.fields['task_type'].widget.attrs.update({'class' : 'form-control','placeholder':'Task Type'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control','placeholder':'Task Description','rows':3})
        self.fields['name'].widget.attrs.update({'class' : 'form-control','placeholder':'Task Name'})
        self.fields['content'].widget.attrs.update({'class' : 'form-control','placeholder':'Task Content','rows':3})
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        