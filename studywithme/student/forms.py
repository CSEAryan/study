from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label="Student Name")
    grade = forms.CharField(label="Grade")
