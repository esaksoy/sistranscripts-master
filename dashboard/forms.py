from django import forms
from . import models as dashboard_models


class YearForm(forms.Form):
    year = forms.ChoiceField(choices=dashboard_models.YEAR_CHOICES, label='Year',
                             widget=forms.Select(attrs={
                                 "placeholder": "",
                                 "class": "form-control"
                             })
                             )
