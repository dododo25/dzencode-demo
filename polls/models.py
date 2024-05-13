from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    up_votes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=datetime.now())
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def clean(self):
        checked = [self]

        while checked[-1]:
            response_to = checked[-1].response_to

            if response_to and checked[0].id == response_to.id:
                raise ValidationError('Loop of comments detected!')

            checked.append(response_to)

        if self.response_to and self.creation_date < self.response_to.creation_date:
            raise ValidationError('Comment creation time cannot be set before it`s response comment creation time.')

    def __str__(self):
        return f'{self.commenter} - {self.creation_date} - {self.up_votes}'