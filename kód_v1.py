#coding: utf-8

#----------------------------------------------------------------------------------------------------------------
###### importy

from random import randint

#----------------------------------------------------------------------------------------------------------------
###### místo na proměnné, které se nemění zas tak často

tyden=103   #kolikátý týden se píše od hráčova nástupu do funkce ředitele
kildny_tyden=0 #kolik týdnů se nekonala žádná soutěž
penize=1000 #kolik má škola na účtě
studenti_spokojenost=50 #
ucitele_spokojenost=50	# spokojenosti skupin 
rodice_spokojenost=50	#

#modifikátory plynoucí z vybavení školy - používají se při meziškolních soutěžích
veda_modifier=0
sport_modifier=0  
vzdelanost_modifier=0

#proměnné, které jsou závislé na jiných faktorech
vydaje_na_ucitele= 15
pocet_zaku=120
najem=15
castka=800   #částka, kterou platí každý student na školném
skolne=castka*pocet_zaku


#----------------------------------------------------------------------------------------------------------------

#třída hra
###########pokud budu realizovat random události, vyplatilo by se učitele, studenty a rodiče udělat jako třídy.


class game:
	#def __init__(self):

	def game_over_finance(self):
		print "konec hry, Škola zkrachovala"
	
	def game_over_puc(self):
		print "konec hry, byl jsi sesazen kombinovanou mocí svých poddaných"
	
	def game_over_gut(self):  ###nefunguje... proč? prej není definováno (ostatní konce hry fungujou normálně)
		print "konec hry, šťastně jsi dokázal vést svou školu po dobu pěti let! Gratulujeme"
	
	def vpred(self):
		global tyden  ### nešlo by to nějak dostat na jeden řádek?
		global penize  ###nacpat do konstruktoru x nemuselo by se to pak složitě vypisovat do volání třídy game?
		global skolne
		global vydaje_na_ucitele
		global najem
		tyden+=1
		print tyden
		if tyden%44==0: #kontrola, jestli neskončil školní rok
			tyden=tyden+8	#skok přes prázdniny
		if tyden==104: #kontrola, jestli hráči neskončilo funkční obodobí
			self.game_over_gut()
		if tyden%4==0:  #kontrola, zda škola nezkrachuje při placení nájmu nebo vyplácení platů na konci měsíce 
			if (penize+skolne)-(vydaje_na_ucitele+najem)<0:
				self.game_over_finance()
			elif studenti_spokojenost<15 and ucitele_spokojenost<15 or studenti_spokojenost<15 and rodice_spokojenost<15 or rodice_spokojenost<15 and ucitele_spokojenost<15: #kontrola spokojenosti na začátku každého měsíce
				self.game_over_puc()
			else:
				penize=penize-(vydaje_na_ucitele+najem)+skolne   #když škola nezkrachovala, tak se odečtou náklady
				print penize
				self.zeptej_se()
		if studenti_spokojenost<=25:	#varování kvůli nespokojenosti nějaké skupiny
			print "studenti jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat"
		if rodice_spokojenost<=25:
			self.zeptej_se()
			print "rodiče jsou vrcholně nespokojeni. Vyplatilo by se něco s tím udělat"
			self.zeptej_se()
		if ucitele_spokojenost<=25:
			print "ucitele jsou vrcholně nespokojeni. Vyplatilo by se s tím něco udělat"
			self.zeptej_se()
		######meziškolní soutěže (zvlášť funkce volaná odsud
		
				
	def zeptej_se(self):   #náhrada za grafické rozhraní, lze díky tomu vkládat vstup aspoň primitivně
		print "vpred / vylepseni / zmen_skolne"
		lul=raw_input "vpred"
		if lul =="vpred": #casovy skok o tyden
			self.vpred()
		#elif lul=="vylepseni":
			#self.vylepseni()
		elif lul=="zmen_skolne" #nechá ředitele změnit školné, což má vliv na spokojenost
			self.zmenit_skolne()
		else:
			print "error. zkus to znova"
			self.zeptej_se()
			
	
	def zmenit_skolne(self):
		global skolne  ##nešlo by to na jeden řádek?
		global castka
		global studenti_spokojenost
		global rodice_spokojenost
		self.x=0
		self.y=0
		print "současné školné na jednoho žáka je " + castka
		print "zadej novou hodnotu školného. Zadej 'zpet' pro krok zpět "
		self.ha=raw_input "kolik mají žáci platit?"
		if (ha==zpet): #možnost vrátit se "o okno zpátky"
			self.zeptej_se()
		elif self.ha<1200 and self.ha>400 and self.ha!=castka:  #jestli není školné moc vysoké, nebo nízké, nebo jestli se vůbec změnilo
			if self.ha<castka: 
				self.ha-castka=self.x
				self.x/50=self.y
				studenti_spokojenost=studenti_spokojenost+self.y*5    #úprava spokojeností v závislosti na školném
				rodice_spokojenost=rodice_spokojenost+self.y*5
				print "od příštího měsíce se školné sníží. Studenti a rodiče jsou rádi"
			else:
				self.ha-castka=self.x
				self.x/50=self.y			
				studenti_spokojenost=studenti_spokojenost-self.y*5	  #úprava spokojenosti v závislosti na školném
				rodice_spokojenost=rodice_spokojenost-self.y*5
				print "od příštího měsíce se školné zvýší. Studenti a rodiče nejsou rádi"
			castka=self.ha
			self.zeptej_se()
		elif:
			print "neplatná hodnota, zadej znovu. 'zpet' pro krok zpět"	#error
			self.zmenit_skolne()
		print skolne
		return skolne
		
	##možnost podnikání grantů?
	##
		
				
	

	
hra=game()			
hra.zeptejse()
	

