#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from models import User,Blog,Comment

def test():
	yield from orm.create_pool(host='127.0.0.1',port=3306,user='root',password='123456',db='py_blog')
	u = User(name='Test',email='test@example.com',passwd='1234567890',image='about:blank')

	yield from u.save()

for x in test():
	pass