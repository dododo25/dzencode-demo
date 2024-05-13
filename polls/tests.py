from datetime import timedelta

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.test import TestCase

from .models import *


class CommentTestCase(TestCase):

    u1, u2, u3 = None, None, None

    def setUp(self):
        self.u1 = User.objects.create_user(username='alice', email='alice@example.org', password='alice_passw0rd')
        self.u2 = User.objects.create_user(username='bob', email='bob@example.org', password='bob_passw0rd')
        self.u3 = User.objects.create_user(username='cailey', email='cailey@example.org', password='cailey_passw0rd')

    def test_create_comments(self):
        c1 = Comment.objects.create(commenter=self.u1, content='Alice comment')
        c2 = Comment.objects.create(commenter=self.u2, content='Bob response comment to Alice`s comment', response_to=c1)
        Comment.objects.create(commenter=self.u3, content='Cailey response comment to Cailey`s comment', response_to=c2)

    def test_create_comments(self):
        c1 = Comment.objects.create(commenter=self.u1, content='Alice comment')
        c2 = Comment.objects.create(commenter=self.u2, content='Bob response comment to Alice`s comment', response_to=c1)
        c3 = Comment.objects.create(commenter=self.u3, content='Cailey response comment to Cailey`s comment', response_to=c2)

        self.assertEqual(0, c1.up_votes)
        self.assertEqual(0, c2.up_votes)
        self.assertEqual(0, c3.up_votes)
        self.assertIsNotNone(c1.creation_date)
        self.assertIsNotNone(c2.creation_date)
        self.assertIsNotNone(c3.creation_date)

    def test_create_comments_should_throw_exception_when_loop_of_comments_detected(self):
        c1 = Comment.objects.create(commenter=self.u1, content='Alice comment')
        c2 = Comment.objects.create(commenter=self.u2, content='Bob response comment to Alice`s comment', response_to=c1)
        c3 = Comment.objects.create(commenter=self.u3, content='Cailey response comment to Cailey`s comment', response_to=c2)

        c1.response_to = c3

        with self.assertRaises(ValidationError):
            c1.clean()

    def test_create_comments_should_throw_exception_when_creation_date_invalid(self):
        c1 = Comment.objects.create(commenter=self.u1, content='Alice comment')
        c2 = Comment.objects.create(commenter=self.u2, content='Bob response comment to Alice`s comment', response_to=c1)

        c2.creation_date = c1.creation_date - timedelta(days=1)

        with self.assertRaises(ValidationError):
            c2.clean()