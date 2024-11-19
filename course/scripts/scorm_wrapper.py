from browser import window
from typing import Literal

MIN_SCORE = 0
MAX_SCORE = 100

_LMS_commit = window.LMSCommit
_LMS_finish = window.LMSFinish
_LMS_get_value = window.LMSGetValue
_LMS_set_value = window.LMSSetValue
_LMS_initialize = window.LMSInitialize
_LMS_is_initialized = window.LMSIsInitialized


class ScormWrapper:
    def __init__(self) -> None:
        if not _LMS_is_initialized():
            _LMS_initialize()
            self.set_score(0)

    def get_learner_name(self) -> str:
        return _LMS_get_value("cmi.core.student_name")

    def set_completion_status(
        self, status: Literal["not attempted", "incomplete", "completed"]
    ) -> None:
        _LMS_get_value("cmi.core.lesson_status", status)
        _LMS_commit()

    def get_score(self) -> int:
        return int(_LMS_get_value("cmi.core.score.raw"))

    def set_score(self, score: int | float) -> None:
        _LMS_set_value("cmi.core.score.raw", score)

        _LMS_set_value("cmi.core.score.min", MIN_SCORE)
        _LMS_set_value("cmi.core.score.max", MAX_SCORE)

        scaled_score = score / MAX_SCORE
        _LMS_set_value("cmi.core.score.scaled", scaled_score)

        _LMS_commit()

    def on_finish(self) -> None:
        _LMS_set_value("cmi.exit", "suspend")
        _LMS_set_value("adl.nav.request", "suspendAll")

        _LMS_finish()


_instance = ScormWrapper()

get_score = _instance.get_score
set_score = _instance.set_score
on_finish = _instance.on_finish
set_completion_status = _instance.set_completion_status
