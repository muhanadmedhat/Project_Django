from django.db import models

from students.models import Student
from subjects.models import Subject

# Create your models here.
class Grades(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  subject = models.ForeignKey(Subject ,on_delete=models.CASCADE)
  degree = models.DecimalField(max_digits=5, decimal_places=2)

  class Meta:
        unique_together = ('student', 'subject')
        
  def __str__(self):
    return f"{self.student} - {self.subject} - {self.degree}"
