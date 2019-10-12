from django.db import models
class Choice(models.Model):
    place_name = models.CharField(max_length=200)
    place_no = models.IntegerField(default=0)
    def __str__(self):
        return self.place_name