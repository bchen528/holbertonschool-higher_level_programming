#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        tup = ()
        sent = list(sentence)
        if sentence == "":
                sent[0] = None
        tup = (len(sent), sent[0])
        return tup
