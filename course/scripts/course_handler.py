from browser import document
from scorm_wrapper import MAX_SCORE, set_score, set_completion_status


clicked_ids = set()
details_tags = document.select("details")

HALF_SCORE = MAX_SCORE // 2
SCORE_PER_CLICK = HALF_SCORE / len(details_tags)


def switch_to_test():
    main = document["main"]

    main.class_name += " h-screen"

    main.html = """
    <iframe
      width="100%"
      height="100%"
      src="test.htm"
      frameborder="0"
    ></iframe>
    """


def get_on_clicked(id: int):
    def on_clicked(_) -> None:
        set_completion_status("incomplete")

        clicked_ids.add(id)
        all_clicked = len(clicked_ids) == len(details_tags)

        score = SCORE_PER_CLICK * len(clicked_ids)
        if all_clicked:
            score = HALF_SCORE

        set_score(score)

    return on_clicked


for i, element in enumerate(details_tags):
    element.bind("click", get_on_clicked(i))

document["enter-test"].bind("click", lambda _: switch_to_test())
