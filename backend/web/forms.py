from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from backend.core.forms import BaseStyledForm


class LoginUserForm(AuthenticationForm, BaseStyledForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SignupUserForm(BaseStyledForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Введите пароль еще раз", widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Необязательно"}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Пароли не совпадают")

        return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
