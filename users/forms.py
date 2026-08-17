from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField 
GENDER = (
    ("M", "M"),
    ("Ж", "Ж")
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=15, required=False, initial='+996')
    gender = forms.ChoiceField(choices=GENDER, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    captcha = CaptchaField() 

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'photo',
            'phone_number',
            'gender',
            'birth_date',
            'captcha', 
        )
    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user