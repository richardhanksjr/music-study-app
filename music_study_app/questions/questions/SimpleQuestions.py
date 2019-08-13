from .questions import Question


class SimpleIntervalIs(Question):

    def __init__(self, **kwargs):
        self._answer_options = None
        self._question = None
        self._answer = None
        self._help_steps = None
        super().__init__()

    def _generate_answer(self):
        self._answer = "An interval that encompasses an octave or less"

    def _generate_answer_options(self):
        self._answer_options = ["A perfect interval", "A Major or minor interval",
                                "An interval that encompasses an octave or less",
                                "A consonant interval"]

    def _generate_help_steps_array(self):
        self._help_steps = ({'prompt': 'What is a simple interval?',
                             'answer': 'an interval of one octave or less.'}, )


    @property
    def question(self):
        return self._question

    @property
    def answer_options(self):
        return self._answer_options

    @property
    def answer(self):
        return self._answer

    @property
    def question_type(self):
        return "simple-interval-is"
    @property
    def question_params(self):
        return {'question_type', self.question_type}

    @property
    def help_steps(self):
        return self._help_steps

    def _generate_question(self):
        self._question = "A SIMPLE INTERVAL is: "
