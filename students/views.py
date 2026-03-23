from django.shortcuts import redirect, render

from students.models import Student

# Create your views here.
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

def deleteStudent(request,id):
  student = Student.objects.get(id=id)
  student.delete()
  students = Student.objects.all()
  return redirect("student")