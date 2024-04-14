from django import forms
from django.forms import widgets

class CodeForm(forms.Form):
    code = forms.CharField(widget=widgets.Textarea, label='Код')
    stdinput = forms.CharField(widget=widgets.Textarea, label='Ввод', required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['is'] = 'highlighted-code'
        self.fields['code'].widget.attrs['language'] = 'python'

        self.fields['stdinput'].widget.attrs['placeholder'] = 'Рекомендуется ознакомится с особенностями использования.'