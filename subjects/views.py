from django.shortcuts import redirect, render
from .forms import SubjectForm
from django.contrib.auth.decorators import login_required
from .models import Subject
# Create your views here.
@login_required 
def subject(request):
  if request.method == 'POST':
    form = SubjectForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("subject")
    else:
      subjects = Subject.objects.all()
      return render(request , "subject.html", {'form': form , 'allSubjects':subjects})
  form = SubjectForm()
  subjects = Subject.objects.all()
  return render(request , "subject.html", {'form': form , 'allSubjects':subjects})

@login_required
def deleteSubject(request,id):
  subject = Subject.objects.filter(id=id).first()
  subject.delete()
  return redirect("subject")

@login_required
def updateSubject(request,id):
  if request.method == "POST":
    subject = Subject.objects.filter(id=id).first()
    form = SubjectForm(request.POST,instance=subject)
    if form.is_valid():
      form.save()
      return redirect("subject")
    else:
      return render(request , "subjectCreateForm.html" , {'form':SubjectForm(instance=subject)})
  subject = Subject.objects.filter(id=id).first()
  return render(request , "subjectCreateForm.html" , {'form':SubjectForm(instance=subject)})