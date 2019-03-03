#coding: utf-8

#spočítat a vybalancovat začáteční pozici hráče

##grafika
#aby se widgety nehýbaly během hry
#dynamická velikost na hlavní obrazovce
#velikost okna,framů a přilepení k okrajům
#spawnovat uprostřed obrazovky(funkce geometry)
#dynamická velikost písma/jak to udělat, aby se widgety nerozlejzaly ven z obrazovky

#----------------------------------------------------------------------------------------------------------------
#importy
from random import randint
from sys import exit
from Tkinter import *
import tkFont
#import PIL.Image
from PIL import Image,ImageTk




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
		self.penize=1000000000000000000 #kolik má škola na účtě, integer aby se z toho nedělal float a na obrazovce nebylo x.0
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
		#self.main.configure(background="white")
		self.screen_width = self.main.winfo_screenwidth()
		self.screen_height = self.main.winfo_screenheight()
		
		#nápisy
		
		self.l_font=tkFont.Font(family="comic sans",size=16)
		self.buttonFont=tkFont.Font(family="comic sans",size=22,weight=tkFont.BOLD)		
		self.label_font=tkFont.Font(family="comic sans",size=16) #font na nápisy
		#self.int_font=tkFont.Font(family="comic sans",size=22,weight=tkFont.BOLD) #font na čísla u nápisů
		
		
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
		self.student_iint=Label(self.alt_frame,font=self.label_font,fg="red",text=self.castka)
		self.student_iint.grid(column=1,row=5,sticky=W)

		#spokojenosti
		
		self.sa_frame=Frame(self.main) #,pady=self.label_width-) #rámeček kvůli grafickému rozmístění
		self.sa_frame.grid(row=2,column=0)
		self.studenti_info=Label(self.sa_frame,text="spokojenost studentů: ")# + str(self.studenti_spokojenost)) #píše spokojenost žáků
		self.studenti_info.grid(column=0,row=0)
		self.ucitele_info=Label(self.sa_frame,text="spokojenost učitelů: ")# + str(self.ucitele_spokojenost)) #píše spokojenost učitelů
		self.ucitele_info.grid(column=0,row=1)
		self.rodice_info=Label(self.sa_frame,text="spokojenost rodičů: ")# + str(self.rodice_spokojenost)) #píše spokojenost rodičů
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
		
		self.button_frame=Frame(self.main) #,height=self.screen_height-self.sf_height) #rámeček kvůli grafickému rozmístění
		self.button_frame.grid(row=0,column=2)#,sticky=N+E+S+W)#,pady=20,padx=20)
		self.money_button=Button(self.button_frame,height=2,font=self.buttonFont, text="změnit školné",command=self.zmenit_skolne) #otevře okno na změnu školného
		self.money_button.grid(column=0,row=2,sticky=E+W)
		self.upgrade_button=Button(self.button_frame,height=2,font=self.buttonFont,text="vylepšení",command=self.upgrades) #otevře okno s vylepšeními školního vybavení
		self.upgrade_button.grid(column=0,row=3,sticky=E+W)
		self.plat_button=Button(self.button_frame,height=2,font=self.buttonFont,text="změnit platy",command=self.zmenit_platy) #otevře okno na změnu učitelských platů
		self.plat_button.grid(column=0,row=4,sticky=E+W)
		self.trophy_button=Button(self.button_frame,height=2,font=self.buttonFont,text="skříňka s trofejemi",command=self.trophies) #otevírá okno se školními poháry
		self.trophy_button.grid(column=0,row=5,sticky=E+W)
		
		#obrázek
		self.image=Image.open("reditelna.jpg")
		self.img=ImageTk.PhotoImage(self.image)
		self.img_label=Label(self.main,image=self.img)
		self.img_label.image=self.img
		self.img_label.grid(row=0,column=0,columnspan=2,rowspan=2)

		#vpřed  a opustit hru
		self.admin_frame=Frame(self.main)
		self.admin_frame.grid(row=2,column=2,sticky=S+W+E+N)
		
		#tlačítko vpřed
		self.forwardbuttonfont=tkFont.Font(family="comic sans",size=36,weight=tkFont.BOLD)
		self.forward_button=Button(self.admin_frame,font=self.forwardbuttonfont, text="vpřed",command=self.vpred) #posune čas o týden vpřed 
		self.forward_button.grid(column=0,row=0,sticky=E+W)#,sticky=N+E+W+S)
		
		#tlačítko opustit hru
		self.leavebuttonfont=tkFont.Font(family="comic sans",size=14,weight=tkFont.BOLD)
		self.exit_button=Button(self.admin_frame,font=self.leavebuttonfont, text="opustit hru", command=sys.exit) #ukončí hru
		self.exit_button.grid(column=0,row=1,sticky=E+W)#,sticky=E+W)
		
		self.main.update()
		self.screen_width = self.main.winfo_screenwidth()
		self.screen_height = self.main.winfo_screenheight()
		#self.label_width=self.label_frame.winfo_width()
		#self.sa_width=self.sa_frame.winfo_width()
		#self.bt_height=self.button_frame.winfo_height()
		#self.sa_height=self.sa_frame.winfo_height()
		#self.v_indent=self.screen_height-self.bt_height-self.sa_height-10
		#self.h_indent=self.screen_width-self.sa_width-self.label_width-10
		#self.sa_frame.grid(row=1,column=0,padx=(10,self.v_indent),pady=(self.h_indent,10))

		
