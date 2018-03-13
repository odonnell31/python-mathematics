from decile import decile
from elfi import elfi
from mean import mean
from median import median
from ordinal_rank import ordinal_rank
from per_capita import per_capita
from per_sqmi import per_sqmi
from percentage_change import percentage_change
from percentage import percentage
from percentile import percentile
from standard_deviation import standard_deviation

from sys import modules

# These require Django
if 'django' in modules:
    from competition_rank import competition_rank
    from random_point import random_point
    from mean_center import mean_center
    from nudge_points import nudge_points
    from standard_deviation_distance import standard_deviation_distance
    from standard_deviation_ellipses import standard_deviation_ellipses
