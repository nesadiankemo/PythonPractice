#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def load(path):
    words = []
    with open(path, 'r') as f:
        for line in f:
            # the line string‘s end with '\n', remove it
            word = line[:-1]
            words.append(word)
            print(word)
    return words

def repl(obj):
    return len(obj.group(0)) * '*'

# about method re.mach & re.sub visit: https://docs.python.org/3/library/re.html
if __name__ == "__main__":
    words = load('filtered_words.txt')
    p = '|'.join(words)
    pattern = re.compile(p)
    s = input('input:')
    if pattern.match(s):
        print('Freedom')
    else:
        print('Human Rights')

    s = input('0012 input:')
    m = pattern.sub(repl, s)
    print(m)
