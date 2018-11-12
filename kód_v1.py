#coding: utf-8

#----------------------------------------------------------------------------------------------------------------
###### importy

from random import randint

#----------------------------------------------------------------------------------------------------------------
###### místo na proměnné, které se nemění zas tak často

tyden=103 #kolikátý týden se píše od hráčova nástupu do funkce ředitele
penize=1000 #kolik má škola na účtě
studenti_spokojenost=50
ucitele_spokojenost=50
rodice_spokojenost=50

#modifikátory plynoucí z vybavení školy - používají se při meziškolních soutěžích
veda_modifier=0
sport_modifier=0
vzdelanost_modifier=0

#proměnné, které jsou závislé na jiných faktorech
vydaje_na_ucitele= 15
#pocet_zaku=
najem=15
#castka=   #částka, kterou platí každý student na školném
skolne=2

#----------------------------------------------------------------------------------------------------------------

#třída hra

class game:
	#def __init__(self):

	def game_over_finance(self):
		print "konec hry, Škola zkrachovala"
	
	def game_over_puc(self):
		print "konec hry, byl jsi sesazen kombinovanou mocí svých poddaných"
	
	def game_over_gut(self):  ###nefunguje... proč? prej není definováno
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
			game_over_gut()
		if tyden%4==0:  #kontrola, zda škola nezkrachuje při placení nájmu nebo vyplácení platů na konci měsíce 
			if (penize+skolne)-(vydaje_na_ucitele+najem)<0:
				self.game_over_finance()
			elif studenti_spokojenost<15 and ucitele_spokojenost<15 or studenti_spokojenost<15 and rodice_spokojenost<15 or rodice_spokojenost<15 and ucitele_spokojenost<15: #kontrola spokojenosti na začátku každého měsíce
				self.game_over_puc()
			else:
				penize=penize-(vydaje_na_ucitele+najem)+skolne   #když škola nezkrachovala, tak se odečtou náklady
				print penize
				self.zeptejse()
		
				
	def zeptejse(self):
		print "vpred, vylepseni"
		lul=raw_input("vpred")
		if lul =="vpred":
			self.vpred()
		elif lul=="vylepseni":
			self.vylepseni()
		else:
			self.zeptejse()
	"""	
	"""
	
hra=game()			
hra.zeptejse()
	

