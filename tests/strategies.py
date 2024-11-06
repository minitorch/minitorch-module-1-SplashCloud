from hypothesis import settings
from hypothesis.strategies import floats, integers, composite
from typing import Callable, Tuple
import minitorch


settings.register_profile("ci", deadline=None)
settings.load_profile("ci")


small_ints = integers(min_value=1, max_value=3)
small_floats = floats(min_value=-100, max_value=100, allow_nan=False)
med_ints = integers(min_value=1, max_value=20)
posi_floats = floats(min_value=1e-6, max_value=100, allow_nan=False, exclude_min=True)


def assert_close(a: float, b: float) -> None:
    assert minitorch.operators.is_close(a, b), "Failure x=%f y=%f" % (a, b)


@composite
def ordered_triplets(draw: Callable) -> Tuple:
    a = draw(small_floats)
    b = draw(floats(min_value=a + 1, max_value=a + 200, allow_nan=False))
    c = draw(floats(min_value=b + 1, max_value=b + 200, allow_nan=False))
    return a, b, c
