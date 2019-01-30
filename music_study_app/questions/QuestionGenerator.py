from .questions import Question


class QuestionGenerator:

    question_choices = {'simple-interval-major': SimpleIntervalMajor}

    @staticmethod
    def question_factory(question_type=None):
        if not question_type:
            raise TypeError('question_factory missing keyword argument question_type')

        # TODO get question based on the question_type and the question_choices dict above
        return Question()
