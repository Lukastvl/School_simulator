#coding: utf-8

# jak restartovat program, aby nešlo hrát po prohře/výhře hráče
# jinak lépe dynamicky vytvářet labely
# mazání hodnot funkcí self.random_event() 


#!!!!!!předělat upgrady - na hlavní obrazovku?

##grafika

#----------------------------------------------------------------------------------------------------------------
#importy
from random import randint
from sys import exit
from Tkinter import *

#----------------------------------------------------------------------------------------------------------------
#konstruktor

class main:
	def __init__(self):
		
#----------------------------------------------------------------------------------------------------------------
#proměnné
#----------------------------------------------------------------------------------------------------------------

		self.vzdel_souteze=[
			"a soutěž v matematicu",	#seznam vědomostních meziškolních soutěží
			"a biologická olympiáda",
			"a matematická olympiáda",
			"a fyzikální olympiáda",
			" matematický klokan",
			"a soutěž Pražský glóbus",
			"a zeměpisná olympiáda",
		]
		
		self.sport_souteze=[   #seznam sportovních meziškolních soutěží
			" meziškolní turnaj ve vybíjené",
			" meziškolní turnaj ve fotbalu",
			" meziškolní turnaj ve florbalu",
			" meziškolní turnaj v atletice",
			" meziškolní turnaj v šipkách",
			" meziškolní turnaj ve stolním tenisu",
			" meziškolní turnaj v orientačním běhu",
		]
		
		self.veda_souteze=[ #seznam vědeckých meziškolních soutěží
			"a soutěž v rychlomíchání chemických sloučenin",
			"a robosoutěž",
			"a soutěž školních časopisů",
			"a soutěž v navrhování fyzikálních experimentů",
			"a soutěž mladých inženýrů",
			"a soutěž mladých designérů",
			"a soutěž v rychlopitvách ježků",
		]
		
		self.tyden=42   #kolikátý týden se píše od hráčova nástupu do funkce ředitele
		self.calm_week=0 #kolik týdnů se nekonala žádná meziškolní soutěž
		self.penize=int(10000) #kolik má škola na účtě, integer aby se z toho nedělal float a na obrazovce nebylo x.0
		self.min_salary=12000 #minimální plat pro učitele
		self.studenti_spokojenost=50
		self.ucitele_spokojenost=50 #spokojenosti tří skupin osazenstva školy
		self.rodice_spokojenost=50
				
		# levely školního vybavení a modifikátory plynoucí z vybavení školy - používají se při meziškolních soutěžích
		self.veda_level=0
		self.veda_modifier=self.veda_level*2.75 
		self.sport_level=0
		self.sport_modifier=self.sport_level*2.75
		self.vedomosti_level=0
		self.vedomosti_modifier=self.sport_level*2.75

		#proměnné, které jsou závislé na jiných faktorech
		self.plat=15500 #plat na jednoho učitele
		self.pocet_zaku=120	#počet žáků školy
		self.zaci_lvl=1 #proměnná nepřímo závislá na počtu žáků, používá se pro počty při vylepšování školy 
		self.najem=100000 #měsíční nájem za školní budovu
		self.castka=800   #částka, kterou platí každý student na školném
		self.pocet_ucitelu=self.pocet_zaku/10+10 #počet učitelů ve škole
		self.vydaje_na_ucitele= self.pocet_ucitelu*self.plat #celkové výdaje na celý učitelský sbor
		self.skolne=self.castka*self.pocet_zaku	#celková měsíční částka, kterouškola dostane na školném
		
		
		self.main=Tk()
		self.main.attributes("-fullscreen", True) #fullscreen mode
		
		#tlačítka na hlavní obrazovce
		
		self.forward_button=Button(self.main, text="vpřed",command=self.vpred) #posune čas o týden vpřed 
		self.forward_button.pack()
		self.exit_button=Button(self.main, text="opustit hru", command=sys.exit) #ukončí hru
		self.exit_button.pack()
		self.money_button=Button(self.main, text="změnit školné",command=self.zmenit_skolne) #otevře okno na změnu školného
		self.money_button.pack()
		self.upgrade_button=Button(self.main,text="vylepšení",command=self.upgrades) #otevře okno s vylepšeními školního vybavení
		self.upgrade_button.pack()
		self.plat_button=Button(self.main,text="změnit platy",command=self.zmenit_platy) #otevře okno na změnu učitelských platů
		self.plat_button.pack()
		
		#nápisy
		
		self.week_info=Label(self.main, text="týden: " + str (self.tyden)) #píše kolikátý je týden od začátku hry
		self.week_info.pack()
		self.money_info=Label(self.main, text="finance: " + str (self.penize)+"kč") #píše stav konta školy
		self.money_info.pack()
		self.studenti_info=Label(self.main,text="spokojenost studentů: " + str(self.studenti_spokojenost)) #píše spokojenost žáků
		self.studenti_info.pack()
		self.ucitele_info=Label(self.main,text="spokojenost učitelů: " + str(self.ucitele_spokojenost)) #píše spokojenost učitelů
		self.ucitele_info.pack()
		self.rodice_info=Label(self.main,text="spokojenost rodičů: " + str(self.rodice_spokojenost)) #píše spokojenost rodičů
		self.rodice_info.pack()
		self.teacher_count=Label(self.main,text="počet učitelů: "+str(self.pocet_ucitelu)) #píše počet učitelů na škole
		self.teacher_count.pack()
		self.teacher_salary=Label(self.main,text="plat učitel/měsíc: "+str(self.plat)+"kč") #píše plat na jednoho učitele
		self.teacher_salary.pack()
		self.student_count=Label(self.main,text="počet žáků: "+str(self.pocet_zaku)) #píše počet žáků
		self.student_count.pack()
		self.student_income=Label(self.main,text="školné žák/měsíc: "+str(self.castka)+"kč") #píše školné, které platí každý žák za měsíc
		self.student_income.pack()
		self.building_expenses=Label(self.main,text="měsíční nájem: "+ str(self.najem)+"kč") #píše měsíční nájem
		self.building_expenses.pack()
