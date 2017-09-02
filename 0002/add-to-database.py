#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
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

def addToDatabase(data):
    passwd = input('password for database: ')
    db = pymysql.connect(host='localhost', user='root', passwd=passwd)
    cur = db.cursor()
    cur.execute('create database if not exists test;')
    cur.execute('use test;')
    cur.execute('DROP TABLE if exists t1;')
    cur.execute('''create table t1(
                    id int unsigned not null auto_increment primary key,
                    num char(10) not null);''')
    # cur.execute('''insert into t1 values(NULL, 'abcdefg');''')
    for x in data:
        cur.execute('''insert into t1 values(NULL, "{0}");'''.format(x))
    cur.close()
    db.commit()
    db.close()

if __name__ == '__main__':
    data = random_gen(200)
    addToDatabase(data)