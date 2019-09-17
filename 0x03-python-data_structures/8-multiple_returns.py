#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    strlen = len(sentence)
    strfchar = sentence[0]
    if sentence[0] is None:
        return(strlen, None)
    return(strlen, strfchar)
