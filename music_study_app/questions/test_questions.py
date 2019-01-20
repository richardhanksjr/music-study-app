from django.test import TestCase
from .QuestionGenerator import QuestionGenerator
from .QuestionGenerator import SimpleIntervalMajorScale


class QuestionTest(TestCase):

    def test_major_scale_degree_identification_question_format(self):
        question_generator = SimpleIntervalMajorScale('C', 5)
        expected_question_format = 'What is the fourth note of C Major?'
        actual_question_format = question_generator.question
        self.assertEqual(expected_question_format, actual_question_format)