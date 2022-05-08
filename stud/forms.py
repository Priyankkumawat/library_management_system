from dataclasses import fields
from django import forms
from .models import issuebook

class Issueform(forms.ModelForm):
    class Meta:
        model = issuebook
        fields=['name','mobile','enrollment','book','issue_date']
