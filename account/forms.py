from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


        def save(self, commit =True):
            user =super().save(commit =False)
            full_name =self.cleaned_data['full_name']
            first_name, last_name = full_name.split('',1)
            user.first_name = first_name
            user.last_name = last_name
            if commit:
                user.save()
            return user
        
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)
            self.fields['full name'].widget.attrs.update(
                {'placeholder':'Enter full name', 'class':'form-control'}
            )
            self.fields['username'].widget.attrs.update(
                {'placeholder':'Enter username', 'class':'form-control'}
            )
            self.fields['full name'].widget.attrs.update(
                {'placeholder':'Enter full name', 'class':'form-control'}
            )