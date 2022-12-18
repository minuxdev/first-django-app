from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    remember = forms.BooleanField(widget=forms.CheckboxInput, required=False)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255, widget=forms.EmailInput)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    check_password = forms.CharField(max_length=255, widget=forms.PasswordInput)
