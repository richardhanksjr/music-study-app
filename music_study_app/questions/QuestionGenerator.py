import random
from .questions.question_choices import question_choices


class QuestionGenerator:



    @staticmethod
    def question_factory(question_type=None):
        """
        Used to get a question.  If no question_type is given, returns a random question, else returns
        a question of the type given in the question_type key.
        :param question_type: The key of the Question subclass that we are to return
        :return: An instance of a Question
        """

        if not question_type:
            return question_choices[random.choice(list(question_choices.keys()))]

        return question_choices.get(question_type, None)
