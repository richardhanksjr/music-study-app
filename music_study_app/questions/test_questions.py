from django.test import TestCase
from music21 import *
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

    def setUp(self):
        self.question = SimpleScaleDegreeMajor('B-', 4)

    def test_for_correct_question_string(self):
        # Check for the fifth scale degree of Bb Major
        question = self.question
        expected = "What is the fifth scale degree of B\u266D Major?"
        self.assertEqual(expected, question.question)

    def test_for_correct_answer(self):
        expected_answer = 'F'
        actual_answer = self.question.answer
        self.assertEqual(expected_answer, actual_answer)

    def test_for_correct_answer_options(self):
        # The length of the answer array should be 4
        self.assertEqual(4, len(self.question.answer_options))
        # All answers should be strings
        for answer in self.question.answer_options:
            if not isinstance(answer, str):
                self.assertFalse(True)
            else:
                self.assertTrue(True)
        # All the answers should be unique
        if len(list(set(self.question.answer_options))) != len(self.question.answer_options):
            self.assertFalse(True)
        else:
            self.assertTrue(True)
        # The correct answer should be in the list
        if 'F' in self.question.answer_options:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_for_correct_help_steps(self):
        root = pitch.Pitch('B-')
        expected_help = ({'prompt': 'What is the root of this key?', 'answer': root.unicodeName},)
        self.assertTupleEqual(expected_help, self.question.help_steps)

