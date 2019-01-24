#coding: utf-8

#----------------------------------------------------------------------------------------------------------------
#importy
from random import randint
from sys import exit
from Tkinter import *

#----------------------------------------------------------------------------------------------------------------

class main:
	def __init__(self):
		
#----------------------------------------------------------------------------------------------------------------
#proměnné
#----------------------------------------------------------------------------------------------------------------

		self.vzdel_souteze=[
			"a soutěž v matematicu",	###seznam vědomostních soutěží
			"a biologická olympiáda",
			"a matematická olympiáda",
			"a fyzikální olympiáda",
			" matematický klokan",
			"a soutěž Pražský glóbus",
			"a zeměpisná olympiáda",
		]
		self.sport_souteze=[
			" meziškolní turnaj ve vybíjené",
			" meziškolní turnaj ve fotbale",
			" meziškolní turnaj ve florbale",
			" meziškolní turnaj v atletice",
			" meziškolní turnaj v šipkách",
			" McKačer cup",
			
		]
		self.veda_souteze=[
			"a soutěž v rychlomíchání chemických sloučenin",
			"a robosoutěž"
		]
		
		self.tyden=42   #kolikátý týden se píše od hráčova nástupu do funkce ředitele
		#self.klidny_tyden=0 #kolik týdnů se nekonala žádná soutěž
		self.penize=10000 #kolik má škola na účtě
		self.celkove_prijmy=0
		self.celkove_vydaje=0
		self.mesicni_prijmy=0
		self.mesicni_vydaje=0
		self.studenti_spokojenost=50
		self.ucitele_spokojenost=50
		self.rodice_spokojenost=50
		
		
		#modifikátory plynoucí z vybavení školy - používají se při meziškolních soutěžích
		self.veda_level=0
		self.veda_modifier=self.veda_level*2.25 
		self.sport_level=0
		self.sport_modifier=self.sport_level*2.25
		self.vedomosti_level=0
		self.vedomosti_modifier=self.sport_level*2.25


		#proměnné, které jsou závislé na jiných faktorech
		self.plat=10
		self.pocet_zaku=120
		self.zaci_lvl=1
		self.najem=15
		self.castka=800   #částka, kterou platí každý student na školném
		self.pocet_ucitelu=self.pocet_zaku/10+10
		self.vydaje_na_ucitele= self.pocet_ucitelu*self.plat
		self.skolne=self.castka*self.pocet_zaku
		
		
		self.main=Tk()
		screen_width = self.main.winfo_screenwidth()
		screen_height = self.main.winfo_screenheight()
		self.main.attributes("-fullscreen", True)
		#main.overrideredirect=True
		#w = self.main.winfo_screenheight()
		#h = self.main.winfo_screenwidth()
		#self.main.geometry("%dx%d+0+0" % (w, h))
		
		#tlačítka
		
		self.forward_button=Button(self.main, text="vpřed",command=self.vpred) #tlačítka
		self.forward_button.pack()
		self.exit_button=Button(self.main, text="opustit hru", command=self.terminate)
		self.exit_button.pack()
		self.money_button=Button(self.main, text="změnit školné",command=self.zmenit_skolne)
		self.money_button.pack()
		self.economy_button=Button(self.main, text="ekonomika",command=self.economy)
		self.economy_button.pack()
		self.upgrade_button=Button(self.main,text="vylepšení",command=self.upgrades)
		self.upgrade_button.pack()
		self.plat_button=Button(self.main,text="změnit platy",command=self.zmenit_platy)
		self.plat_button.pack()
		
		#nápisy
		
		self.week_info=Label(self.main, text="týden: " + str (self.tyden))
		self.week_info.pack()
		self.money_info=Label(self.main, text="finance: " + str (self.penize))
		self.money_info.pack()
		self.studenti_info=Label(self.main,text="spokojenost studentů: " + str (self.studenti_spokojenost))
		self.studenti_info.pack()
		self.ucitele_info=Label(self.main,text="spokojenost učitelů: " + str (self.ucitele_spokojenost))
		self.ucitele_info.pack()
		self.rodice_info=Label(self.main,text="spokojenost rodičů: " + str (self.rodice_spokojenost))
		self.rodice_info.pack()
