from django.db import models

class Idea(models.Model):
    id = models.CharField(max_length=5, primary_key=True)

    title = models.CharField(max_length=100)
    pitch = models.CharField(max_length=300, default='')

    creation_date = models.DateTimeField('date published')

    votes  = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
