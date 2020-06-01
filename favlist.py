#!/usr/bin/env python2
# coding: utf-8

import cPickle as pickle

class Favs:
	"""docstring for Favs"""
	def __init__(self):
		try:
			self.favlist=pickle.load(open("./cache/fvlst.txt","rb"))
		except IOError as e:
			self.favlist=[]

	def add_fav(self,stopName,routeTag,stopTag):
		data=stopName+"|"+routeTag+"|"+stopTag
		if data not in self.favlist:
			self.favlist.append(data)

	def add_def_fav(self,stopName,routeTag,stopTag):
		data=stopName+"|"+routeTag+"|"+stopTag
		if data not in self.favlist:
			self.favlist.insert(0,data)

	def get_fav_list(self):
		return self.favlist

	def save_fav_list(self):
		pickle.dump(self.favlist,open("./cache/fvlst.txt","wb"))
		