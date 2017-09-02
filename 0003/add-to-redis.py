#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
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

def addToRedis(data):
	r = redis.Redis(host='localhost', port=6379, db=0)
	for x in data:
		r.lpush('my_key', x)

if __name__ == '__main__':
	data = random_gen(200)
	addToRedis(data)