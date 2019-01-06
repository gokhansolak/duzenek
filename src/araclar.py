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

def kucult_str(str_in):
    """
    Türkçe karakterli string küçült
    """
    lower_map = {
        ord('I'): 'ı',
        ord('İ'): 'i',
    }
    str_out = str_in.translate(lower_map)
    return str_out.lower()
