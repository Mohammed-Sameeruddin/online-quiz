from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.TextField()
    option1 =  models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    answer = models.TextField()
    
    

