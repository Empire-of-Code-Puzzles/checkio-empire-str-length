from checkio_referee import RefereeBase


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "str_length"
    FUNCTION_NAMES = {
        "js_node": "strLength"
    }