#----------------------------------------------------------------------------------------------------------------
	def refresh(self): #funkce kontrolující obsah okna
self.week_int=Label(self.label_frame,font=self.label_font,fg="red",text=self.tyden)	
	def game_over_finance(self): #funkce na konec hry kvůli financím
		self.popupmsg("konec hry, Škola zkrachovala, zkus to znovu")
		return
		
	def game_over_odvolani(self): #funkce na konec hry kvůli znepřátelení osazenstva školy/rodičů
		self.popupmsg("konec hry, byl jsi sesazen kombinovanou mocí svých poddaných")
		return
		
	def game_over_gut(self): #funkce na "šťastný konec hry"
		self.popupmsg("konec hry, šťastně jsi dokázal vést svou školu po dobu dvou let! Gratulujeme")
		return
	
	def popupmsg(self,msg):  #custom msgbox
		self.popup=Toplevel()
		self.popup.grab_set() #aby uživatel nemohl do hlavního okna než vyřeší popup
		#self.popup.geometry("500x150+50+50")
		#self.popup.wm_title("pozor")
		self.label=Label(self.popup, text=msg)
		self.label.pack(side="top",fill="x", pady=10)
		self.b1=Button(self.popup,text="OK",command=self.end) #ok tlačítko, zavírá popup
		self.b1.pack()
		return
	
	def trophies(self):
		self.trp=Toplevel()
		self.trp.grab_set()
		self.tph_label=Label()
	
	def end(self): #funkce uzavírající jak popupmsg, tak hru. Volá se při konci hry
		self.popup.destroy()
		self.main.destroy()
		
	def upgrades(self): #okno, kde se dá vylepšovat školní vybavení
		self.upg=Toplevel()
		self.upg.grab_set()
		#self.upg.geometry("400x600")
		#self.upg.attributes("-fullscreen",True)
		
		##info
		self.sport_frame=Frame(self.upg)
		self.sport_frame.grid(row=0,column=0)#,sticky=N+S)
		self.sport_info=Label(self.sport_frame,text="úroveň sportovního vybavení: "+str(self.sport_level)) #info o levelu sportovního vybavení
		self.sport_info.grid(row=0,column=0,padx=10)
		self.sport_button=Button(self.sport_frame,text="vylepšit sportovní vybavení",command=self.sport_upgrade) #tlačítko na vylepšení sportovního vybavení
		self.sport_button.grid(row=0,column=1,padx=10)#,sticky=E+W)
	
		self.veda_frame=Frame(self.upg,width=200)
		self.veda_frame.grid(row=1,column=0,sticky=E+W)		
		self.veda_info=Label(self.veda_frame,text="úroveň vědeckého vybavení: "+str(self.veda_level)) #info o levelu vědeckého vybavení
		self.veda_info.grid(row=0,column=0,sticky=W)
		self.veda_button=Button(self.veda_frame,text="vylepšit vědecké vybavení",command=self.veda_upgrade) #tlačítko na vylepšení vědeckého vybavení 
		self.veda_button.grid(row=0,column=1,sticky=E)
				
		self.vedomosti_frame=Frame(self.upg)
		self.vedomosti_frame.grid(row=2,column=0,sticky=E+W)
		self.vedomosti_info=Label(self.vedomosti_frame,text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level)) #info o levelu učebního vybavení
		self.vedomosti_info.grid(row=0,column=0,sticky=W)
		self.vedomosti_button=Button(self.vedomosti_frame,text="vylepšit učební pomůcky",command=self.vedomosti_upgrade) #tlačítko na vylepšení učebních pomůcek
		self.vedomosti_button.grid(row=0,column=1,sticky=E)
		
		self.capacity_frame=Frame(self.upg)
		self.capacity_frame.grid(row=3,column=0,sticky=E+W)
		self.capacity_info=Label(self.capacity_frame,text="maximální kapacita žáků je: "+str(self.pocet_zaku)) #info o počtu žáků
		self.capacity_info.grid(row=0,column=0,sticky=W)
		self.capacity_button=Button(self.capacity_frame,text="zvýšit kapacitu školy",command=self.expand) #tlačítko na zvětšení školy
		self.capacity_button.grid(row=0,column=1,sticky=E)
		
		##zpět
		self.b1=Button(self.upg,text="zpět",command=self.upg.destroy) #tlačítko zavírající okno
		self.b1.grid(row=4,column=0,columnspan=2,sticky=E+W)
	
	def expand(self): #funkce zvyšující kapacitu budovy
		self.penize=self.penize-((self.zaci_lvl+1)*1050000) #počítání ceny na základě stávajícího počtu žáků
		self.money_int.config(text=self.penize)
		self.zaci_lvl+=1 
		self.ucitele_spokojenost-=5 #sníží spokojenost učitelů, protože nemají rádi na starost víc lidí
		self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
		self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		self.pocet_zaku+=40 #přidá kapacitu škole (+40 žáků)
		self.kapacita_info.config(text="maximální kapacita žáků je: "+str(self.pocet_zaku))
	
	def sport_upgrade(self): #funkce zvyšující úroveň sportovního vybavení
		self.penize=self.penize-((self.sport_level+1)*10000) #počítání ceny a odečítání peněz na základě stávajícího lvlu vybavení
		self.money_int.config(text=self.penize)
		self.sport_level+=1
		self.studenti_spokojenost+=10  #úpravy spokojeností
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=5
		self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
		self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
		self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
		self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
		self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
		self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		self.sport_info.config(text="úroveň sportovního vybavení: "+str(self.sport_level))
		return
	
	def veda_upgrade(self): #funkce zvyšující úroveň vědeckého vybavení
		self.penize=self.penize-((self.veda_level+1)*10000) #dynamciká cena odvíjející se od současného lvlu vybavení
		self.money_int.config(text=self.penize)
		self.veda_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=5
		self.ucitele_spokojenost+=10
		self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
		self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
		self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
		self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
		self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
		self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		self.veda_info.config(text="úroveň vědeckého vybavení: "+str(self.veda_level))
		return
		
	def vedomosti_upgrade(self): #funkce zvyšující úroveň učebních pomůcek
		self.penize=self.penize-((self.vedomosti_level+1)*10000)
		self.money_int.config(text=self.penize)
		self.vedomosti_level+=1
		self.studenti_spokojenost+=5
		self.rodice_spokojenost+=10
		self.ucitele_spokojenost+=5
		self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
		self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
		self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
		self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
		self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
		self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		self.vedomosti_info.config(text="úroveň vzdělanostního vybavení: "+str(self.vedomosti_level))
		return
		

	def zmenit_skolne(self): #definuje okno, které umožňuje měnit školné 
		self.skol=Toplevel()
		self.skol.grab_set() #
		#self.skol.geometry("500x150+50+50")
		self.infolabel=Label(self.skol,font=self.l_font, text="Stávající školné na žáka na měsíc je "+str(self.castka)+" kč")
		self.infolabel.grid(column=1,row=0,padx=10,pady=5)#,columnspan=2)
		self.low=Label(self.skol,font=self.l_font,foreground="red",text="moc nízká hodnota") #definice textu pro případ zadání neplatné hodnoty hráčem
		self.high=Label(self.skol,font=self.l_font,fg="red",text="moc vysoká hodnota")
		self.entry_width=self.infolabel.winfo_width()
		self.s_entry=Entry(self.skol,font=self.l_font)
		self.s_entry.grid(column=1,row=1,padx=10,pady=5,sticky=N+E+W+S)#,columnspan=2)
		self.s_entry.focus_set() #aby se hned po otevření okna dalo psát do Entry
		self.b1=Button(self.skol, text="Storno",font=self.l_font, command=self.skol.destroy) #tlačítka
		self.b1.grid(column=0,row=1,sticky=N+E+W+S,padx=10,pady=5)
		self.b2=Button(self.skol,text="Potvrdit",font=self.l_font, command=self.s_zmen)
		self.b2.grid(column=0,row=0,sticky=N+E+W+S,padx=10,pady=5)
		
	def s_zmen(self): #funkce měnící výši školného
		self.s_output=int(self.s_entry.get()) #vyčtení hodnoty z Entry 
		if (self.s_output>400)and(self.s_output<1500): #kontrola jestli je zadaná hodnota v povoleném rozmezí
			if self.s_output>self.castka:
				self.i=(self.s_output-self.castka)/100
				if self.i==0:
					self.i=1				
				self.rodice_spokojenost=self.rodice_spokojenost+self.i #anticheese
				self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
				self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)
			elif self.s_output<self.castka:
				self.i=(self.castka-self.s_output)/100
				if self.i==0:
					self.i=1
				self.rodice_spokojenost=self.rodice_spokojenost-self.i #anticheese
				self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
				self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)
			self.castka=self.s_output
			self.student_iint.config(text=self.castka)
			self.skol.destroy()
		elif (self.s_output<400): #když je zadaná hodnota moc nízká, napíše hlášku nadefinovanou v self.zmenit_skolne
			self.low.grid(column=1,row=2)
		elif (self.s_output>1500): #když je zadaná hodnota moc vysoká napíše hlášku nadefinovanou v self.zmenit_skolne
			self.high.grid(column=1,row=2)
			
			return
		
	def zmenit_platy(self): #definuje okno umožňující měnit platy učitelů 
		
		self.plat_wndw=Toplevel()
		self.plat_wndw.grab_set()
		#self.b_frame=Frame(self.plat_wndw)
		#self.b_frame.grid(column=0,row=0)
		self.pocet_label=Label(self.plat_wndw,font=self.l_font,text="počet učitelů: "+str(self.pocet_ucitelu))
		self.pocet_label.grid(column=0,row=0,padx=10,pady=10)#,sticky=NW)
		self.teacher_min_salary=Label(self.plat_wndw,font=self.l_font,text="minimální plat: "+str(self.min_salary))
		self.teacher_min_salary.grid(column=0,row=1,padx=10,pady=10)#,sticky=SW)
		self.plat_label=Label(self.plat_wndw,font=self.l_font,text="plat na jednoho učitele: "+str(self.plat))
		self.plat_label.grid(column=1,row=0,padx=10,pady=10)
		self.naklady_label=Label(self.plat_wndw,font=self.l_font,text="celkové náklady na učitele: "+str(self.vydaje_na_ucitele))
		self.naklady_label.grid(column=1,row=1,padx=10,pady=10)
		self.error_line=Label(self.plat_wndw,font=self.l_font,text="neplatná hodnota")
		self.p_entry=Entry(self.plat_wndw,font=self.l_font, width=40)
		self.p_entry.grid(column=0,row=2,columnspan=2,padx=10,pady=10,sticky=E+W)
		self.p_entry.focus_set()
		self.b1=Button(self.plat_wndw,text="Storno",command=self.plat_wndw.destroy) #tlačítko zavírající okno
		#self.b1.grid(column=0,row=0,sticky=N+E+W+S)
		self.b1.grid(column=0,row=3,padx=10,pady=10)#,sticky=E+W)
		self.b2=Button(self.plat_wndw,text="Potvrdit", command=self.p_zmen) #tlačítko volající funkci, která mění výši platů
		#self.b2.grid(column=1,row=0,sticky=N+E+W+S)
		self.b2.grid(column=1,row=3,padx=10,pady=10)#,sticky=E+W)
		
		"""
		self.w=self.plat_wndw.winfo_width() #šířka okna 
		self.h=self.plat_wndw.winfo_height()

		self.x=(self.screen_width-self.w)/2
		self.h=(self.screen_height-self.h)/2
		self.plat_wndw.geometry("%dx%d%"+self.x+self.y")
		"""
		
	def p_zmen(self): #funkce měnící plat 
		self.p_output=self.p_entry.get() #vyčtení hodnoty zadané hráčem
		if self.p_output!=0:
			if (self.p_output>self.min_salary): #kontrola, zda je zadaná hodnota nad minimálním platem
				if self.p_output>self.plat:
					self.i=(self.p_output-self.plat)/300
					if self.i==0:
						self.i=1
					self.ucitele_spokojenost=self.ucitele_spokojenost+self.i #algorytmus měnící spokojenost učitelů v závislosti na tom, jestli jim bylo přidáno, nebo ubráno
					self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
					self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
				elif self.p_output<self.plat:
					self.i=(self.plat-self.p_output)/300
					if self.i==0:
						self.i=1
					self.ucitele_spokojenost=self.ucitele_spokojenost-self.i
					self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
					self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
				self.plat=self.p_output
				self.teacher_sint.config(text=self.plat) 
				self.plat_wndw.destroy() #konec změny, zavření okna
				return
			else:
				self.error_line.grid() #když je neplatná hodnota, objeví se chybová hláška
	
	def vpred(self): #funkce posouvající čas o týden dopředu
		self.game_over=0
		self.tyden+=1
		self.week_info.config(text="týden: " + str (self.tyden)) #mění číslo týdne v ukazateli v hlavním okně
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
				self.money_info.config(text="finance: " + str (self.penize)+"kč")
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
		self.soutez_label=Label(self.soutez_okno,text="V týdnu se konal"+str(self.competition_type))
		self.soutez_label.pack()
		self.result_label=Label(self.soutez_okno,text="") #prázdný label, přidá se do něj, kolikátá skončila hráčova škola
		self.result_label.pack()
		self.prize_label=Label(self.soutez_okno,text="") #prázdný label na info o tom, kolik peběz škola vyhrála
		self.prize_label.pack()
		self.ok_b=Button(self.soutez_okno,text="ok",command=self.soutez_okno.destroy) #potvrzovací tlačítko
		self.ok_b.pack()
		self.playerschool=randint(0,100)+int(self.competition_modifier) #náhodné skóre pro školu hráče
		self.pos_values=[] #prázdný seznam na hodnoty NPC škol i hráčovy školy
		for i in range (0,100):	#aby NPC škola nemohla mít stejné skóre jako hráč
			self.pos_values.append(i) #vygenerovaná čísla se dají prázdného seznamu
		self.pos_values.remove(self.playerschool) #hodnota hráčovy školy se odebere ze seznamu, aby hráčova škola nemohla mít stejnou hodnotu jako NPC školy
		
		self.school1=self.pos_values[randint(0,len(self.pos_values)-1)] #pro každou školu se vygeneruje náhodné číslo 
		self.school2=self.pos_values[randint(0,len(self.pos_values)-1)]
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
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			if self.place==1:
				self.ucitele_spokojenost+=5
				self.rodice_spokojenost+=5
				self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
				self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
				self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
				self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
			
		
	def random_event(self,eve): #funkce simulující náhodné události
		self.event=eve
		if self.event<
		
		
		
		"""
		self.random_wndw=Toplevel()
		self.random_wndw.grab_set()
		
		if "self.consequence2" in locals():
			print self.consequence2
		if "self.consequence3" in locals():
			print self.consequence3
		if "self.consequence4" in locals():
			print self.consequence4
		
		self.event_type=randint(0,13) #náhodně se vybere, jaká událost se stane
		if self.event_type==0:
			self.event_text="Školní inspekce odhalila vady na vybavení školy. Musíš okamžitě vynaložit prostředky na opravu." #event text je proměnná použitá ve všech náhodných událostech, sloužící ke sdělení základní zprávy o tom, co se stalo
			self.consequence1="peníze - "+str(40000+self.zaci_lvl*8000)  #self.consequence se používá ve všech náhodných událostech ke sdělení hráčí, jaké měla událost následky
			self.consequence2="spokojenost rodičů - 10"
			self.consequence3="spokojenost učitelů - 10"
			self.consequence4="spokojenost žáků - 10"
			self.evil=0
			self.penize=self.penize-(40000+self.zaci_lvl*8000) #po self.consequence se provedou všechny věci v self.consequence popsané
			self.rodice_spokojenost-=10
			self.ucitele_spokojenost-=10
			self.studenti_spokojenost-=10
			self.money_info.config(text="finance: " + str (self.penize)+"kč") #tady se změní labely
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==1:
			self.evil=0
			self.event_text="Vypověděl službu jeden z kotlů na teplou vodu. Ve škole teče jen studená voda a je třeba urychleně investovat do nového kotle."
			self.consequence1="peníze - 100000"
			self.consequence2="spokojenost žáků - 10"
			self.consequence3="spokojenost učitelů - 10"
			self.penize-=100000
			self.studenti_spokojenost=self.studenti_spokojenost-10
			self.ucitele_spokojenost=self.ucitele_spokojenost-10
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==2:
			self.evil=0
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
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==3:
			self.evil=3
			self.event_text="Výpadek elektřiny, studenti i učitelé šli dřív domů"
			self.consequence1="spokojenost studentů + 5"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost rodičů - 5"
			self.studenti_spokojenost+=5
			self.ucitele_spokojenost+=5
			self.rodice_spokojenost-=5
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==4:
			self.evil=1
			self.event_text="Navýšení minimální mzdy: Minimální mzda je odteď "+str(self.min_salary+800)
			self.consequence1="spokojenost učitelů + 10"
			self.ucitele_spokojenost+=10
			self.min_salary+=800
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==5:
			self.evil=0
			self.event_text="Stala se nehoda v chemické laboratoři, bude nepoužitelná, dokud se neopraví"
			self.consequence1="level vědeckého vybavení - 1"
			self.consequence2="spokojenost učitelů - 5"
			self.consequence3="spokojenost žáků - 5"
			self.consequence4="spokojenost rodičů - 5"
			self.veda_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==6:
			self.evil=0
			self.event_text="Při kontrole se zjistilo, že školní učebnice jsou zastaralé a velké množství se jich muselo vyhodit"
			self.consequence1="level učebního vybavení - 1"
			self.consequence2="spokojenost učitelů - 5"
			self.consequence3="spokojenost žáků - 5"
			self.consequence4="spokojenost rodičů - 5"
			self.vedomosti_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==7:
			self.evil=0
			self.event_text="Při velké bouřce se zničilo školní multifunkční hřiště"
			self.consequence1="level sportovního vybavení - 1"
			self.consequence2="spokojenost učitelů - 5"
			self.consequence3="spokojenost žáků - 5"
			self.consequence4="spokojenost rodičů - 5"
			self.vedomosti_level-=1
			self.ucitele_spokojenost-=5
			self.studenti_spokojenost-=5
			self.rodice_spokojenost-=5
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==8:
			self.evil=1
			self.event_text="škola obrdžela grant na sportovní vybavení"
			self.consequence1="level sportovního vybavení + 1"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost žáků + 5"
			self.consequence4="spokojenost rodičů + 5"
			self.sport_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==9:
			self.evil=1
			self.event_text="škola obrdžela grant na vědecké vybavení"
			self.consequence1="level vědeckého vybavení + 1"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost žáků + 5"
			self.consequence4="spokojenost rodičů + 5"
			self.veda_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==10:
			self.evil=1
			self.event_text="škola obrdžela grant na učební vybavení"
			self.consequence1="level vědeckého vybavení + 1"
			self.consequence2="spokojenost učitelů + 5"
			self.consequence3="spokojenost žáků + 5"
			self.consequence4="spokojenost rodičů + 5"
			self.veda_level+=1
			self.ucitele_spokojenost+=5
			self.studenti_spokojenost+=5
			self.rodice_spokojenost+=5
			self.studenti_canvas.coords(self.stangle,0,0,self.studenti_spokojenost*2,17)
			self.studenti_canvas.itemconfigure(self.stext,text=self.studenti_spokojenost)  #úpravy ukazatelů na hlavní obrazovce
			self.rodice_canvas.coords(self.rtangle,0,0,self.rodice_spokojenost*2,17)
			self.rodice_canvas.itemconfigure(self.rtext,text=self.rodice_spokojenost)
			self.ucitele_canvas.coords(self.utangle,0,0,self.ucitele_spokojenost*2,17)
			self.ucitele_canvas.itemconfigure(self.utext,text=self.ucitele_spokojenost)
		elif self.event_type==11:
			self.evil=1
			self.h=randint(1,30)*1000
			self.event_text="škola obdržela mimořádnou dotaci"
			self.consequence1="peníze + "+str(self.h) 
			self.penize=self.penize+self.h
			self.money_info.config(text="finance: " + str (self.penize)+"kč")
		elif self.event_type==12:
			self.evil=0
			self.k=randint(5,25)*1000
			self.event_text="škole byl zvýšen nájem o "+str(self.k)+" měsíčně"
			self.consequence1="měsíční nájem + "+str(self.k)
			self.najem=self.najem+self.k
			self.building_expenses.config(text="měsíční nájem: "+ str(self.najem)+"kč")
		elif self.event_type==13:
			self.evil=1
			self.k=randint(5,30)*1000
			self.event_text="škole byl snížen nájem o "+str(self.k)+" měsíčně"
			self.consequence1="měsíční nájem - "+str(self.k)
			self.najem=self.najem-self.k
			self.building_expenses.config(text="měsíční nájem: "+ str(self.najem)+"kč")
		if self.evil==0:
			self.random_wndw.configure(bg="red")
			self.back="red"
		elif self.evil==1:
			self.random_wndw.configure(bg="green")
			self.back="green"
		self.gen_label=Label(self.random_wndw,bg=self.back,text=self.event_text)
		self.gen_label.grid(row=1,column=0)
		self.consequence_label=Label(self.random_wndw,bg=self.back,text=self.consequence1) #aspoň jeden následek je vždycky
		self.consequence_label.grid(row=2,column=0)
		if "self.consequence2" in locals(): #když byla dříve nadefinovaná proměnná na následky, vytvoří se o tom label
			self.consequence2_label=Label(self.random_wndw,bg=self.back,text=self.consequence2)
			self.consequence2_label.grid(row=3,column=0)
		if "self.consequence3" in locals():
			self.consequence3_label=Label(self.random_wndw,bg=self.back,text=self.consequence3)
			self.consequence3_label.grid(row=4,column=0)
		if "self.consequence4" in locals():
			self.consequence4_label=Label(self.random_wndw,bg=self.back,text=self.consequence4)
			self.consequence4_label.grid(row=5,column=0)
		self.ok=Button(self.random_wndw,text="ok",command=self.random_wndw.destroy)
		self.ok.grid(row=6,column=0,sticky=E+W)
		"""
lol=main()
mainloop()


