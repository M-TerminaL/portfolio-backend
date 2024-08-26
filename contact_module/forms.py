from django import forms
from django.core.validators import RegexValidator, MaxLengthValidator, EmailValidator


class ContactMeForm(forms.Form):
    full_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'placeholder': "نام و نام خانوادگی",
        'class': 'd-block p-1 ps-3 w-100 bg-transparent mb-3'
    }), validators=[MaxLengthValidator(50),
                    RegexValidator(regex=r'[\u0621-\u06cc\u00ab\u00bb\u060c\u061b]+',
                                   message='*نام و نام خانوادگی را به فارسی بنویسید')])
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={
        'placeholder': "ایمیل",
        'class': 'd-block p-1 ps-3 w-100 bg-transparent mb-3'
    }), validators=[EmailValidator(), MaxLengthValidator(100)])
    subject = forms.CharField(max_length=400, required=True, widget=forms.TextInput(attrs={
        'placeholder': "عنوان",
        'class': 'd-block p-1 ps-3 w-100 bg-transparent mb-3'
    }))
    text = forms.CharField(max_length=400, required=True, widget=forms.Textarea(attrs={
        'rows': '10'
    }))
