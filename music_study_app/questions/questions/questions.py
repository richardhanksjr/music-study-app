from abc import ABC


class Question(ABC):

    def question(self):
        raise NotImplementedError
