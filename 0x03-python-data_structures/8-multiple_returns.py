#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    sent = list(sentence)
    if sentence == "":
        tup = (len(sent), None)
    else:
        tup = (len(sent), sent[0])
    return tup
