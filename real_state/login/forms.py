from django import forms

class EmailLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'placeholder': 'Enter your email',
            'required': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'placeholder': 'Enter your password',
            'required': True,
        })
    )