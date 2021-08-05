from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        subject = self.subject if len(self.subject) < 10 else self.subject[:10] + '...'
        return f"{self.pk}) {subject} on {self.create_date}"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        content = self.content if len(self.content) < 10 else self.content[:10] + '...'
        return f"{self.pk}) {content} on {self.create_date} / RE: {self.question}"
