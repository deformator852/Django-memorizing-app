from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    email = forms.EmailField(
        label="", widget=forms.EmailInput(attrs={"placeholder": "E-mail"})
    )
    password = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={"placeholder": "password"})
    )
    password2 = forms.CharField(
        label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"})
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password", "password2"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise ValidationError("Passwords don't match!")
        return cd["password"]

    def clean_email(self):
        User = get_user_model()
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("The such email exist!")
        return email
