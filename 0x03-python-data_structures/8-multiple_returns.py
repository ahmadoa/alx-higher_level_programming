#!/usr/bin/python3
def multiple_returns(sentence):
    first = ''
    length = len(sentence)
    if sentence == '':
        first = None
    else:
        first = sentence[0]
    return length, first
