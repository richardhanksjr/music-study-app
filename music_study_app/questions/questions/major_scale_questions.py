import random
from music21 import key
from .questions import Question
from ..utilities import (pitch_names, accidentals, scale_degrees, random_pitch, random_answer_options_pitch)


class SimpleScaleDegreeMajor(Question):


    def __init__(self, tonic=None, scale_degree_index=None):
        self.tonic = tonic
        self.scale_degree_index = scale_degree_index
        self.scale_degree = None
        self.question = None
        self.answer = None
        self.answer_options = None
        self.help_steps = None
        self.scale = None
        super().__init__()

    def generate_answer(self):
        scale = key.Key(self.tonic)
        self.answer = scale.pitches[self.scale_degree_index].unicodeName

    def generate_answer_options(self):
        self.answer_options = random_answer_options_pitch(correct_answer=self.answer)

    def generate_question(self):
        if not self.tonic:
            self.tonic = random_pitch()
        if not self.scale_degree_index:
            self.scale_degree_index = random.choice(range(8))
        self.scale_degree = scale_degrees[self.scale_degree_index]
        self.scale = key.Key(self.tonic)
        self.question = f"What is the {self.scale_degree['name']} scale degree " \
                        f"of {self.scale.getTonic().unicodeName} {self.scale.mode.capitalize()}?"

    def generate_help_steps_array(self):
        self.help_steps = ({'prompt': 'What is the root of this key?', 'answer': self.scale.getTonic().unicodeName},)


    def get_question(self):
        return self.question

    def get_answer_options(self):
        return self.answer_options

    def get_answer(self):
        return self.answer