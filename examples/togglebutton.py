#!/usr/bin/env python

# example togglebutton.py

import pygtk
pygtk.require('2.0')
import gtk

class ToggleButton:
	# Our callback
	# The data passed to this method is printed to stdout
	def callback(self, widget, data=None):
		print "%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()])
	def delete_event(self,widget,event,data=None):
		gtk.main_quit()
		return False

	def __init__(self):
		# Create a new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		# Set the window title
		self.window.set_title("Toggle Button")

		# Set a handler for delete_event that immediately exits GTK.
		self.window.connect("delete_event", self.delete_event)

		# Sets the border width of the window
		self.window.set_border_width(20)

		# Create a vertical box
		vbox = gtk.VBox(True, 2)

		# Put the vbox in the main window
		self.window.add(vbox)

		# Create first button
		button = gtk.ToggleButton("togglebutton 1")

		# When the button is toggled, we call the "callback" method
		# with a pointer to "button" as its argument
		button.connect("toggled", self.callback, "togglebutton 1")

		# Insert button 1
		vbox.pack_start(button, True, True, 2)

		button.show()

		# Create second button
		button = gtk.ToggleButton("togglebutton 2")
		button.connect("toggled", self.callback, "togglebutton 2")
		vbox.pack_start(button, True, True, 2)
		button.show()

		# Create "Quit" button
		button = gtk.Button("Quit")
		button.connect("clicked", lambda wid: gtk.main_quit())

		vbox.pack_start(button, True, True, 2)

		button.show()
		vbox.show()
		self.window.show()
def main():
	gtk.main()
	return 0

if __name__=="__main__":
	ToggleButton()
	main()
