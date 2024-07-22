from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):

    username = forms.CharField(max_length=100, required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, required=True,  widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SingUpForm(forms.ModelForm):

    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_confirm = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username' ,'password']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}), 
            'password' : forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
  
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm :
            raise forms.ValidationError("passwords not valid")
        
        return cleaned_data
