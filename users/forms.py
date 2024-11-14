from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  # Add email or any other fields you need
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Use set_password instead of make_password
        if commit:
             user.save()
        return user

    
