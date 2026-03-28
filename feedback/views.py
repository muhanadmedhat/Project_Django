from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feedback.models import Feedback

# Create your views here.
@login_required 
def feedback(request):
  if(request.method == 'POST'):
    email = request.POST.get("email")
    message = request.POST.get("message")
    feedbackAdded = Feedback.objects.create(email=email , message=message)
  feedbacks = Feedback.objects.all()
  return render(request , "feedback.html" , {'feedbacks':feedbacks})