from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


from questions.questions.major_scale_questions import SimpleScaleDegreeMajor


class GetRandomQuestionTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_returns_correct_keys(self):
        expected_keys = ['question', 'answer_options',  'question_params']
        self.assertListEqual(expected_keys, list(self.client.get('/api/question').data.keys()))


class GetAnswerToQuestionTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test')
        self.client.force_authenticate(user=self.user)
        self.tonic = 'B-'
        # This is the fifth of Bb
        self.scale_degree_index = 4
        self.question = SimpleScaleDegreeMajor(tonic=self.tonic,
                                               scale_degree_index=self.scale_degree_index)
        self.question_type = self.question.question_type

    def test_returns_correct_answer(self):
        response = self.client.post('/api/answer', {'question_type': self.question_type,
                                                    'tonic': self.tonic,
                                                    'scale_degree_index': '4',
                                                    'user_answer': 'F'}, format='json')

        if response.status_code != 200:
            self.assertFalse(True)

        expected_response = {'correct_answer': self.question.answer,
                             'user_correct': True,
                             'question': self.question.question}
        self.assertDictEqual(expected_response, response.data)
