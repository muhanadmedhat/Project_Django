from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
  class Meta:
      model = Student
      fields = "__all__"

class LoginForm(forms.Form):
  email = forms.EmailField()
  password = forms.PasswordInput()