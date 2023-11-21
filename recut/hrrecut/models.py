from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    experience = models.IntegerField()
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
