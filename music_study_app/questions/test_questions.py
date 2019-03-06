from django.test import TestCase
from .QuestionGenerator import QuestionGenerator
from .questions.questions import Question
from .questions.major_scale_questions import SimpleScaleDegreeMajor


class QuestionGeneratorTest(TestCase):

    def test_that_question_factory_random_returns_an_instance_of_question(self):
        question = QuestionGenerator.question_factory()
        self.assertTrue(isinstance(question, Question))

    def test_given_question_type_returns_correct_instance(self):
        question = QuestionGenerator.question_factory(question_type='simple-interval-major')
        self.assertTrue(isinstance(question, SimpleScaleDegreeMajor))

    def test_question_has_a_question_string(self):
        question = QuestionGenerator.question_factory()
        self.assertIsInstance(question.question, str)


class SimpleScaleDegreeMajorTest(TestCase):

    def test_for_correct_question_string(self):
        # Check for the fifth scale degree of Bb Major
        question = SimpleScaleDegreeMajor('B-', 4)
        expected = "What is the fifth scale degree of B\u266D Major?"
        self.assertEqual(expected, question.question)
