#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        f_word = sentence[0]
        new_tuple = [length, f_word]
        return(new_tuple)
    else:
        return(length, None)
