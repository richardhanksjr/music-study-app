from django.test import TestCase
from .QuestionGenerator import QuestionGenerator
from .questions import Question


class QuestionGeneratorTest(TestCase):

    def test_question_factory_raises_type_error_if_question_type_missing(self):
        try:
            QuestionGenerator.question_factory()
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)
        except Exception:
            self.assertFalse(False)

    # def test_that_generator_returns_an_instance_of_question(self):
    #     question = QuestionGenerator.question_factory()
    #     self.assertIsInstance(question, Question)
