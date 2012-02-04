#!/usr/bin/env python

# example helloworld.py
from GmailChatStats.DbLoader import DbLoader
import sys
import pygtk
pygtk.require('2.0')
import gtk

class Base:

	def gmailUsedCallbacl(self, widget, data=None):
		if self.gmailInEnglishCheckButton.get_active():
			self.chatsEntry.set_sensitive(False)
		else:
			self.chatsEntry.set_sensitive(True)
		
	def loadData(self, widget, data=None):
		print "loadData"
		
		chatsStr = ""
		if self.gmailInEnglishCheckButton.get_active()== False:
			chatsStr = "[Gmail]/Chats"
		else:
			if self.chatsEntry.get_text() != None:
				chatsStr = self.chatsEntry.get_text()
		dbloader = DbLoader(self.userNameEntry.get_text(), self.passwordEntry.get_text(),chatsStr,self.modeCombo.entry.get_text() )
		dbloader.Process()
		print "\n"
		
		
	def delete_event(self, widget, event, data=None):
		print "delete event occurred"
		return False
	def destroy(self, widget, data=None):
		print "destroy signal occurred"
		gtk.main_quit()

	def __init__(self):
		#window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Gmail stats")
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)
		self.window.set_border_width(0)
		
		#mainBox
		mainBox = gtk.HBox(False, 0)
		self.window.add(mainBox)
		mainBox.show()
		
		#inputBox
		inputBox = gtk.VBox(False, 0)
		mainBox.pack_start(inputBox, True, True, 0)
		inputBox.set_border_width(10)
		inputBox.show()
		
		#buttonsBox
		buttonsBox = gtk.VBox(False, 0)
		mainBox.pack_start(buttonsBox, True, True, 0)
		buttonsBox.set_border_width(10)
		buttonsBox.show()
		
		#gmailInEnglishCheckButton
		self.gmailInEnglishCheckButton = gtk.CheckButton("I use Gmail in English")
		inputBox.pack_start(self.gmailInEnglishCheckButton, True, True, 0)
		self.gmailInEnglishCheckButton.connect("toggled", self.gmailUsedCallbacl, None)
		self.gmailInEnglishCheckButton.show()
		
		
		#username
		tmpBox = gtk.HBox(False, 0)
		inputBox.pack_start(tmpBox, True, True, 0)
		tmpBox.show()
		label = gtk.Label("username  ")
		tmpBox.pack_start(label, True, True, 0)
		label.show()
		
		#userNameEntry
		self.userNameEntry = gtk.Entry(max=0)
		tmpBox.pack_start(self.userNameEntry, True, True, 0)
		self.userNameEntry.show()
		
		#password
		tmpBox = gtk.HBox(False, 0)
		inputBox.pack_start(tmpBox, True, True, 0)
		tmpBox.show()
		label = gtk.Label("password   ")
		tmpBox.pack_start(label, True, True, 0)
		label.show()
		
		#passwordEntry
		self.passwordEntry = gtk.Entry(max=0)
		tmpBox.pack_start(self.passwordEntry, True, True, 0)
		self.passwordEntry.set_visibility(gtk.FALSE)
		self.passwordEntry.show()
		
		
		#chats
		tmpBox = gtk.HBox(False, 0)
		inputBox.pack_start(tmpBox, True, True, 0)
		tmpBox.show()
		label = gtk.Label("chats label ")
		tmpBox.pack_start(label, True, True, 0)
		label.show()
		
		#chatsEntry
		self.chatsEntry = gtk.Entry(max=0)
		tmpBox.pack_start(self.chatsEntry, True, True, 0)
		self.chatsEntry.show()
		
		#mode
		tmpBox = gtk.HBox(False, 0)
		inputBox.pack_start(tmpBox, True, True, 0)
		tmpBox.show()
		label = gtk.Label("mode        ")
		tmpBox.pack_start(label, True, True, 0)
		label.show()
		
		#modeCombo
		self.modeCombo = gtk.Combo()
		slist =["usecache", "nocache", "cacheonly"]
		self.modeCombo.set_popdown_strings(slist)
		tmpBox.pack_start(self.modeCombo, True, True, 0)
		self.modeCombo.show()
		
		
		
		#loadDataButton 
		loadDataButton = gtk.Button("Load data")
		#multiple args
		loadDataButton.connect("clicked", self.loadData, None)
		buttonsBox.pack_start(loadDataButton, True, True, 0)
		loadDataButton.show()
	
		#button Close
		#closeButton = gtk.Button("Close")
		##only one arg
		#closeButton.connect_object("clicked", gtk.Widget.destroy, self.window)
		#buttonsBox.pack_start(closeButton, True, True, 0)
		#closeButton.show()
 
	
		# show window
		self.window.show()

	def main(self):
		gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
print __name__
if __name__ == "__main__":
	base = Base()
	base.main()


