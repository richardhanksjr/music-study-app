from abc import ABC


class Question(ABC):

    def __init__(self):
        self.generate_question()
        self.generate_answer()
        self.generate_answer_options()
        self.generate_help_steps_array()

    def generate_question(self):
        raise NotImplementedError

    def generate_answer(self):
        raise NotImplementedError

    def generate_answer_options(self):
        raise NotImplementedError

    def generate_help_steps_array(self):
        raise NotImplementedError

    @property
    def question(self):
        raise NotImplementedError

    @property
    def answer_options(self):
        raise NotImplementedError

    @property
    def answer(self):
        raise NotImplementedError


