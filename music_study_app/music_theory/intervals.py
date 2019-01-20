class MajorIntervalMapping:
    interval_dict = {
        0: 'root',
        1: 'minor second',
        2: 'major second',
        3: 'minor third',
        4: 'major third',
        5: 'perfect fourth',
        6: 'tritone',
        7: 'perfect fifth',
        8: 'minor sixth',
        9: 'major sixth',
        10: 'minor seventh',
        11: 'major seventh',
        12: 'perfect octave'
    }



    @classmethod
    def interval(cls, num_half_steps: int) -> str:
        return cls.get_interval_from_half_steps(num_half_steps)

    @classmethod
    def get_interval_from_half_steps(cls, num_half_steps: int) -> str:
        key = num_half_steps % 12
        return cls.interval_dict[key]
