#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    sent = list(sentence)
    if sentence == "":
        sent[0] = None
    tup = (len(sent), sent[0])
    return tup
