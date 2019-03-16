from django.test import TestCase
from rest_framework.test import APIClient


class GetRandomQuestionTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_returns_correct_keys(self):
        expected_keys = ['question', 'answer_options', 'question_type']
        self.assertListEqual(expected_keys, list(self.client.get('/api/question').data.keys()))
