from django import forms
from .models import Student


class StudentLoginForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your name"}
        ),
    )
    grade = forms.ChoiceField(
        choices=Student.GRADE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
