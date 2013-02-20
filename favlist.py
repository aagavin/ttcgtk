#!/usr/bin/env python2
# coding: utf-8

import cPickle as pickle

class Favs:
	"""docstring for Favs"""
	def __init__(self):
		self.favlist=[]

	def add_fav(self,data):
		self.favlist.append(data)

	def get_fav_list(self):
		return self.favlist
		