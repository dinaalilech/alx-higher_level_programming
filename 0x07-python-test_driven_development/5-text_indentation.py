#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

It supplies one function, text_indentation().
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ''
    for c in text:
        if c in ' \n\t\r\v\f' and line == '':
            continue
        line += c
        if c in '.?:':
            print(line, end='\n\n')
            line = ''
    while len(line) > 0 and line[-1] in ' \n\t\r\v\f':
        line = line[:-1]
    print(line, end='')
