#coding: utf-8

#----------------------------------------------------------------------------------------------------------------
#importy
from random import randint
from Tkinter import *

#----------------------------------------------------------------------------------------------------------------

class main:
	def __init__(self):
		self.main=Tk()
		#main.overrideredirect=True
		#w = self.main.winfo_screenheight()
		#h = self.main.winfo_screenwidth()
		#self.main.geometry("%dx%d+0+0" % (w, h))
		
		self.forward_button=Button(self.main, text="vpřed",command=self.vpred) #tlačítka
		self.forward_button.pack()
		self.exit_button=Button(self.main, text="opustit hru", command=self.exit)
		self.exit_button.pack()
		#self.money_button=Button(self.main, text="změnit školné",command=self.zmenit_skolne)
#----------------------------------------------------------------------------------------------------------------
#proměnné
#----------------------------------------------------------------------------------------------------------------
		self.tyden=42   #kolikátý týden se píše od hráčova nástupu do funkce ředitele
		#self.klidny_tyden=0 #kolik týdnů se nekonala žádná soutěž
		self.penize=0 #kolik má škola na účtě
		self.studenti_spokojenost=50 #
		self.ucitele_spokojenost=50	# spokojenosti skupin 
		self.rodice_spokojenost=50	#

		#modifikátory plynoucí z vybavení školy - používají se při meziškolních soutěžích
		self.veda_modifier=0
		self.sport_modifier=0  
		self.vzdelanost_modifier=0

		#proměnné, které jsou závislé na jiných faktorech
		self.vydaje_na_ucitele= 15
		self.pocet_zaku=120
		self.najem=15
		self.castka=800   #částka, kterou platí každý student na školném
		self.skolne=self.castka*self.pocet_zaku
#----------------------------------------------------------------------------------------------------------------
	def game_over_finance(self):
		self.popupmsg("konec hry, Škola zkrachovala")
		self.
	def game_over_puc(self):
		self.popupmsg("konec hry, byl jsi sesazen kombinovanou mocí svých poddaných")
	def game_over_gut(self):  
		self.popupmsg("konec hry, šťastně jsi dokázal vést svou školu po dobu pěti let! Gratulujeme")
	def popupmsg(self,msg):
		popup=Tk()
		popup.wm_title("pozor")
		label=Label(popup, text=msg)
		label.pack(side="top",fill="x", pady=10)
		b1=Button(popup,text="OK",command=popup.destroy)
		b1.pack()
		popup.mainloop()
	def exit(self): #ukončí hru
		self.main.quit()
	def vpred(self):
		self.tyden+=1
		print self.tyden
		#self.popupmsg(self.tyden)
		if self.tyden%44==0: #kontrola, jestli neskončil školní rok
			self.tyden=self.tyden+7 #skok přes prázdniny
		if self.tyden==104: #kontrola, jestli hráči neskončilo funkční obodobí
			self.game_over_gut()
		if self.tyden%4==0:  #kontrola, zda škola nezkrachuje při placení nájmu nebo vyplácení platů na konci měsíce 
			if self.penize<0:
				self.game_over_finance()
			print self.tyden, self.penize
			if (self.penize+self.skolne)-(self.vydaje_na_ucitele+self.najem)<0:
				self.game_over_finance()
			elif self.studenti_spokojenost<15 and self.ucitele_spokojenost<15 or self.studenti_spokojenost<15 and self.rodice_spokojenost<15 or self.rodice_spokojenost<15 and self.ucitele_spokojenost<15: #kontrola spokojenosti na začátku každého měsíce
				self.game_over_puc()
			else:
				self.penize=self.penize-(self.vydaje_na_ucitele+self.najem)#+self.skolne   #když škola nezkrachovala, tak se odečtou náklady
		if self.studenti_spokojenost<=25:	#varování kvůli nespokojenosti nějaké skupiny
			self.popupmsg("studenti jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat")
		if self.rodice_spokojenost<=25:
			self.popupmsg("rodiče jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat")
		if self.ucitele_spokojenost<=25:
			self.popupmsg("ucitele jsou vrcholně nespokojeni. Vyplatilo by se s tím něco udělat")
			
		
lol=main()
mainloop()








