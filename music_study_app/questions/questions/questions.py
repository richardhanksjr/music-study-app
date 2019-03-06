from abc import ABC


class Question(ABC):

    def __init__(self):
        self.generate_question()
        self.generate_answer()
        self.generate_answer_options()

    def question(self):
        raise NotImplementedError

    def generate_question(self):
        raise NotImplementedError

    def generate_answer(self):
        raise NotImplementedError

    def generate_answer_options(self):
        raise NotImplementedError