#----------------------------------------------------------------------------------------------------------------

	def game_over_finance(self):
		self.popupmsg("konec hry, Škola zkrachovala, zkus to znovu")
		return
		
	def game_over_puc(self):
		self.popupmsg("konec hry, byl jsi sesazen kombinovanou mocí svých poddaných")
		return
		
	def game_over_gut(self):  
		self.popupmsg("konec hry, šťastně jsi dokázal vést svou školu po dobu dvou let! Gratulujeme")
		return
	
	def popupmsg(self,msg):  #custom msgbox
		self.popup=Toplevel()
		self.popup.grab_set()
		self.popup.geometry("500x150+50+50")
		self.popup.wm_title("pozor")
		self.label=Label(self.popup, text=msg)
		self.label.pack(side="top",fill="x", pady=10)
		self.b1=Button(self.popup,text="OK",command=self.popup.destroy) ##jak zavřít i hlavní okno a vkusně ukončit hru? self.main.destroy zavírá jenom hlavní okno
		self.b1.pack()
		return

	def terminate(self): #ukončí hru
		sys.exit()
	
	def upgrades(self):
		self.upg=Toplevel()
		self.upg.attributes("-fullscreen",True)
		##zpět
		self.b1=Button(self.upg,text="zpět",command=self.upg.destroy)
		self.b1.pack()
		##info
		self.sport_info=Label(self.upg,text="úroveň sportovního vybavení: "+str(self.sport_level))
		self.sport_info.pack()
		self.veda_info=Label(self.upg,text="úroveň vědeckého vybavení: "+str(self.veda_level))
		self.veda_info.pack()
		self.vedomosti_info=Label(self.upg,text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level))
		self.vedomosti_info.pack()
		self.kapacita_info=Label(self.upg,text="maximální kapacita žáků je: "+str(self.pocet_zaku))
		self.kapacita_info.pack()
		##tlačítka na vylepšení
		self.sport_button=Button(self.upg,text="vylepšit sportovní vybavení",command=self.sport_upgrade)
		self.sport_button.pack()
		self.veda_button=Button(self.upg,text="vylepšit vědecké vybavení",command=self.veda_upgrade)
		self.veda_button.pack()
		self.vedomosti_button=Button(self.upg,text="vylepšit učební pomůcky",command=self.vedomosti_upgrade)
		self.vedomosti_button.pack()
		self.capacity_button=Button(self.upg,text="zvýšit kapacitu školy",command=self.expand)
		self.capacity_button.pack()
		return
	
	def expand(self):
		self.penize=self.penize-((self.zaci_lvl+1)*105000)
		self.zaci_lvl+=1
		self.ucitele_spokojenost-=5
		self.pocet_zaku+=40
		self.kapacita_info.config(text="maximální kapacita žáků je: "+str(self.pocet_zaku))
		self.money_info.config(text=str(self.penize))
	
	def sport_upgrade(self):
		self.penize=self.penize-((self.sport_level+1)*10000)
		self.sport_level+=1
		self.studenti_spokojenost+=10
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=5
		self.sport_info.config(text="úroveň sportovního vybavení: "+str(self.sport_level))
		self.money_info.config(text=str(self.penize))
		return
	
	def veda_upgrade(self):
		self.penize=self.penize-((self.veda_level+1)*10000)
		self.veda_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=10
		self.veda_info.config(text="úroveň vědeckého vybavení: "+str(self.veda_level))
		self.money_info.config(text=str(self.penize))
		return
		
	def vedomosti_upgrade(self):
		self.penize=self.penize-((self.vedomosti_level+1)*10000)
		self.vedomosti_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=10
		self.ucitele_spokojenost+=5
		self.vedomosti_info.config(text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level))
		self.money_info.config(text=str(self.penize))
		return
		

	def zmenit_skolne(self):
		self.skol=Toplevel()
		self.skol.grab_set()
		self.skol.geometry("500x150+50+50")
		self.infolabel=Label(self.skol, text="stávající školné na žáka na měsíc je "+str(self.castka)+" kč") #= str(variable_name) + ": " + str(variable) + "kč student/měsíc")
		self.infolabel.pack()
		self.s_entry=Entry(self.skol, width=150)
		self.s_entry.pack()
		self.s_entry.focus_set()
		#self.output=self.entry.get()
		self.b1=Button(self.skol, text="Storno", command=self.skol.destroy)
		self.b1.pack()
		self.b2=Button(self.skol,text="Potvrdit", command=self.s_zmen)# and self.entry.delete(0,"end")) #self.entry.get()))
		self.b2.pack()
		#return self.skol
		
	def s_zmen(self):
		self.s_output=int(self.s_entry.get())
		if (self.s_output>400)and(self.s_output<1500):
			self.castka=self.s_output
			self.skol.destroy()
			#self.potvrzeni=Label(self.ent, text="školné aktualizováno")
			return
		
	def zmenit_platy(self):
		self.plat=Toplevel()
		self.plat.grab_set()
		self.plat.geometry("500x150+50+50")
		self.pocet_label=Label(self.plat,text="počet učitelů: "+str(self.pocet_ucitelu)).pack()
		self.plat_label=Label(self.plat,text="plat na jednoho učitele: "+str(self.plat)).pack()
		self.naklady_label=Label(self.plat,text="celkové náklady na učitele: "+str(self.vydaje_na_ucitele)).pack()
		self.p_entry=Entry(self.plat, width=150)
		self.p_entry.pack()
		self.p_entry.focus_set()
		self.b1=Button(self.plat,text="Storno",command=self.plat.destroy)
		self.b1.pack()
		self.b2=Button(self.plat,text="Potvrdit", command=self.p_zmen)# and self.entry.delete(0,"end")) #self.entry.get()))
		self.b2.pack()	
		
	def p_zmen(self):
		self.p_output=int(self.p_entry.get())
		if (self.p_output>400)and(self.p_output<1500):
			self.castka=self.p_output
			self.plat.destroy()
			#self.potvrzeni=Label(self.ent, text="školné aktualizováno")
			return
	
	def vpred(self):
		self.tyden+=1
		self.week_info.config(text="týden= " + str (self.tyden)) #mění číslo týdne v ukazateli v hlavním okně
		if self.tyden%44==0: #kontrola, jestli neskončil školní rok
			self.tyden=self.tyden+7 #skok přes prázdniny
		if self.tyden==104: #kontrola, jestli hráči neskončilo funkční obodobí
			self.game_over_gut()
			return
		if self.tyden%4==0:  #kontrola, zda škola nezkrachuje při placení nájmu nebo vyplácení platů na konci měsíce 
			if self.penize<0:
				self.game_over_finance()
			print self.tyden, self.penize
			if (self.penize+self.skolne)-(self.vydaje_na_ucitele+self.najem)<0:
				self.game_over_finance()
			elif self.studenti_spokojenost<15 and self.ucitele_spokojenost<15 or self.studenti_spokojenost<15 and self.rodice_spokojenost<15 or self.rodice_spokojenost<15 and self.ucitele_spokojenost<15: #kontrola spokojenosti na začátku každého měsíce
				self.game_over_puc()
			else:
				self.penize=self.penize-(self.vydaje_na_ucitele+self.najem)+self.skolne   #když škola nezkrachovala, tak se odečtou náklady
				self.money_info.config(text="finance: " + str (self.penize))
		if self.studenti_spokojenost<=25:	#varování kvůli nespokojenosti nějaké skupiny
			self.popupmsg("studenti jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat")
			return
		if self.rodice_spokojenost<=25:
			self.popupmsg("rodiče jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat")
			return
		if self.ucitele_spokojenost<=25:
			self.popupmsg("ucitele jsou vrcholně nespokojeni. Vyplatilo by se s tím něco udělat")
			return
			
	def economy(self):
		self.ecwnd=Toplevel()
		self.ecwnd.attributes('-fullscreen', True)
		self.ecwnd.grab_set()
		self.back_button=Button(self.ecwnd, text="zpět",command=self.ecwnd.destroy)
		self.back_button.pack()
		self.time_info=Label(self.ecwnd, text="týden: " + str (self.tyden))
		self.time_info.pack()
		self.money_info=Label(self.ecwnd,text="finance: " + str (self.penize))
		self.money_info.pack()
		self.teacher_count=Label(self.ecwnd,text="počet učitelů: "+str(self.pocet_ucitelu))
		self.teacher_count.pack()
		self.teacher_salary=Label(self.ecwnd,text="plat učitel/měsíc: "+str(self.plat))
		self.teacher_salary.pack()
		self.student_count=Label(self.ecwnd,text="počet žáků: "+str(self.pocet_zaku))
		self.student_count.pack()
		self.student_income=Label(self.ecwnd,text="školné žák/měsíc: "+str(self.castka))
		self.student_income.pack()
		self.building_expenses=Label(self.ecwnd,text="měsíční nájem: "+ str(self.najem))
		self.building_expenses.pack()
		
	def soutez(self):
		self.soutez=Toplevel()
		self.soutez.grab_set()
		self.soutez_label=Label(self.soutez.text="V týdnu se konal")
		
lol=main()
mainloop()
