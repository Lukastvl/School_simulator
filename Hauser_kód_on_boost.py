#coding: utf-8

#----------------------------------------------------------------------------------------------------------------
#importy
from random import randint
from sys import exit
from Tkinter import *
import tkFont
from PIL import Image,ImageTk

#----------------------------------------------------------------------------------------------------------------
#konstruktor
class root:
	def __init__(self):
#----------------------------------------------------------------------------------------------------------------
#proměnné
#---------------------------------------------------------------------------------------------------------------- 
		self.vzdel_souteze=[
			" soutěž v matematicu",	#seznam vědomostních meziškolních soutěží
			" biologická olympiáda",
			" matematická olympiáda",
			" fyzikální olympiáda",
			" soutěž matematický klokan",
			" soutěž Pražský glóbus",
			" zeměpisná olympiáda",
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
			" soutěž v rychlomíchání chemických sloučenin",
			" robosoutěž",
			" soutěž školních časopisů",
			" soutěž v navrhování fyzikálních experimentů",
			" soutěž mladých inženýrů",
			" soutěž mladých designérů",
			" soutěž v rychlopitvách ježků",
		]
		
		self.trophy_list=[] #prázdný seznam, používá se v okně pro trofeje
		
		self.tyden=1   #kolikátý týden se píše od hráčova nástupu do funkce ředitele
		self.calm_week=0 #kolik týdnů se nekonala žádná meziškolní soutěž
		self.penize=1000000000000000000 #kolik má škola na účtě, integer aby se z toho nedělal float a na obrazovce nebylo x.0
		self.min_salary=23000 #minimální plat pro učitele
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
		self.plat=28650 #plat na jednoho učitele
		self.pocet_zaku=120	#počet žáků školy
		self.zaci_lvl=1 #proměnná nepřímo závislá na počtu žáků, používá se pro počty při vylepšování školy 
		self.najem=100000 #měsíční nájem za školní budovu
		self.castka=800   #částka, kterou platí každý student na školném
		self.pocet_ucitelu=self.pocet_zaku/10+10 #počet učitelů ve škole
		self.vydaje_na_ucitele= self.pocet_ucitelu*self.plat #celkové výdaje na celý učitelský sbor
		self.skolne=self.castka*self.pocet_zaku	#celková měsíční částka, kterouškola dostane na školném
		
		
		self.main=Tk() 
		#fonty		
		self.l_font=tkFont.Font(family="comic sans",size=16)
		self.buttonFont=tkFont.Font(family="comic sans",size=22,weight=tkFont.BOLD)		
		self.label_font=tkFont.Font(family="comic sans",size=16) #font na nápis
		
		#nápisy
		self.label_frame=Frame(self.main) #rámeček na nápisy
		self.label_frame.grid(row=2,column=1)
		self.week_info=Label(self.label_frame,font=self.label_font, text="týden: ") #píše kolikátý je týden od začátku hry
		self.week_info.grid(column=0,row=0,sticky=W)
		self.week_int=Label(self.label_frame,font=self.label_font,fg="red",text=self.tyden)
		self.week_int.grid(column=1,row=0,sticky=W)
		self.money_info=Label(self.label_frame,font=self.label_font, text="finance: ") #píše stav konta školy
		self.money_info.grid(column=0,row=1,sticky=W)
		self.money_int=Label(self.label_frame,font=self.label_font,fg="red",text=self.penize)
		self.money_int.grid(column=1,row=1,sticky=W)
		self.building_expenses=Label(self.label_frame,font=self.label_font,text="měsíční nájem: ") #píše měsíční nájem
		self.building_expenses.grid(column=0,row=6,sticky=W)
		self.building_int=Label(self.label_frame,font=self.label_font,fg="red",text=self.najem)
		self.building_int.grid(column=1,row=6,sticky=W)

		self.alt_frame=Frame(self.main)
		self.alt_frame.grid(row=1,column=2)
		self.teacher_count=Label(self.alt_frame,font=self.label_font,text="počet učitelů: ") #píše počet učitelů na škole
		self.teacher_count.grid(column=0,row=2,sticky=W)
		self.teacher_int=Label(self.alt_frame,font=self.label_font,fg="red",text=self.pocet_ucitelu)
		self.teacher_int.grid(column=1,row=2,sticky=W)
		self.teacher_salary=Label(self.alt_frame,font=self.label_font,text="plat učitel/měsíc: ") #píše plat na jednoho učitele
		self.teacher_salary.grid(column=0,row=3,sticky=W)
		self.teacher_sint=Label(self.alt_frame,font=self.label_font,fg="red",text=self.plat)
		self.teacher_sint.grid(column=1,row=3,sticky=W)
		self.student_count=Label(self.alt_frame,font=self.label_font,text="počet žáků: ") #píše počet žáků
		self.student_count.grid(column=0,row=4,sticky=W)
		self.student_int=Label(self.alt_frame,font=self.label_font,fg="red",text=self.pocet_zaku)
		self.student_int.grid(column=1,row=4,sticky=W)
		self.student_income=Label(self.alt_frame,font=self.label_font,text="školné žák/měsíc: ") #píše školné, které platí každý žák za měsíc
		self.student_income.grid(column=0,row=5,sticky=W)
		self.student_castka=Label(self.alt_frame,font=self.label_font,fg="red",text=self.castka)
		self.student_castka.grid(column=1,row=5,sticky=W)

		#spokojenosti
		
		self.sa_frame=Frame(self.main)#rámeček kvůli grafickému rozmístění
		self.sa_frame.grid(row=2,column=0,sticky=N+E+W+S)
		self.studenti_info=Label(self.sa_frame,font=self.label_font,text="spokojenost studentů: ")#píše spokojenost žáků
		self.studenti_info.grid(column=0,row=0)
		self.ucitele_info=Label(self.sa_frame,font=self.label_font,text="spokojenost učitelů: ")#píše spokojenost učitelů
		self.ucitele_info.grid(column=0,row=1)
		self.rodice_info=Label(self.sa_frame,font=self.label_font,text="spokojenost rodičů: ")#píše spokojenost rodičů
		self.rodice_info.grid(column=0,row=2)
		self.studenti_canvas=Canvas(self.sa_frame,background="white",width=200, height=15)
		self.stangle=self.studenti_canvas.create_rectangle(0,0,self.studenti_spokojenost*2,17,fill="green",width=0)
		self.stext=self.studenti_canvas.create_text(94,2,anchor=NW,text=self.studenti_spokojenost)
		self.studenti_canvas.grid(column=1,row=0)
		self.ucitele_canvas=Canvas(self.sa_frame,background="white",width=200,height=15)
		self.utangle=self.ucitele_canvas.create_rectangle(0,0,self.ucitele_spokojenost*2,17,fill="green",width=0)
		self.utext=self.ucitele_canvas.create_text(94,2,anchor=NW,text=self.ucitele_spokojenost)
		self.ucitele_canvas.grid(column=1,row=1)
		self.rodice_canvas=Canvas(self.sa_frame,background="white",width=200,height=15)
		self.rtangle=self.rodice_canvas.create_rectangle(0,0,self.rodice_spokojenost*2,17,fill="green",width=0)
		self.rtext=self.rodice_canvas.create_text(94,2,anchor=NW,text=self.rodice_spokojenost)
		self.rodice_canvas.grid(column=1,row=2)
		
		#tlačítka na hlavní obrazovce
		self.button_frame=Frame(self.main) #rámeček kvůli grafickému rozmístění
		self.button_frame.grid(row=0,column=2,sticky=E+W)
		self.money_button=Button(self.button_frame,height=2,font=self.buttonFont, text="změnit školné",command=self.zmenit_skolne) #otevře okno na změnu školného
		self.money_button.grid(column=0,row=2,sticky=E+W)
		self.upgrade_button=Button(self.button_frame,height=2,font=self.buttonFont,text="vylepšení",command=self.upgrades) #otevře okno s vylepšeními školního vybavení
		self.upgrade_button.grid(column=0,row=3,sticky=E+W)
		self.plat_button=Button(self.button_frame,height=2,font=self.buttonFont,text="změnit platy",command=self.zmenit_platy) #otevře okno na změnu učitelských platů
		self.plat_button.grid(column=0,row=4,sticky=E+W)
		self.trophy_button=Button(self.button_frame,height=2,font=self.buttonFont,text="skříňka s trofejemi",command=self.trophies) #otevírá okno se školními poháry
		self.trophy_button.grid(column=0,row=5,sticky=E+W)
		
		#obrázek ředitelny
		self.image=Image.open("reditelna.jpg")
		self.img=ImageTk.PhotoImage(self.image)
		self.img_label=Label(self.main,image=self.img)
		self.img_label.image=self.img
		self.img_label.grid(row=0,column=0,columnspan=2,rowspan=2)

		#vpřed a opustit hru
		self.admin_frame=Frame(self.main)
		self.admin_frame.grid(row=2,column=2,sticky=W+E)
		
		#tlačítko vpřed
		self.forwardbuttonfont=tkFont.Font(family="comic sans",size=36,weight=tkFont.BOLD)
		self.forward_button=Button(self.admin_frame,font=self.forwardbuttonfont, text="vpřed",command=self.vpred) #posune čas o týden vpřed 
		self.forward_button.grid(column=0,row=0,sticky=E+W)
		
		#tlačítko opustit hru
		self.leavebuttonfont=tkFont.Font(family="comic sans",size=14,weight=tkFont.BOLD)
		self.exit_button=Button(self.admin_frame,font=self.leavebuttonfont, text="opustit hru", command=sys.exit) #ukončí hru
		self.exit_button.grid(column=0,row=1,sticky=E+W)
				
		self.main.update()
		self.screen_width = self.main.winfo_screenwidth()
		self.screen_height = self.main.winfo_screenheight()
		self.center(self.main)
		
