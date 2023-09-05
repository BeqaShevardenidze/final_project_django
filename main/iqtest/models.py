from django.db import models

# Create your models here.
class Score(models.Model):
    user = models.CharField(max_length=50, blank=False)
    score = models.IntegerField(blank=False)

    def __str__(self) -> str:
        return f'{self.user}  {self.score}'