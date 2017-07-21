#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
def main(args):
	pass

def calcul_words(text):
	d = dict()
	l = re.split(r'[\W]+', text)
	for w in l:
		if w.isalpha():
			if w in d:
				d[w.lower()] = d[w] + 1
			else:
				d[w.lower()] = 1
	return d
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	s = calcul_words(f.read())
	print('total find: %d' % len(s))
	for k, v in s.items():
		print('%s: %d' % (k, v))