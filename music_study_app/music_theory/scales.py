class Scale:
    pass


class MajorScale(Scale):
    scale_degree = {
        1: {
            'name': 'tonic',
            'position_name': 'first'
        },
        2: {
            'name': 'super tonic',
            'position_name': 'second'
        },
        3: {'name': 'mediant',
            'position_name': 'third'
            },
        4: {
            'name': 'subdominant',
            'position_name': 'fourth'
        },
        5: {
            'name': 'dominant',
            'position_name': 'fifth'
        },
        6: {
            'name': 'submediant',
            'position_name': 'sixth'
        },
        7: {
            'name': 'leading tone',
            'position_name': 'seventh'
        }
    }

    @classmethod
    def diatonic_scale_degree(cls, scale_degree: int) -> dict:
        """
       :param scale_degree:  The number of the major scale degree to be searched for
       :return: A dictionary containing the information for the given scale degree
       """
        return cls.scale_degree[scale_degree]
