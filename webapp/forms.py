from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

#Register / Create User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

#Record Form
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['firstname', 'lastname', 'email', 'phone', 'address', 'city', 'state', 'zip', 'country']
   
# Update Record Form
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['firstname', 'lastname', 'email', 'phone', 'address', 'city', 'state', 'zip', 'country']