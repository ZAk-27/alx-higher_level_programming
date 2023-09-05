#!/usr/bin/python3
"""
Function printing a text with 2 new lines after each '.', '?', ':'
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    nvText = ""
    for i in range(len(text)):
        if not i == 0 and text[i] == " " and text[i - 1] in ".?:":
            continue
        nvText += text[i]
        if text[i] in ".?:":
            nvText += "\n\n"
    print(nvText, end="")
