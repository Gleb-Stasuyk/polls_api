from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(_('название опроса'), max_length=4096)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}/'


class Question(models.Model):
    class ANSWER_CHOICES(models.TextChoices):
        TEXT = 'text',
        ONE_CHOICE = 'radio',
        MULTIPLE_CHOICES = 'checkbox'

    question_text = models.CharField(_('вопрос'), max_length=4096)
    pub_date = models.DateField(auto_now_add=True, blank=True, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    choice_type = models.CharField(max_length=20, choices=ANSWER_CHOICES.choices, default=ANSWER_CHOICES.TEXT)


    def __str__(self):
        return self.question_text



class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='choices', blank=True, null=True)
    text = models.CharField(max_length=4096)
    is_correct = models.BooleanField(default=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='answer')
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choices = models.ManyToManyField(Choice)
    created = models.DateTimeField(auto_now_add=True)
    answer_text = models.CharField(max_length=4096, blank=True, null=True)

    def __str__(self):
        return ' USER № ' + str(self.user.id) + self.question.question_text
