import datetime

from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
'''
class newTableName(models.Model):
    clmn_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.clmn_name
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('published date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    