#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    strfchar = sentence[0]
    if not sentence[0]:
        strfchar = None
    return(strlen, strfchar)
