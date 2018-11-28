#coding: utf-8

from Tkinter import *

class main:
	def __init__(self):
		self.main=Tk()
		main.overrideredirect=True
		w = self.main.winfo_screenheight()
		h = self.main.winfo_screenwidth()
		self.main.geometry("%dx%d+0+0" % (w, h))
		
		#self.forward_button=Button(self.main, text="vpřed",command=self.forward)
		#self.forward_button.pack
		self.exit_button=Button(self.main, text="opustit hru", command=self.exit)
		self.exit_button.pack
	def exit(self):
		self.main.quit()
		
lol=main()
mainloop()



###proč musíš neodpustit zrovna mě?
###nejistoty jsou zbytečný
###nikdy nikam s nikým nechodím
#rip budoucnost
#jak nedospělej?






