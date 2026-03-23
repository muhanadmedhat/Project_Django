from django.shortcuts import render

from feedback.models import Feedback

# Create your views here.
def feedback(request):
  if(request.method == 'POST'):
    email = request.POST.get("email")
    message = request.POST.get("message")
    feedbackAdded = Feedback.objects.create(email=email , message=message)
  feedbacks = Feedback.objects.all()
  return render(request , "feedback.html" , {'feedbacks':feedbacks})