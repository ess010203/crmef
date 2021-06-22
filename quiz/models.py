from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model



class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=70)
    image = models.ImageField()
    roll_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
     
 
 
    def __str__(self):
         return self.label
 
class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	label = models.CharField(max_length=100)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.label