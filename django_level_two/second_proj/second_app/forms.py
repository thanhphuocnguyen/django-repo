from django import forms

from second_app.models import User


class UserRegisterForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'