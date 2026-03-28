
from django.urls import include, path

from subjects.views import subject , deleteSubject , updateSubject

urlpatterns = [
    path('',subject,name="subject"),
    path('delete/<int:id>/' , deleteSubject , name="deleteSubject"),
    path('update/<int:id>/' , updateSubject , name="updateSubject"), 
]