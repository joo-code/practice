from django.db import models

# ---------------------------------- [edit] ---------------------------------- #
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
# ---------------------------------------------------------------------------- #

class Hospital(models.Model):
    sido = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    medical = models.IntegerField()
    room = models.IntegerField()
    tel = models.CharField(max_length=15)
    address = models.CharField(max_length=100)