#coding: utf-8

#----------------------------------------------------------------------------------------------------------------
#importy
from random import randint
from sys import exit
from Tkinter import *

#----------------------------------------------------------------------------------------------------------------

class main:
	def __init__(self):
		self.main=Tk()
		screen_width = self.main.winfo_screenwidth()
		screen_height = self.main.winfo_screenheight()
		self.main.attributes('-fullscreen', True)
		#main.overrideredirect=True
		#w = self.main.winfo_screenheight()
		#h = self.main.winfo_screenwidth()
		#self.main.geometry("%dx%d+0+0" % (w, h))
		
		self.forward_button=Button(self.main, text="vpřed",command=self.vpred) #tlačítka
		self.forward_button.pack()
		self.exit_button=Button(self.main, text="opustit hru", command=self.terminate)
		self.exit_button.pack()
		self.money_button=Button(self.main, text="změnit školné",command=self.zmenit_skolne)
		self.money_button.pack()
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
		self.popupmsg("konec hry, Škola zkrachovala, zkus to znovu")
		return
	def game_over_puc(self):
		self.popupmsg("konec hry, byl jsi sesazen kombinovanou mocí svých poddaných")
		return
	def game_over_gut(self):  
		self.popupmsg("konec hry, šťastně jsi dokázal vést svou školu po dobu pěti let! Gratulujeme")
		return
	def popupmsg(self,msg):
		popup=Tk()
		#####popup.set_focus()
		popup.geometry("500x150+50+50")
		popup.wm_title("pozor")
		label=Label(popup, text=msg)
		label.pack(side="top",fill="x", pady=10)
		b1=Button(popup,text="OK",command=popup.destroy) ##jak zavřít i hlavní okno a vkusně ukončit hru? self.main.destroy zavírá jenom hlavní okno
		b1.pack()
		popup.mainloop()
	def popuptxt(self,msg):
		ptxt=Tk()
		ptxt.geometry("500x150+600+600")
		t1=Label(ptxt, text=msg)
		t1.pack()
		e=Entry(ptxt,width=150).pack()
		#value=e.get()
		b1=Button(text="ok",command=self.overwrite)
		ptxt.b1.pack()
		b2=Button(text="zpět",command=ptxt.exit)
		ptxt.b2.pack()
		ptxt.mainloop()
		def overwrite(self):
			self.x=0
			self.y=0
			if value<1200 and value>400 and value==self.castka:  #jestli není školné moc vysoké, nebo nízké, a jestli se vůbec změnilo
				if value<castka: 
					self.x=value-castka
					self.y=self.x/50
					self.studenti_spokojenost=self.studenti_spokojenost+self.y*5    #úprava spokojeností v závislosti na školném
					self.rodice_spokojenost=self.rodice_spokojenost+self.y*5
				else:
					self.x=value-castka
					self.y=self.x/50			
					self.studenti_spokojenost=self.studenti_spokojenost-self.y*5	  #úprava spokojenosti v závislosti na školném
					self.rodice_spokojenost=self.rodice_spokojenost-self.y*5
				castka=value
		
	def terminate(self): #ukončí hru
		sys.exit()
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
			return
		if self.rodice_spokojenost<=25:
			self.popupmsg("rodiče jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat")
			return
		if self.ucitele_spokojenost<=25:
			self.popupmsg("ucitele jsou vrcholně nespokojeni. Vyplatilo by se s tím něco udělat")
			return
			
			
			
	def zmenit_skolne(self):
		self.popuptxt("jak má být vysoké školné?")
	
		
lol=main()
mainloop()








