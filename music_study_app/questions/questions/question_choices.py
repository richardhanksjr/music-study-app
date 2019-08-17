from .major_scale_questions import SimpleScaleDegreeMajor
from .minor_scale_questions import SimpleScaleDegreeMinor
from .SimpleQuestions import SimpleIntervalIs, InvertedQualityIs, TritoneIs

question_choices = {
    # 'simple-scale-degree-major': SimpleScaleDegreeMajor,
    #                 'simple-interval-is': SimpleIntervalIs,
    #                 'inverted-quality-is': InvertedQualityIs,
    #                 'simple-scale-degree-minor': SimpleScaleDegreeMinor
    'tritone-is': TritoneIs
}
