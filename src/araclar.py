#!/usr/bin/python3
# -*- coding: utf-8 -*-

def ikili_ara(wordlist, word):
    """
    Binary search
    """
    start = 0
    end = len(wordlist) - 1

    while start <= end:
        mid = int((start + end)/ 2)
        word_mid = wordlist[mid]
        if word_mid > word:
            end = mid - 1
        elif word_mid < word:
            start = mid + 1
        else:
            return mid
    return -1
