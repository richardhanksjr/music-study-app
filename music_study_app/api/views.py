from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from questions.QuestionGenerator import QuestionGenerator


class GetRandomQuestion(APIView):

    def get(self, request, format=None):
        question = QuestionGenerator.question_factory()
        return Response({'question': question.get_question(),
                         'answer_options': question.get_answer_options()})

