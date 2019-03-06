from django.test import TestCase
from .QuestionGenerator import QuestionGenerator
from .questions.questions import Question
from .questions.major_scale_questions import SimpleIntervalMajor


class QuestionGeneratorTest(TestCase):

    def test_that_question_factory_random_returns_an_instance_of_question(self):
        question = QuestionGenerator.question_factory()
        self.assertTrue(issubclass(question, Question))

    def test_given_question_type_returns_correct_instance(self):
        question = QuestionGenerator.question_factory(question_type='simple-interval-major')
        self.assertIs(question, SimpleIntervalMajor)

    def test_question_has_a_question_string(self):
        question = QuestionGenerator.question_factory()
        self.assertIsInstance(question().question(), str)
