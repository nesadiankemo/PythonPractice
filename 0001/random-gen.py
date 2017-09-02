#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

def random_gen(length, key_length=10):
    keys = 'abcdefghijklmnopqrstuvwxyz0123456789'
    s = set()
    while len(s) < length:
        a = ''
        for i in range(key_length):
            a = a + random.choice(keys)
        s.add(a)
    return s
if __name__ == '__main__':
    s = random_gen(200)
    print(s)
