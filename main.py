#!/usr/bin/env python2
# coding: utf-8

from gi.repository import Gtk, Gdk#, GdkPixbuf
from parser import ParseData
from favlist import Favs

#
class Appgui:
	"""docstring for Appgui"""
	def __init__(self):
		#builder init stuff
		builder=Gtk.Builder()
		builder.add_from_file("ttc.glade")
		builder.connect_signals(WinSignals())
		#window
		self.window=builder.get_object("main_window")

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

		### statusbar
		self.statbar=builder.get_object("statusbar")
		###

		#show all
		self.window.show_all()
		#builder.get_object("main_window").show_all()

		#about_dialog
		self.aboutdiag=builder.get_object("about_dialog")
		#get fav list
		self.favs=Favs()
		#generate routs
		self.generate_routs()		

	def generate_routs(self):
		""" generate """
		for i in ParseData().getAllRoutesTitle():
			self.route_cmb.append_text(str(i))

	def fav_win(self):
		fav_builder=Gtk.Builder()
		fav_builder.add_from_file("fav.glade")
		#connect
		fav_builder.connect_signals(FavSignals())
		#fav win
		fav_win=fav_builder.get_object("fav_window")

		#fav_cmb_box
		self.fav_cmb_box=fav_builder.get_object("fav_cmb_box")
		#Show Azll
		fav_win.show_all()
		#generate favourite
		self.generate_favourite()

	def generate_favourite(self):
		for i in self.favs.get_fav_list():
			self.fav_cmb_box.append_text(str(i))

class FavSignals:
	"""docstring for FavSignals"""
	def add_as_def_fav(self,widget,event=None):
		"""
		stoptag=hello.stop_cmb.get_active_text().split("-")
		stopName=hello.route_cmb.get_active_text()
		hello.favs.add_def_fav(hello.stop_cmb.get_active_text().split("-")[0],stopName.split("-")[0],stoptag[1].replace("[","").replace("]",""))
		"""
	def del_event(self,widget,event=None):
		hello.fav_cmb_box.remove(hello.fav_cmb_box.get_active())
		

class WinSignals:
	"""docstring for Signals"""

	def gtk_close(self,widget,event=None):
		hello.favs.save_fav_list()
		Gtk.main_quit()

	def about_menu(self,widget,event=None):
		hello.aboutdiag.run()
		hello.aboutdiag.hide()

	def add_fav(self,widget,event=None,data=None):
		stoptag=hello.stop_cmb.get_active_text().split("-")
		stopName=hello.route_cmb.get_active_text()
		if type(widget)==Gtk.Button:
			hello.favs.add_def_fav(hello.stop_cmb.get_active_text().split("-")[0],stopName.split("-")[0],stoptag[1].replace("[","").replace("]",""))
			hello.statbar.set_text("Added as default favourite")
		else:			
			hello.favs.add_fav(hello.stop_cmb.get_active_text().split("-")[0],stopName.split("-")[0],stoptag[1].replace("[","").replace("]",""))
			hello.statbar.set_text("Added as favourite")


	def view_fav(self,widget,event=None):
		hello.fav_win()

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
		try:
			stopid=(hello.stop_cmb.get_active_text().split("[")[1])[:-1]
		except AttributeError:
			pass
		
		nextStopsTimes=ParseData().getTimes(routeNum,stopid)
		try:
			hello.lbl1.set_text(nextStopsTimes[0]+"mins")
		except IndexError:
			hello.lbl1.set_text("...")
		try:
			hello.lbl2.set_text(nextStopsTimes[1]+"mins")
		except IndexError:
			hello.lbl2.set_text("...")
		try:
			hello.lbl3.set_text(nextStopsTimes[2]+"mins")
		except IndexError:
			hello.lbl3.set_text("...")
	########################################

		
		
if __name__=="__main__":
	hello=Appgui()
	Gtk.main()
