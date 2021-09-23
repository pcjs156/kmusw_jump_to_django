from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    view_count = models.IntegerField(null=False, blank=False, default=0, verbose_name='조회수')

    FIELD_CHOICES = (
        ('BE', '백엔드'),
        ('FE', '프론트엔드')
    )
    FIELD_MAX_LENGTH = max(map(len, map(lambda e: e[0], FIELD_CHOICES)))
    field = models.CharField(choices=FIELD_CHOICES, null=False, blank=False,
                             max_length=FIELD_MAX_LENGTH, verbose_name='질문 분야')

    def __str__(self):
        subject = self.subject if len(self.subject) < 10 else self.subject[:10] + '...'
        return f"{self.pk}) {subject} on {self.create_date}"


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        content = self.content if len(self.content) < 10 else self.content[:10] + '...'
        return f"{self.pk}) {content} on {self.create_date} / RE: {self.question}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
