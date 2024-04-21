from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')

class LiteratureLinks(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title
    

class Question(models.Model):
    CHOICES = (
        ('please', 'Просить'),
        ('refuse', 'Отказывать'),
        ('conflict', 'Конфликтовать'),
        ('opinion', 'Выражать мнение'),
        ('praise', 'Хвалить'),
        ('critisize', 'Критиковать'),
    )
    question = models.CharField(max_length=250)
    type = models.CharField(max_length=100, choices=CHOICES)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.FloatField(choices=[(0, '0'), (0.5, '0.5'), (1, '1')])

    def __str__(self):
        return self.choice_text
    