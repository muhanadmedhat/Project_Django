
from django.urls import path
from .views import grades , deleteGrade , updateGrade

urlpatterns = [
    path('',grades,name="grades"),
    path('delete/<int:id>/' , deleteGrade , name="deleteGrade"),
    path('update/<int:id>/' , updateGrade , name="updateGrade"),
]