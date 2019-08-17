from django.test import TestCase
from ..questions.SimpleQuestions import InvertedQualityIs, SimpleIntervalIs
from rest_framework.test import APIRequestFactory


class SimpleIntervalIsTest(TestCase):
    def setUp(self):
        self.question = SimpleIntervalIs()

    def test_question_params(self):
        expected_params = {'question_type': "simple-interval-is"}
        actual_params = self.question.question_params
        self.assertDictEqual(expected_params, actual_params)


class InvertedQualityIsTest(TestCase):

    def setUp(self):
        self.question = InvertedQualityIs(interval_quality='perfect', same=True)
        self.question_false = InvertedQualityIs(interval_quality='perfect', same=False)
        self.question_major_true = InvertedQualityIs(interval_quality='major', same=True)

    def test_for_correct_question_str(self):
        expected_question = "If a perfect interval is inverted it remains perfect"
        self.assertEqual(expected_question, self.question.question)

    def test_for_correct_question_str_same_is_false(self):
        expected_question = "If a perfect interval is inverted it does NOT remain perfect"
        self.assertEqual(expected_question, self.question_false.question)

    def test_for_correct_answer(self):
        expected_answer = "True"
        actual_answer = self.question.answer
        self.assertEqual(expected_answer, actual_answer)

    def test_for_correct_answer_not_same(self):
        expected_answer = "False"
        actual_answer = self.question_false.answer
        self.assertEqual(expected_answer, actual_answer)

    def test_for_answer_options(self):
        expected_answers = ["True", "False"]
        self.assertEqual(expected_answers, self.question.answer_options)

    def test_question_type(self):
        expected_type = 'inverted-quality-is'
        actual_type = self.question.question_type
        self.assertEqual(expected_type, actual_type)

    def test_question_params(self):
        expected_params = {'question_type': "inverted-quality-is",
                           'same': True,
                           'interval_quality': 'perfect'}
        actual_params = self.question.question_params
        self.assertEqual(expected_params, actual_params)

    def test_help_steps(self):
        expected_steps = ({'prompt': 'How are interval qualities affected by inversion?',
                           'answer': 'Perfect -> Perfect, Major -> minor, minor -> Major, diminished '
                                     '-> Augmented, Augmented -> diminished'}, )
        actual_steps = self.question.help_steps
        self.assertEqual(expected_steps, actual_steps)

    def test_correct_answer_major_true(self):
        expected_answer = "False"
        print(self.question_major_true.question)
        actual_answer = self.question_major_true.answer
        self.assertEqual(expected_answer, actual_answer)