#----------------------------------------------------------------------------------------------------------------

	def game_over_finance(self): #funkce na konec hry kvůli financím
		self.popupmsg("konec hry, Škola zkrachovala, zkus to znovu")
		return
		
	def game_over_puc(self): #funkce na konec hry kvůli znepřátelení osazenstva školy/rodičů
		self.popupmsg("konec hry, byl jsi sesazen kombinovanou mocí svých poddaných")
		return
		
	def game_over_gut(self): #funkce na "šťastný konec hry"
		self.popupmsg("konec hry, šťastně jsi dokázal vést svou školu po dobu dvou let! Gratulujeme")
		return
	
	def popupmsg(self,msg):  #custom msgbox
		self.popup=Toplevel()
		self.popup.grab_set() #aby uživatel nemohl do hlavního okna než vyřeší popup
		self.popup.geometry("500x150+50+50")
		#self.popup.wm_title("pozor")
		self.label=Label(self.popup, text=msg)
		self.label.pack(side="top",fill="x", pady=10)
		self.b1=Button(self.popup,text="OK",command=self.popup.destroy) #ok tlačítko, zavírá popup
		self.b1.pack()
		return
	
	def upgrades(self): #okno, kde se dá vylepšovat školní vybavení
		self.upg=Toplevel()
		self.upg.grab_set()
		#self.upg.attributes("-fullscreen",True)
		
		##info
		self.sport_info=Label(self.upg,text="úroveň sportovního vybavení: "+str(self.sport_level)) #info o levelu sportovního vybavení
		self.sport_info.pack()
		self.veda_info=Label(self.upg,text="úroveň vědeckého vybavení: "+str(self.veda_level)) #info o levelu vědeckého vybavení
		self.veda_info.pack()
		self.vedomosti_info=Label(self.upg,text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level)) #info o levelu učebního vybavení
		self.vedomosti_info.pack()
		self.kapacita_info=Label(self.upg,text="maximální kapacita žáků je: "+str(self.pocet_zaku)) #info o počtu žáků
		self.kapacita_info.pack()
		
		##tlačítka na vylepšení
		self.sport_button=Button(self.upg,text="vylepšit sportovní vybavení",command=self.sport_upgrade) #tlačítko na vylepšení sportovního vybavení
		self.sport_button.pack()
		self.veda_button=Button(self.upg,text="vylepšit vědecké vybavení",command=self.veda_upgrade) #tlačítko na vylepšení vědeckého vybavení 
		self.veda_button.pack()
		self.vedomosti_button=Button(self.upg,text="vylepšit učební pomůcky",command=self.vedomosti_upgrade) #tlačítko na vylepšení učebních pomůcek
		self.vedomosti_button.pack()
		self.capacity_button=Button(self.upg,text="zvýšit kapacitu školy",command=self.expand) #tlačítko na zvětšení školy
		self.capacity_button.pack()
		##zpět
		self.b1=Button(self.upg,text="zpět",command=self.upg.destroy) #tlačítko zavírající okno
		self.b1.pack()
		return
	
	def expand(self): #funkce zvyšující kapacitu budovy
		self.penize=self.penize-((self.zaci_lvl+1)*1050000) #počítání ceny na základě stávajícího počtu žáků
		self.money_info.config(text="finance: " + str (self.penize)+"kč")
		self.zaci_lvl+=1 
		self.ucitele_spokojenost-=5 #sníží spokojenost učitelů, protože nemají rádi na starost víc lidí
		self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
		self.pocet_zaku+=40 #přidá kapacitu škole (+40 žáků)
		self.kapacita_info.config(text="maximální kapacita žáků je: "+str(self.pocet_zaku))
	
	def sport_upgrade(self): #funkce zvyšující úroveň sportovního vybavení
		self.penize=self.penize-((self.sport_level+1)*10000) #počítání ceny a odečítání peněz na základě stávajícího lvlu vybavení
		self.money_info.config(text="finance: " + str (self.penize)+"kč")
		self.sport_level+=1
		self.studenti_spokojenost+=10  #úpravy spokojeností
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=5
		self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))  #úpravy infolabelů v hlavním okně
		self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
		self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		self.sport_info.config(text="úroveň sportovního vybavení: "+str(self.sport_level))
		self.money_info.config(text=str(self.penize))
		return
	
	def veda_upgrade(self):
		self.penize=self.penize-((self.veda_level+1)*10000)
		self.money_info.config(text="finance: " + str (self.penize)+"kč")
		self.veda_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=10
		self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
		self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
		self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		self.veda_info.config(text="úroveň vědeckého vybavení: "+str(self.veda_level))
		self.money_info.config(text=str(self.penize))
		return
		
	def vedomosti_upgrade(self):
		self.penize=self.penize-((self.vedomosti_level+1)*10000)
		self.money_info.config(text="finance: " + str (self.penize)+"kč")
		self.vedomosti_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=10
		self.ucitele_spokojenost+=5
		self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
		self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
		self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		self.vedomosti_info.config(text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level))
		self.money_info.config(text=str(self.penize))
		return
		

	def zmenit_skolne(self):
		self.skol=Toplevel()
		self.skol.grab_set()
		self.skol.geometry("500x150+50+50")
		self.infolabel=Label(self.skol, text="stávající školné na žáka na měsíc je "+str(self.castka)+" kč")
		self.infolabel.pack()
		self.low=Label(self.skol,text="moc nízká hondota")
		self.high=Label(self.skol,text="moc vysoká hodnota")
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
			self.student_income.config(text="školné žák/měsíc: "+str(self.castka)+"kč")
			self.student_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.skol.destroy()
			#self.potvrzeni=Label(self.ent, text="školné aktualizováno")
		elif (self.s_output<400):
			self.low.pack()
		elif (self.s_output>1500):
			self.high.pack()
			
			return
		
	def zmenit_platy(self):
		self.plat_wndw=Toplevel()
		self.plat_wndw.grab_set()
		self.plat_wndw.geometry("500x150+50+50")
		self.pocet_label=Label(self.plat_wndw,text="počet učitelů: "+str(self.pocet_ucitelu)).pack()
		self.teacher_min_salary=Label(self.plat_wndw,text="minimální plat: "+str(self.min_salary)).pack()
		self.plat_label=Label(self.plat_wndw,text="plat na jednoho učitele: "+str(self.plat)).pack()
		self.naklady_label=Label(self.plat_wndw,text="celkové náklady na učitele: "+str(self.vydaje_na_ucitele)).pack()
		self.error_line=Label(self.plat_wndw,text="neplatná hodnota")
		self.p_entry=Entry(self.plat_wndw, width=150)
		self.p_entry.pack()
		self.p_entry.focus_set()
		self.b1=Button(self.plat_wndw,text="Storno",command=self.plat_wndw.destroy)
		self.b1.pack()
		self.b2=Button(self.plat_wndw,text="Potvrdit", command=self.p_zmen)# and self.entry.delete(0,"end")) #self.entry.get()))
		self.b2.pack()	
		
	def p_zmen(self):
		self.p_output=int(self.p_entry.get())
		if (self.p_output>self.min_salary):
			self.plat=self.p_output
			self.teacher_salary.config(text="plat učitel/měsíc: "+str(self.plat)+"kč")
			self.plat_wndw.destroy()
			self.ucitele_spokojenost+=self.p_output/300
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			#self.potvrzeni=Label(self.ent, text="školné aktualizováno")
			return
		else:
			self.error_line.pack()
	
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
			if (self.penize+self.skolne)-(self.vydaje_na_ucitele+self.najem)<0:
				self.game_over_finance()
			elif self.studenti_spokojenost<15 and self.ucitele_spokojenost<15 or self.studenti_spokojenost<15 and self.rodice_spokojenost<15 or self.rodice_spokojenost<15 and self.ucitele_spokojenost<15: #kontrola spokojenosti na začátku každého měsíce
				self.game_over_puc()
			else:
				self.penize=self.penize-(self.vydaje_na_ucitele+self.najem)+self.skolne   #když škola nezkrachovala, tak se odečtou náklady
				self.money_info.config(text="finance: " + str (self.penize)+"kč")
		if self.studenti_spokojenost<=25:	#varování kvůli nespokojenosti nějaké skupiny
			self.popupmsg("studenti jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat")
			return
		if self.rodice_spokojenost<=25:
			self.popupmsg("rodiče jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat")
			return
		if self.ucitele_spokojenost<=25:
			self.popupmsg("ucitele jsou vrcholně nespokojeni. Vyplatilo by se s tím něco udělat")
			return
		
		##meziškolní soutěže 

		if self.calm_week+randint(0,10)>=15:
			self.calm_week=0
			self.competition()
		else:
			self.calm_week+=1
		
		##random events
		
		if randint(0,10)<4 and self.calm_week!=0:
			self.random_event()
	"""	
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
	"""

	def competition(self):       ####meziškolní soutěže
		self.place=1
		self.typ=randint(1,3)
		if (self.typ==1):
			self.competition_type=self.vzdel_souteze[randint(0,6)]
			self.competition_modifier=self.vedomosti_modifier
		elif(self.typ==2):
			self.competition_type=self.sport_souteze[randint(0,6)]
			self.competition_modifier=self.sport_modifier
		else:
			self.competition_type=self.veda_souteze[randint(0,6)]
			self.competition_modifier=self.veda_modifier

		self.soutez_okno=Toplevel()
		self.soutez_okno.grab_set()
		self.soutez_label=Label(self.soutez_okno,text="V týdnu se konal"+str(self.competition_type))
		self.soutez_label.pack()
		self.result_label=Label(self.soutez_okno,text="")
		self.result_label.pack()
		self.prize_label=Label(self.soutez_okno,text="")
		self.prize_label.pack()
		self.ok_b=Button(self.soutez_okno,text="ok",command=self.soutez_okno.destroy)
		self.ok_b.pack()
		self.playerschool=randint(0,100)+int(self.competition_modifier)
		self.pos_values=[]
		for i in range (0,100):	#aby NPC škola nemohla mít stejné skóre jako hráč
			self.pos_values.append(i)
		self.pos_values.remove(self.playerschool)
		
		self.school1=self.pos_values[randint(0,len(self.pos_values)-1)]
		self.school2=self.pos_values[randint(0,len(self.pos_values)-1)]
		self.school3=self.pos_values[randint(0,len(self.pos_values)-1)]
		
		self.results=[self.playerschool,self.school1,self.school2,self.school3]
		
		while (max(self.results)!=self.playerschool):
			self.results.remove(max(self.results))
			self.place+=1
			
		self.prize=500*randint(1,50)
		if self.place==2:
			self.prize=self.prize*0.75
		elif self.place==3:
			self.prize=self.prize*0.5
		elif self.place==4:
			self.prize=self.prize*0
			
		if max(self.results)==self.playerschool:
			self.result_label.config(text="Tvoje škola skončila "+str(self.place)+".")
			self.prize_label.config(text="Získal jsi finanční odměnu v hodnotě "+str(self.prize))
			self.penize=self.penize+self.prize
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			self.rodice_spokojenost+=5
			self.ucitele_spokojenost+=5 
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
		
	def random_event(self):
		self.random_wndw=Toplevel()
		self.random_wndw.grab_set()
		self.event_type=randint(0,13)	
		if self.event_type==0:
			self.event_text="Školní inspekce odhalila vady na vybavení školy. Musíš okamžitě vynaložit prostředky na opravu."
			self.consequence1="peníze - "+str(40000+self.zaci_lvl*8000)
			self.consequence2="spokojenost rodičů - 10"
			self.consequence3="spokojenost učitelů - 10"
			self.consequence4="spokojenost žáků - 10"
			self.penize=self.penize-(40000+self.zaci_lvl*8000)
			self.rodice_spokojenost=self.rodice_spokojenost-10
			self.ucitele_spokojenost=self.ucitele_spokojenost-10
			self.studenti_spokojenost=self.studenti_spokojenost-10
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==1:
			self.event_text="Vypověděl službu jeden z kotlů na teplou vodu. Ve škole teče jen studená voda a je třeba urychleně investovat do nového kotle."
			self.consequence1="peníze - 100000"
			self.consequence2="spokojenost žáků - 10"
			self.consequence3="spokojenost učitelů - 10"
			self.penize-=100000
			self.studenti_spokojenost=self.studenti_spokojenost-10
			self.ucitele_spokojenost=self.ucitele_spokojenost-10
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
		elif self.event_type==2:
			self.event_text="Studenti vytopili záchody, je třeba je opravit a potrestat viníky"
			self.consequence1="peníze - 5000"
			self.consequence2="spokejenost studentů - 5"
			self.consequence3="spokojenost učitelů + 5"
			self.consequence4="spokojenost rodičů - 5"
			self.penize-=5000
			self.studenti_spokojenost-=5
			self.ucitele_spokojenost+=5
			self.rodice_spokojenost-=5
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==3:
			self.event_text="Výpadek elektřiny, studenti i učitelé šli dřív domů"
			self.consequence1="spokojenost studentů + 5"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost rodičů - 5"
			self.studenti_spokojenost+=5
			self.ucitele_spokojenost+=5
			self.rodice_spokojenost-=5
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==4:
			self.event_text="Navýšení minimální mzdy: Minimální mzda je odteď "+str(self.min_salary+800)
			self.consequence1="spokojenost učitelů + 10"
			self.spokojenost_ucitelu+=10
			self.min_salary+=800
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
		elif self.event_type==5:
			self.event_text="Stala se nehoda v chemické laboratoři, bude nepoužitelná, dokud se neopraví"
			self.consequence1="level vědeckého vybavení - 1"
			self.consequence2="spokojenost učitelů - 5"
			self.consequence3="spokojenost žáků - 5"
			self.consequence4="spokojenost rodičů - 5"
			self.veda_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==6:
			self.event_text="Při kontrole se zjistilo, že školní učebnice jsou zastaralé a velké množství se jich muselo vyhodit"
			self.consequence1="level učebního vybavení - 1"
			self.consequence2="spokojenost učitelů - 5"
			self.consequence3="spokojenost žáků - 5"
			self.consequence4="spokojenost rodičů - 5"
			self.vedomosti_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==7:
			self.event_text="Při velké bouřce se zničilo školní multifunkční hřiště"
			self.consequence1="level sportovního vybavení - 1"
			self.consequence2="spokojenost učitelů - 5"
			self.consequence3="spokojenost žáků - 5"
			self.consequence4="spokojenost rodičů - 5"
			self.vedomosti_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==8:
			self.event_text="škola obrdžela grant na sportovní vybavení"
			self.consequence1="level sportovního vybavení + 1"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost žáků + 5"
			self.consequence4="spokojenost rodičů + 5"
			self.sport_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==9:
			self.event_text="škola obrdžela grant na vědecké vybavení"
			self.consequence1="level vědeckého vybavení + 1"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost žáků + 5"
			self.consequence4="spokojenost rodičů + 5"
			self.veda_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==10:
			self.event_text="škola obrdžela grant na učební vybavení"
			self.consequence1="level vědeckého vybavení + 1"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost žáků + 5"
			self.consequence4="spokojenost rodičů + 5"
			self.veda_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.ucitele_info.config(text="spokojenost učitelů: " + str(self.ucitele_spokojenost))
			self.studenti_info.config(text="spokojenost studentů: " + str(self.studenti_spokojenost))
			self.rodice_info.config(text="spokojenost rodičů: " + str(self.rodice_spokojenost))
		elif self.event_type==11:
			self.h=randint(1,30)*1000
			self.event_text="škola obdržela mimořádnou dotaci"
			self.consequence1="peníze + "+str(self.h) 
			self.penize=self.penize+self.h
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
		elif self.event_type==12:
			self.k=randint(5,25)*1000
			self.event_text="škole byl zvýšen nájem o "+str(self.k)+" měsíčně"
			self.consequence1="měsíční nájem + "+str(self.k)
			self.najem=self.najem+self.k
			self.building_expenses.config(text="měsíční nájem: "+ str(self.najem)+"kč")
		elif self.event_type==13:
			self.k=randint(5,30)*1000
			self.event_text="škole byl snížen nájem o "+str(self.k)+" měsíčně"
			self.consequence1="měsíční nájem - "+str(self.k)
			self.najem=self.najem-self.k
			self.building_expenses.config(text="měsíční nájem: "+ str(self.najem)+"kč")
		self.gen_label=Label(self.random_wndw,text=self.event_text)
		self.gen_label.pack()
		self.consequence_label=Label(self.random_wndw,text=self.consequence1)
		self.consequence_label.pack()
		if "self.consequence2" in locals():
			self.consequence2_label=Label(self.random_wndw,text=self.consequence2)
			self.consequence2_label.pack()
		if "self.consequence3" in locals():
			self.consequence3_label=Label(self.random_wndw,text=self.consequence3)
			self.consequence3_label.pack()
		if "self.consequence4" in locals():
			self.consequence4_label=Label(self.random_wndw,text=self.consequence4)
			self.consequence4_label.pack()
		self.ok=Button(self.random_wndw,text="ok",command=self.random_wndw.destroy)
		self.ok.pack()
		
lol=main()
mainloop()
