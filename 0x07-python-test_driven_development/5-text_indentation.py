#!/usr/bin/python3
def text_indentation(text):
    """text_indentation

    Arguments:
        text {[str]} -- [text to be indented]

    Raises:
        TypeError: [if text given is not str]
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_string = ""
    for i in text:
        new_string += i
        if i in '?:.':
            print(new_string.lstrip(), end='\n\n')
            new_string = ""
    print(new_string.lstrip(), end="")
