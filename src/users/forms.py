from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        first_name = forms.CharField(max_length=255, required = True)
        las_name = forms.CharField(max_length = 255, required = True)
        fields = ['first_name','last_name','username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']