#----------------------------------------------------------------------------------------------------------------
	def refresh(self): #funkce kontrolující obsah okna
		self.week_int.config(text=self.tyden)
		self.money_int.config(text=self.penize)
		self.building_int.config(text=self.najem)
		self.teacher_int.config(text=self.pocet_ucitelu)
		self.teacher_sint.config(text=self.plat)
		self.student_int.config(text=self.pocet_zaku)
		self.student_castka.config(text=self.castka)
		
		#úpravy spokojeností
		self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
		self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)
		self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
		self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
		self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
		self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		
	def center(self,win): #funkce,která vycentruje současné okno
		win.update()
		w_req, h_req = win.winfo_width(), win.winfo_height()
		w_form = win.winfo_rootx() - win.winfo_x()
		w = w_req + w_form*2
		h = h_req + (win.winfo_rooty() - win.winfo_y()) + w_form
		x = (win.winfo_screenwidth() // 2) - (w // 2)
		y = (win.winfo_screenheight() // 2) - (h // 2)
		win.geometry('{0}x{1}+{2}+{3}'.format(w_req, h_req, x, y))
		
	def game_over_finance(self): #funkce na konec hry kvůli financím
		self.popupmsg("konec hry, Škola zkrachovala, zkus to znovu")
		
	def game_over_odvolani(self): #funkce na konec hry kvůli znepřátelení osazenstva školy/rodičů
		self.popupmsg("konec hry, byl jsi sesazen kombinovanou mocí svých podřízených")
		
	def game_over_gut(self): #funkce na "šťastný konec hry"
		self.popupmsg("konec hry, šťastně jsi dokázal vést svou školu po dobu dvou let! Gratulujeme")
	
	def popupmsg(self,msg):  #custom msgbox
		self.popup=Toplevel()
		self.popup.grab_set() #aby uživatel nemohl do hlavního okna než vyřeší popup
		self.center(self.popup) #vycentruje doprostřed
		self.label=Label(self.popup, text=msg)
		self.label.pack(side="top",fill="x", pady=10)
		self.b1=Button(self.popup,text="OK",command=self.end) #ok tlačítko, zavírá popup
		self.b1.pack()
		self.center(self.popup)
	
	def trophies(self): #okno, kde se ukazují všechny trofeje, které hráčova škola vyhrála
		self.trp=Toplevel()
		self.trp.grab_set()
		self.row_index=0
		self.list_len=len(self.trophy_list)
		if self.list_len==0:
			self.empty=Label(self.trp,font=self.label_font,text="Tvoje škola zatím nemá žádné trofeje! Vylepši něco a tvoji studenti budou úspěšnější")
			self.empty.grid(row=0,column=0,padx=30,pady=20)
		for	x in range (len(self.trophy_list)):
			self.trp_lbl=Label(self.trp,text=self.trophy_list[x])
			self.trp_lbl.grid(row=self.row_index,font=self.label_font,column=0,padx=10,pady=10)
			self.row_index+=1
		self.btn=Button(self.trp,font=self.label_font,text="ok",command=self.trp.destroy)
		self.btn.grid()
		self.center(self.trp)
			
		
	def end(self): #funkce uzavírající jak popupmsg, tak hru. Volá se při konci hry
		self.popup.destroy()
		self.main.destroy()
		
	def upgrades(self): #okno, kde se dá vylepšovat školní vybavení
		self.upg=Toplevel()
		self.upg.grab_set()
		
		##info
		self.sport_info=Label(self.upg,font=self.label_font,text="úroveň sportovního vybavení: "+str(self.sport_level)) #info o levelu sportovního vybavení
		self.sport_info.grid(row=0,column=0,padx=20,pady=10)#,sticky=W)
		self.sport_button=Button(self.upg,font=self.label_font,text="vylepšit sportovní vybavení",command=self.sport_upgrade) #tlačítko na vylepšení sportovního vybavení
		self.sport_button.grid(row=0,column=1,padx=10,pady=10,sticky=W+E)#,sticky=E+W)
	
		self.veda_info=Label(self.upg,font=self.label_font,text="úroveň vědeckého vybavení: "+str(self.veda_level)) #info o levelu vědeckého vybavení
		self.veda_info.grid(row=1,column=0,padx=20,pady=10)#,sticky=W)
		self.veda_button=Button(self.upg,font=self.label_font,text="vylepšit vědecké vybavení",command=self.veda_upgrade) #tlačítko na vylepšení vědeckého vybavení 
		self.veda_button.grid(row=1,column=1,padx=10,pady=10,sticky=W+E)
				
		self.vedomosti_info=Label(self.upg,font=self.label_font,text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level)) #info o levelu učebního vybavení
		self.vedomosti_info.grid(row=2,column=0,padx=20,pady=10)#,sticky=W)
		self.vedomosti_button=Button(self.upg,font=self.label_font,text="vylepšit učební pomůcky",command=self.vedomosti_upgrade) #tlačítko na vylepšení učebních pomůcek
		self.vedomosti_button.grid(row=2,column=1,padx=10,pady=10,sticky=W+E)
		
		self.capacity_info=Label(self.upg,font=self.label_font,text="maximální kapacita žáků je: "+str(self.pocet_zaku)) #info o počtu žáků
		self.capacity_info.grid(row=3,column=0,padx=20,pady=10)#,sticky=W)
		self.capacity_button=Button(self.upg,font=self.label_font,text="zvýšit kapacitu školy",command=self.expand) #tlačítko na zvětšení školy
		self.capacity_button.grid(row=3,column=1,padx=10,pady=10,sticky=W+E)
		
		##zpět
		self.b1=Button(self.upg,font=self.label_font,text="zpět",command=self.upg.destroy) #tlačítko zavírající okno
		self.b1.grid(row=4,column=0,columnspan=2,padx=20,pady=10)#,sticky=E+W)
		self.center(self.upg)
	
	def expand(self): #funkce zvyšující kapacitu budovy
		self.penize=self.penize-((self.zaci_lvl+1)*1050000) #počítání ceny na základě stávajícího počtu žáků
		self.money_int.config(text=self.penize)
		self.zaci_lvl+=1 
		self.ucitele_spokojenost-=5 #sníží spokojenost učitelů, protože nemají rádi na starost víc lidí
		self.pocet_zaku+=40 #přidá kapacitu škole (+40 žáků)
		self.refresh()
		self.kapacita_info.config(text="maximální kapacita žáků je: "+str(self.pocet_zaku))
	
	def sport_upgrade(self): #funkce zvyšující úroveň sportovního vybavení
		self.penize=self.penize-((self.sport_level+1)*10000) #počítání ceny a odečítání peněz na základě stávajícího lvlu vybavení
		self.sport_level+=1
		self.studenti_spokojenost+=10  #úpravy spokojeností
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=5
		self.refresh() #upravit všechny nápisy v hlavním okně
		self.sport_info.config(text="úroveň sportovního vybavení: "+str(self.sport_level))
		return
	
	def veda_upgrade(self): #funkce zvyšující úroveň vědeckého vybavení
		self.penize=self.penize-((self.veda_level+1)*10000) #dynamciká cena odvíjející se od současného lvlu vybavení
		self.veda_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=10
		self.refresh() #upravit všechny nápisy v hlavním okně
		self.veda_info.config(text="úroveň vědeckého vybavení: "+str(self.veda_level))
		return
		
	def vedomosti_upgrade(self): #funkce zvyšující úroveň učebních pomůcek
		self.penize=self.penize-((self.vedomosti_level+1)*10000)
		self.vedomosti_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=10
		self.ucitele_spokojenost+=5
		self.refresh() #upravit všechny nápisy v hlavním okně
		self.vedomosti_info.config(text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level))
		return
		

	def zmenit_skolne(self): #definuje okno, které umožňuje měnit školné 
		self.skol=Toplevel()
		self.skol.grab_set()
		self.infolabel=Label(self.skol,font=self.l_font, text="Stávající školné na žáka na měsíc je "+str(self.castka)+" kč")
		self.infolabel.grid(column=1,row=0,padx=10,pady=5)#,columnspan=2)
		self.low=Label(self.skol,font=self.l_font,foreground="red",text="moc nízká hodnota") #definice textu pro případ zadání neplatné hodnoty hráčem
		self.high=Label(self.skol,font=self.l_font,fg="red",text="moc vysoká hodnota")
		self.entry_width=self.infolabel.winfo_width()
		self.s_entry=Entry(self.skol,font=self.l_font)
		self.s_entry.grid(column=1,row=1,padx=10,pady=5,sticky=N+E+W+S)
		self.s_entry.focus_set() #aby se hned po otevření okna dalo psát do Entry
		self.b1=Button(self.skol, text="Storno",font=self.l_font, command=self.skol.destroy) #tlačítka
		self.b1.grid(column=0,row=1,sticky=N+E+W+S,padx=10,pady=5)
		self.b2=Button(self.skol,text="Potvrdit",font=self.l_font, command=self.s_zmen)
		self.b2.grid(column=0,row=0,sticky=N+E+W+S,padx=10,pady=5)
		self.center(self.skol)
		
	def s_zmen(self): #funkce měnící výši školného
		self.s_output=int(self.s_entry.get()) #vyčtení hodnoty z Entry 
		if (self.s_output>400)and(self.s_output<1500): #kontrola jestli je zadaná hodnota v povoleném rozmezí
			if self.s_output>self.castka:
				self.i=(self.s_output-self.castka)/100
				if self.i==0:
					self.i=1				
				self.rodice_spokojenost=self.rodice_spokojenost+self.i #anticheese
				self.refresh() #upravit všechny nápisy v hlavním okně
			elif self.s_output<self.castka:
				self.i=(self.castka-self.s_output)/100
				if self.i==0:
					self.i=1
				self.rodice_spokojenost=self.rodice_spokojenost-self.i #anticheese
				self.refresh() #upravit všechny nápisy v hlavním okně
			self.castka=self.s_output
			self.student_castka.config(text=self.castka)
			self.skol.destroy()
		elif (self.s_output<400): #když je zadaná hodnota moc nízká, napíše hlášku nadefinovanou v self.zmenit_skolne
			self.low.grid(column=1,row=2)
		elif (self.s_output>1500): #když je zadaná hodnota moc vysoká napíše hlášku nadefinovanou v self.zmenit_skolne
			self.high.grid(column=1,row=2)
			
			return
		
	def zmenit_platy(self): #definuje okno umožňující měnit platy učitelů 
		self.plat_wndw=Toplevel()
		self.plat_wndw.grab_set()
		self.pocet_label=Label(self.plat_wndw,font=self.l_font,text="počet učitelů: "+str(self.pocet_ucitelu))
		self.pocet_label.grid(column=0,row=0,padx=10,pady=10)
		self.teacher_min_salary=Label(self.plat_wndw,font=self.l_font,text="minimální plat: "+str(self.min_salary))
		self.teacher_min_salary.grid(column=0,row=1,padx=10,pady=10)
		self.plat_label=Label(self.plat_wndw,font=self.l_font,text="plat na jednoho učitele: "+str(self.plat))
		self.plat_label.grid(column=1,row=0,padx=10,pady=10)
		self.naklady_label=Label(self.plat_wndw,font=self.l_font,text="celkové náklady na učitele: "+str(self.vydaje_na_ucitele))
		self.naklady_label.grid(column=1,row=1,padx=10,pady=10)
		self.error_line=Label(self.plat_wndw,font=self.l_font,text="neplatná hodnota")
		self.p_entry=Entry(self.plat_wndw,font=self.l_font, width=40)
		self.p_entry.grid(column=0,row=2,columnspan=2,padx=10,pady=10,sticky=E+W)
		self.p_entry.focus_set()
		self.b1=Button(self.plat_wndw,text="Storno",command=self.plat_wndw.destroy) #tlačítko zavírající okno
		self.b1.grid(column=0,row=3,padx=10,pady=10)
		self.b2=Button(self.plat_wndw,text="Potvrdit", command=self.p_zmen) #tlačítko volající funkci, která mění výši platů
		self.b2.grid(column=1,row=3,padx=10,pady=10)
		self.center(self.plat_wndw)
		
	def p_zmen(self): #funkce měnící plat 
		self.p_output=self.p_entry.get() #vyčtení hodnoty zadané hráčem
		if self.p_output!=0:
			if (self.p_output>self.min_salary): #kontrola, zda je zadaná hodnota nad minimálním platem
				if self.p_output>self.plat:
					self.i=(self.p_output-self.plat)/300
					if self.i==0:
						self.i=1
					self.ucitele_spokojenost=self.ucitele_spokojenost+self.i #algorytmus měnící spokojenost učitelů v závislosti na tom, jestli jim bylo přidáno, nebo ubráno
				elif self.p_output<self.plat:
					self.i=(self.plat-self.p_output)/300
					if self.i==0:
						self.i=1
					self.ucitele_spokojenost=self.ucitele_spokojenost-self.i
				self.plat=self.p_output
				self.refresh() #upravit všechny nápisy v hlavním okně 
				self.plat_wndw.destroy() #konec změny, zavření okna
				return
			else:
				self.error_line.grid() #když je neplatná hodnota, objeví se chybová hláška
	
	def vpred(self): #funkce posouvající čas o týden dopředu
		self.game_over=0
		self.tyden+=1
		if self.tyden%44==0: #kontrola, jestli neskončil školní rok
			self.tyden=self.tyden+7 #skok přes prázdniny
		if self.tyden==104: #kontrola, jestli hráči neskončilo funkční obodobí
			self.game_over_gut() # funkce na šťastný konec
			self.game_over=1
		if self.tyden%4==0:  #kontrola, zda škola nezkrachuje při placení nájmu nebo vyplácení platů na konci měsíce 
			if (self.penize+self.skolne)-(self.vydaje_na_ucitele+self.najem)<0: #když je škola ke konci měsíce zadlužená, hráč prohrál
				self.game_over_finance()
				self.game_over=1
			elif self.studenti_spokojenost<15 and self.ucitele_spokojenost<15 or self.studenti_spokojenost<15 and self.rodice_spokojenost<15 or self.rodice_spokojenost<15 and self.ucitele_spokojenost<15: #když jsou dvě skupiny ze tří vrcholně nespokojeny, ředitel bude k začátku příštího měsíce odvolán - hráč prohraje
				self.game_over_odvolani()
				self.game_over=1
			else:
				self.penize=self.penize-(self.vydaje_na_ucitele+self.najem)+self.skolne   #když škola nezkrachovala, tak se odečtou náklady
		if self.studenti_spokojenost<=25:	#varování kvůli nespokojenosti nějaké skupiny
			self.popupmsg("studenti jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat") #varuje hráče před nespokojeností studentů
			return
		if self.rodice_spokojenost<=25:
			self.popupmsg("rodiče jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat") #varuje hráče před nespokojeností rodičů
			return
		if self.ucitele_spokojenost<=25:
			self.popupmsg("ucitele jsou vrcholně nespokojeni. Vyplatilo by se s tím něco udělat") #varuje hráče před nespokojeností učitelů
			return
		
		##meziškolní soutěže 
		if self.game_over!=1:
			if self.calm_week+randint(0,10)>=15: #algorytmus, který kombinuje náhodu a okolnosti. Rozhoduje o tom, jestli se spustí meziškolní soutěž
				self.calm_week=0
				self.competition()
			else:
				self.calm_week+=1
		
		##random events
		if self.game_over!=1:
			if randint(0,10)<4 and self.calm_week!=0: #algorytmus, který spouští náhodné události 
				self.kek=randint(0,13)
				self.random_event(self.kek)
				
		self.refresh() #upravit všechny nápisy v hlavním okně


	def competition(self): #meziškolní soutěže
		self.place=1 #proměnná používaná pro určování umístění hráčovy školy
		self.typ=randint(1,3) 
		if (self.typ==1): #test rozhodující o tom, jestli bude soutěž vědomostní, vědecká, nebo sportovní a taky jaká konkrétní soutěž to bude.
			self.competition_type=self.vzdel_souteze[randint(0,6)]
			self.competition_modifier=self.vedomosti_modifier
		elif(self.typ==2):
			self.competition_type=self.sport_souteze[randint(0,6)]
			self.competition_modifier=self.sport_modifier
		else:
			self.competition_type=self.veda_souteze[randint(0,6)]
			self.competition_modifier=self.veda_modifier

		self.soutez_okno=Toplevel() #definice okna pro soutěže
		self.soutez_okno.grab_set()
		self.soutez_label=Label(self.soutez_okno,text=str(self.competition_type)+"!")
		self.soutez_label.pack()
		self.result_label=Label(self.soutez_okno,text="") #prázdný label, přidá se do něj, kolikátá skončila hráčova škola
		self.result_label.pack()
		self.prize_label=Label(self.soutez_okno,text="") #prázdný label na info o tom, kolik peněz škola vyhrála
		self.prize_label.pack()
		self.ok_b=Button(self.soutez_okno,text="ok",command=self.soutez_okno.destroy) #potvrzovací tlačítko
		self.ok_b.pack()
		self.playerschool=randint(0,100)+int(self.competition_modifier) #náhodné skóre pro školu hráče
		self.pos_values=[] #prázdný seznam na hodnoty NPC škol i hráčovy školy
		for i in range (0,100):	#aby NPC škola nemohla mít stejné skóre jako hráč
			self.pos_values.append(i) #vygenerovaná čísla se dají prázdného seznamu
		self.pos_values.remove(self.playerschool) #hodnota hráčovy školy se odebere ze seznamu, aby hráčova škola nemohla mít stejnou hodnotu jako NPC školy
		
		self.school1=self.pos_values[randint(0,len(self.pos_values)-1)] #pro každou školu se vygeneruje náhodné číslo 
		self.school2=self.pos_values[randint(0,len(self.pos_values)-1)]	#ze seznamu, aby neměly školy stejné hodnoty
		self.school3=self.pos_values[randint(0,len(self.pos_values)-1)]
		self.school4=self.pos_values[randint(0,len(self.pos_values)-1)]
		self.school5=self.pos_values[randint(0,len(self.pos_values)-1)]
		self.school6=self.pos_values[randint(0,len(self.pos_values)-1)]
		
		self.results=[self.playerschool,self.school1,self.school2,self.school3,self.school4,self.school5,self.school6] #všechny hodnoty škol se dají do seznamu 
		
		while (max(self.results)!=self.playerschool): #cyklus zjišťující nejvyšší hodnotu ze seznamu výsledků
			self.results.remove(max(self.results)) #nejvyšší hodnota se smaže ze seznamu
			self.place+=1 #umístění školy se sníží
			
		self.prize=500*randint(1,50) #náhodná peněžní výhra pro školu hráče
		if self.place==2: #když škola neskončí první, peněží výhra se škáluje podle umístění
			self.prize=self.prize*0.75
		elif self.place==3:
			self.prize=self.prize*0.5
		elif self.place==4 or self.place==5 or self.place==6 or self.place==7:
			self.prize=self.prize*0
			
		if max(self.results)==self.playerschool: #když má hráčova škola nejvyšší hodnotu v seznamu, cyklus skončí a spustí se následující kód
			self.result_label.config(text="Tvoje škola skončila "+str(self.place)+".")
			self.prize_label.config(text="Získal jsi finanční odměnu v hodnotě "+str(self.prize))
			self.penize=self.penize+self.prize
			if self.place==1:
				self.ucitele_spokojenost+=5
				self.rodice_spokojenost+=5
				self.refresh() #upravit všechny nápisy v hlavním okně
			if self.place<=3:
				self.exito=str(self.place)+". místo -"+str(self.competition_type)
				self.trophy_list.append(self.exito)
		self.center(self.soutez_okno)
		
	def random_event(self,eve): #funkce simulující náhodné události
		self.event=eve
		if self.event==0:
			self.k=randint(5,30)*1000
			self.najem=self.najem-self.k
			self.event_class1("škole byl snížen nájem o "+str(self.k)+" měsíčně","green","měsíční nájem - "+str(self.k))
		elif self.event==1:
			self.k=randint(5,30)*1000
			self.najem=self.najem+self.k
			self.event_class1("škole byl zvýšen nájem o "+str(self.k)+" měsíčně","red","měsíční nájem + "+str(self.k))
		elif self.event==2:
			self.h=randint(1,30)*1000
			self.penize=self.penize+self.h
			self.event_class1("škola obdržela mimořádnou dotaci","green","peníze + "+str(self.h))
		elif self.event==3:
			self.ucitele_spokojenost+=10
			self.min_salary+=800
			self.event_class1("Navýšení minimální mzdy: Minimální mzda je odteď "+str(self.min_salary+800),"grey","spokojenost učitelů + 10")
		elif self.event==4:
			self.veda_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.event_class4("škola obrdžela grant na učební vybavení","green","level vědeckého vybavení + 1","spokojenost učitelů + 5","spokojenost žáků + 5","spokojenost rodičů + 5")
		elif self.event==5:
			self.penize=self.penize-(20000+self.zaci_lvl*8000) 
			self.rodice_spokojenost-=10
			self.ucitele_spokojenost-=10
			self.studenti_spokojenost-=10
			self.event_class4("Inspekce odhalila vady na vybavení školy. Musíš to okamžitě napravit.","red","peníze - "+str(40000+self.zaci_lvl*8000),"spokojenost rodičů - 10","spokojenost učitelů - 10","spokojenost žáků - 10")
		elif self.event==6:
			self.penize-=100000
			self.studenti_spokojenost-=10
			self.ucitele_spokojenost-=10
			self.event_class3("Vypověděl službu jeden z kotlů na teplou vodu. Je třeba investovat do nového kotle","red","peníze - 100000","spokojenost žáků - 10","spokojenost učitelů - 10")
		elif self.event==7:
			self.penize-=5000
			self.studenti_spokojenost-=5
			self.ucitele_spokojenost+=5
			self.rodice_spokojenost-=5
			self.event_class4("Studenti vytopili záchody, je třeba je opravit a potrestat viníky","red","peníze - 5000","spokejenost studentů - 5","spokojenost učitelů + 5","spokojenost rodičů - 5")
		elif self.event==8:
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5			
			self.event_class3("Výpadek elektřiny, studenti i učitelé šli dřív domů","grey","spokojenost studentů + 5","spokojenost učitelů + 5","spokojenost rodičů - 5")
		elif self.event==9:
			self.veda_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.event_class4("Stala se nehoda v chemické laboratoři, bude nepoužitelná, dokud se neopraví","red","level vědeckého vybavení - 1","spokojenost žáků - 5","spokojenost rodičů - 5","spokojenost učitelů - 5")			
		elif self.event==10:
			self.vedomosti_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.event_class4("Školní učebnice jsou zastaralé a velké množství se jich muselo vyhodit","red","level učebního vybavení - 1","spokojenost učitelů - 5","spokojenost žáků - 5","spokojenost rodičů - 5")
		elif self.event==11:
			self.sport_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.event_class4("Při velké bouřce se zničilo školní multifunkční hřiště","red","level sportovního vybavení - 1","spokojenost učitelů - 5","spokojenost žáků - 5","spokojenost rodičů - 5")
		elif self.event==12:
			self.sport_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.event_class4("škola obrdžela grant na sportovní vybavení","green","level sportovního vybavení + 1","spokojenost učitelů + 5","spokojenost žáků + 5","spokojenost rodičů + 5")
		else:
			self.veda_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.event_class3("škola obrdžela grant na vědecké vybavení","green","level vědeckého vybavení + 1","spokojenost učitelů + 5","spokojenost žáků + 5","spokojenost rodičů + 5")		
				
	def event_class1(self,txt,clr,cons):
		self.refresh()
		self.random_wndw=Toplevel()
		self.random_wndw.grab_set()
		self.random_wndw.configure(background=clr)
		self.event_label=Label(self.random_wndw,bg=clr,font=self.random_font,text=txt)
		self.event_label.grid(row=0,column=0)
		self.consequence_label=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons)
		self.consequence_label.grid(row=1,column=0)
		self.ok=Button(self.random_wndw,text="ok",command=self.random_wndw.destroy)
		self.ok.grid(row=2,column=0,sticky=E+W)
		return
		
	def event_class2(self,txt,clr,cons1,cons2):
		self.refresh()
		self.random_wndw=Toplevel()
		self.random_wndw.grab_set()
		self.random_wndw.configure(background=clr)
		self.event_label_2=Label(self.random_wndw,bg=clr,font=self.random_font,text=txt)
		self.event_label_2.grid(row=0,column=0)
		self.consequence_label1_2=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons1)
		self.consequence_label1_2.grid(row=1,column=0)
		self.consequence_label2_2=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons2)
		self.consequence_label2_2.grid(row=2,column=0)
		self.ok=Button(self.random_wndw,text="ok",command=self.random_wndw.destroy)
		self.ok.grid(row=3,column=0,sticky=E+W)
		return
		
	def event_class3(self,txt,clr,cons1,cons2,cons3):
		self.refresh()
		self.random_wndw=Toplevel()
		self.random_wndw.grab_set()
		self.random_wndw.configure(background=clr)
		self.event_label_3=Label(self.random_wndw,bg=clr,font=self.random_font,text=txt)
		self.event_label_3.grid(row=0,column=0)
		self.consequence_label1_3=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons1)
		self.consequence_label1_3.grid(row=1,column=0)
		self.consequence_label2_3=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons2)
		self.consequence_label2_3.grid(row=2,column=0)
		self.consequence_label3_3=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons3)
		self.consequence_label3_3.grid(row=3,column=0)
		self.ok=Button(self.random_wndw,text="ok",command=self.random_wndw.destroy)
		self.ok.grid(row=4,column=0,sticky=E+W)
		return
		
	def event_class4(self,txt,clr,cons1,cons2,cons3,cons4):
		self.refresh()
		self.random_wndw=Toplevel()
		self.random_wndw.grab_set()
		self.random_wndw.configure(background=clr)
		self.event_label_4=Label(self.random_wndw,bg=clr,font=self.random_font,text=txt)
		self.event_label_4.grid(row=0,column=0)
		self.consequence_label1_4=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons1)
		self.consequence_label1_4.grid(row=1,column=0)
		self.consequence_label2_4=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons2)
		self.consequence_label2_4.grid(row=2,column=0)
		self.consequence_label3_4=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons3)
		self.consequence_label3_4.grid(row=3,column=0)
		self.consequence_label4_4=Label(self.random_wndw,bg=clr,font=self.random_font,text=cons4)
		self.consequence_label4_4.grid(row=4,column=0)
		self.ok=Button(self.random_wndw,text="ok",command=self.random_wndw.destroy)
		self.ok.grid(row=5,column=0,sticky=E+W)
		return

lol=root()
mainloop()


