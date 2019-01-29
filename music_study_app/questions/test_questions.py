from django.test import TestCase
from .QuestionGenerator import QuestionGenerator
from .questions import Question


class QuestionGeneratorTest(TestCase):

    def test_that_generator_returns_an_instance_of_question(self):
        question = QuestionGenerator.random_question()
        self.assertIsInstance(question, Question)
