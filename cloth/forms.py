from django import forms
from . import models


class OrderClForm(forms.ModelForm):
    class Meta:
        model = models.OrderCl
        fields = "__all__"
