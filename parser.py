#!/usr/bin/env python2
#

#import library to do http requests:
import urllib
#import easy to use xml parser called minidom:
from xml.dom import minidom

#All List Data urls
ROUTESLISTURL='http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=ttc'
DIRECTIONTAGINFO ='http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=ttc&r='
STOPIDURL='http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=ttc&stopId='

class ParseData:
	"""The class that gets the
	requred data and returns it"""
	def __init__(self):
		pass

	def getAllRoutesTitle(self):
		routeArray=[]
		dom=minidom.parse(urllib.urlopen(ROUTESLISTURL))
		for i in dom.getElementsByTagName('route'):
			routeArray.append(i.attributes['title'].value)
		return routeArray


	def getRouteDirection(self,route):
		directionarr=[]
		dom=minidom.parse(urllib.urlopen(DIRECTIONTAGINFO+route))
		for i in dom.getElementsByTagName('direction'):
			directionarr.append(i.attributes['title'].value)
		return directionarr

	def getStops(self,route,dirNum):
		stopStr=""
		directions=self.getRouteDirection(route)

		dom=minidom.parse(urllib.urlopen(DIRECTIONTAGINFO+route))

		for i in dom.getElementsByTagName('stop'):
			try:
				title=i.attributes['title'].value
				tag=i.attributes['stopId'].value
				if "_ar" in tag:
					stopStr=stopStr+title+" ["+tag+"]"+"|"
				else:
					stopStr=stopStr+title+" ["+tag+"]"+"!"
				#stopArr.append(stop)
			except Exception:
				continue

		#print len(stopStr.split("|"))
		#print stopStr.split("|")[dirNum].split("!")
		return stopStr.split("|")[dirNum].split("!")

	def getTimes(self,stopId):
		stopTimes=[]
		dom=minidom.parse(urllib.urlopen(STOPIDURL+stopId))

		for i in dom.getElementsByTagName('prediction'):
			stopTimes.append(i.attributes['minutes'].value)

		print stopTimes

