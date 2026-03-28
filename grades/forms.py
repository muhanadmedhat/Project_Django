from django import forms
from .models import Grades
class GradesForm(forms.ModelForm):
  class Meta:
    model = Grades
    fields = "__all__"