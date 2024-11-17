from browser import document

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

document["enter-test"].bind("click", lambda _: switch_to_test())
