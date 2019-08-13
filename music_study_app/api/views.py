import json
from django.shortcuts import render
from django.http import QueryDict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from questions.QuestionGenerator import QuestionGenerator


class GetRandomQuestion(APIView):

    def get(self, request, format=None):
        question = QuestionGenerator.question_factory()
        return Response({'question': question.question,
                         'answer_options': question.answer_options,
                         'question_params': question.question_params})


class GetAnswerToQuestion(APIView):

    def post(self, request, format=None):
        request_dict = request.data
        # req_dict = request.data.copy()
        # request_dict = {}
        # for (key, value) in req_dict.items():
        #     if value.isdigit():
        #         request_dict[key] = int(value)
        #     else:
        #         request_dict[key] = value
        user_answer = request_dict.get('user_answer')
        try:
            del request_dict['user_answer']
        except KeyError:
            return Response({'Error': 'Missing user answer'}, status=status.HTTP_400_BAD_REQUEST)
        question = QuestionGenerator.question_factory(**request_dict)
        response_dict = {'correct_answer': question.answer,
                         'user_correct': user_answer == question.answer,
                         'question': question.question}
        return Response(response_dict)


class HelpSteps(APIView):
    def post(self, request, format=None):
        request_dict = request.data;
        # request_dict = request.data.copy()
        # request_dict = request.data.copy().dict()
        # # request_dict['question_type'] = request_dict['question_type'][0]
        # for (key, value) in request_dict.items():
        #     if value.isdigit():
        #         request_dict[key] = int(value[0])
        #     else:
        #         request_dict[key] = value

        question = QuestionGenerator.question_factory(**request_dict)
        response = list(question.help_steps)
        return Response(response)
