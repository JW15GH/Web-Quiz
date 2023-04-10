from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer_a = models.CharField(max_length=200)
    answer_b = models.CharField(max_length=200)
    answer_c = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)
    question_number = models.PositiveIntegerField()

    def __str__(self):
        return self.question_text


    class Meta:
        app_label = 'ecm2434'

