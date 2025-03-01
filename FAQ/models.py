from django.db import models

class FaqModel(models.Model):
    question = models.CharField()
    answer = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.answer
