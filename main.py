#!/usr/bin/env python2
# coding: utf-8

from gi.repository import Gtk, Gdk#, GdkPixbuf
from parser import ParseData
#
class Appgui:
	"""docstring for Appgui"""
	def __init__(self):
		#builder init stuff
		builder=Gtk.Builder()
		builder.add_from_file("ttc.glade")
		builder.connect_signals(Signals())
		#window
		#self.window=builder.get_object("main_window")

		### combo boxes
		#route_combo
		self.route_cmb=builder.get_object("route_combo")
		#direction_combo
		self.dir_cmb=builder.get_object("direction_combo")
		#stop_combo
		self.stop_cmb=builder.get_object("stop_combo")
		###

		### info labels
		# first label
		self.lbl1=builder.get_object("info_label1")
		# second label
		self.lbl2=builder.get_object("info_label2")
		# tird label
		self.lbl3=builder.get_object("info_label3")
		### end info labels

		#show all
		#self.window.show_all()
		builder.get_object("main_window").show_all()
		#generate
		self.generate()

	""" generate """
	def generate(self):
		for i in ParseData().getAllRoutesTitle():
			self.route_cmb.append_text(str(i))

class Signals:
	"""docstring for Signals"""

	def gtk_close(self,widget,event=None):
		Gtk.main_quit()

	

	########################################
	def generateDirection(self,widget,event=None):
		busnum=hello.route_cmb.get_active_text().split("-")[0]
		hello.dir_cmb.get_model().clear()
		for i in ParseData().getRouteDirection(busnum):
			hello.dir_cmb.append_text(str(i))

	def generateStop(self,widget,event=None):
		busnum=hello.route_cmb.get_active_text().split("-")[0]
		dirNum=hello.dir_cmb.get_active()

		hello.stop_cmb.get_model().clear()
		for i in ParseData().getStops(busnum,dirNum):
			hello.stop_cmb.append_text(str(i))

	def printStopTimes(self,widget,event=None):
		routeNum=(hello.route_cmb.get_active_text().split("-"))[0]
		stopid=(hello.stop_cmb.get_active_text().split("[")[1])[:-1]
		
		nextStopsTimes=ParseData().getTimes(routeNum,stopid)
		hello.lbl1.set_text(nextStopsTimes[0]+"mins")
		hello.lbl2.set_text(nextStopsTimes[1]+"mins")
		hello.lbl3.set_text(nextStopsTimes[2]+"mins")
	########################################

		
		
if __name__=="__main__":
	hello=Appgui()
	Gtk.main()
