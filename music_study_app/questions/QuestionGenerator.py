from music_theory.scales import MajorScale
from abc import ABC

class QuestionGenerator(ABC):


    @property
    def question(self) -> str:
        return self.generate_question()

    def generate_question(self) -> str:
        raise NotImplementedError


class SimpleIntervalMajorScale(QuestionGenerator):

    def __init__(self, root: str, interval_half_steps: int):
        super()
        self.root = root.upper()
        self.interval_half_steps = interval_half_steps

    def generate_question(self) -> str:
        interval_as_string = MajorScale.diatonic_scale_degree(5).position
        return f'What is the {interval_as_string} note of {self.root} Major?'

