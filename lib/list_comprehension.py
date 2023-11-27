#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = []
    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums if even_nums else []

def make_exclamation(sentence_list):
    pass