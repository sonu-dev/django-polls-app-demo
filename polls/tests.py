
from django.utils import timezone
from django.test import TestCase
import datetime

from .models import Question

# Create your tests here.

class QuestionMethodTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=5)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
