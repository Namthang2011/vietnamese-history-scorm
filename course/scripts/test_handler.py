from browser import document  # type: ignore
from problems import problems
from scorm_wrapper import (
    MAX_SCORE,
    get_score,
    set_score,
    on_finish,
    set_completion_status,
)

HALF_SCORE = MAX_SCORE / 2
SCORE_PER_CORRECT = HALF_SCORE / len(problems)


def reload_problem(index: int):
    problem = problems[index]

    description = f"<b>Câu {index+1}: </b>{problem.description}"
    document["description"].html = description

    problem_dict = vars(problem)

    for answer in ["a", "b", "c", "d"]:
        document[f"{answer}-desc"].html = problem_dict[answer]


class TestHandler:
    def __init__(self) -> None:
        reload_problem(0)
        self.correct_count = 0
        self.current_problem = 0

    def on_test_ended(self):
        test_score = self.correct_count * SCORE_PER_CORRECT
        if self.correct_count == len(problems):
            test_score = HALF_SCORE

        course_score = get_score()
        total_score = course_score + test_score

        completion_status = "not attempted"
        if total_score > 0:
            completion_status = "completed"

        set_completion_status(completion_status)
        set_score(total_score)

        on_finish()

        document["description"].html = f"""
        Bạn đã trả lời đúng <b>{self.correct_count}</b> câu.
        <br>
        Số điểm của bạn là <b>{total_score}</b>.
        """

        for answer_btn in ["a", "b", "c", "d"]:
            del document[f"{answer_btn}-button"]

    def on_choose_answer(self, answer: str) -> None:
        if answer == problems[self.current_problem].right_answer:
            self.correct_count += 1

        self.current_problem += 1

        if self.current_problem >= len(problems):
            self.on_test_ended()
            return

        reload_problem(self.current_problem)


_instance = TestHandler()

document["a-button"].bind("click", lambda _: _instance.on_choose_answer("a"))
document["b-button"].bind("click", lambda _: _instance.on_choose_answer("b"))
document["c-button"].bind("click", lambda _: _instance.on_choose_answer("c"))
document["d-button"].bind("click", lambda _: _instance.on_choose_answer("d"))
