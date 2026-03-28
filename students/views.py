from django.shortcuts import redirect, render
from students.models import Student
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
# Create your views here.

@login_required 
def student(request):
  if(request.method == "POST"):
    name = request.POST.get("name")
    age=request.POST.get("age")
    email=request.POST.get("email")
    imagepath=request.FILES.get("image")
    student = Student.objects.create(name=name,age=age,email=email,image=imagepath)
  students = Student.objects.all()
  context = {'all_students': students} 
  return render(request, "students.html", {'all_students': students})
 
@login_required  
def deleteStudent(request,id):
  student = Student.objects.get(id=id)
  student.delete()
  students = Student.objects.all()
  return redirect("student")

@login_required  
def updateStudent(request,id):
  if request.method == "POST":
    studentData = Student.objects.filter(id=id).first()
    form = StudentForm(request.POST,request.FILES,instance=studentData)
    if form.is_valid():
      form.save()
      return redirect("student")
    else:
      form = StudentForm(instance=studentData)
      return render(request , "form.html" , {"form":form})
  studentData = Student.objects.filter(id=id).first()
  form = StudentForm(instance=studentData)
  return render(request, "form.html", {"form": form})
  
  