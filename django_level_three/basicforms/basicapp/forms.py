from django import forms
from django.core import validators


def check_for_z(value: str):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Character Need to start with Z')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)])

    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if (len(bot_catcher)) > 0:
    #         raise forms.ValidationError("Gotcha bot")
    #     return bot_catcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email')
        vemail = all_clean_data.get('verify_email')
        if email != vemail:
            raise forms.ValidationError('Make sure email match')