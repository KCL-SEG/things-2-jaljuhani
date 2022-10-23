"""Forms of the project."""

from django import forms

class ThingForm(forms.Form):
    name=forms.CharField(label='Name',)
    description=forms.CharField(label='Description')
    quantity=forms.CharField(label='Quantity')





# Create your forms here.
