from django.shortcuts import redirect, render
from .forms import GradesForm
from .models import Grades
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def grades(request):
  if request.method == "POST":
    form = GradesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("grades")
    else:
      grades = Grades.objects.all()
      return render(request , "grades.html" , {"form":form , "grades":grades})
  form = GradesForm()
  grades = Grades.objects.all()
  return render(request , "grades.html" , {"form":form , "grades":grades})

@login_required
def deleteGrade(request , id):
  grade = Grades.objects.filter(id=id).first()
  grade.delete()
  return redirect("grades")

@login_required
def updateGrade(request , id):
  if request.method == "POST":
    grade = Grades.objects.filter(id=id).first()
    newForm = GradesForm(request.POST, instance=grade)
    if newForm.is_valid():
      newForm.save()
      return redirect("grades")
    else:
      return render(request , "gradeUpdateForm.html" , {"form":newForm})
  grade = Grades.objects.filter(id=id).first()
  return render(request , "gradeUpdateForm.html" , {"form":GradesForm(instance=grade)})