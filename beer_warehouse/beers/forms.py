from django import forms
from django.core.exceptions import ValidationError

from models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'tax_number']

    def clean_name(self):
        data = self.cleaned_data['name']
        if data == "florida":
            raise ValidationError("That name is forbidden.")

        return data

    def clean(self):
        cleaned_data = super(CompanyForm, self).clean()
        name = self.cleaned_data.get('name')
        tax_number = self.cleaned_data.get('tax_number')

        if name == 'jaime' or tax_number == 0:
            raise ValidationError('Nombre o codigo prohibido', code='error')
        else:
            return cleaned_data