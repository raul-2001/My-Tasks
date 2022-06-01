from django.db import models



class List(models.Model):
    title = models.CharField(max_length=250)
    complet = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title