# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:05:46 2020

@author: Giulio
"""

import random as rd
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy import optimize
import string


def Guess_The_Word(Direction = "Fremd->T",filename = 'Test.xls', filepath = '',N = 20):
	
	RA = 0
	WA = 0
	
	words = pd.read_excel(filepath+filename)
	Dword = list(words['Fremd'])
	Tword = list(words['Translation'])

	
	
	if Direction == "Fremd->T":
		
		for i in range(N):
			
			unknown = rd.choice(Dword)
			guess   = input("Insert the translation for " + unknown+"\n")
			
			
			
			
			if guess.lower() == Tword[Dword.index(unknown)].lower():
				RA += 1
				Tword.remove(Tword[Dword.index(unknown)])
				Dword.remove(unknown)
				print ("Right!")
				
				
			elif guess.lower() != Tword[Dword.index(unknown)].lower():
				
				Twordplus = [Tword[Dword.index(unknown)].split(' / ')[i].lower() for i in range(len(Tword[Dword.index(unknown)].split(' / ')))]
				
				if guess.lower() in Twordplus:
					RA +=1
					print("Right!\nThe complete solution is given by: ",Tword[Dword.index(unknown)].lower())
					Tword.remove(Tword[Dword.index(unknown)])
					Dword.remove(unknown)
					
				elif (guess.lower()) not in Twordplus:
					Twordplus1 = [Tword[Dword.index(unknown)].split(' ')[i].lower() for i in range(len(Tword[Dword.index(unknown)].split(' ')))]
					print(Twordplus1)
					if guess.lower() in Twordplus1:
						RA +=1
						print("Right!\nThe complete solution is given by: ",Tword[Dword.index(unknown)].lower())
						Tword.remove(Tword[Dword.index(unknown)])
						Dword.remove(unknown)
						
					
					else:
						WA += 1
						print("Wrong!\nThe right translation was",Tword[Dword.index(unknown)])
						continue

					
			
			
	



	if Direction != "Fremd->T" and Direction == "T->Fremd":
		
		for i in range(N):
		
			unknown = rd.choice(Tword)
			guess   = input("Insert the translation for " + unknown+"\n")
			
			
			
			
			if guess.lower() == Dword[Tword.index(unknown)].lower():
				RA += 1
				Dword.remove(Dword[Tword.index(unknown)])
				Tword.remove(unknown)
				print ("Right!")
		
		
			elif guess.lower() != Dword[Tword.index(unknown)].lower():
				
				Dwordplus = [Dword[Tword.index(unknown)].split(' ')[i].lower() for i in range(len(Dword[Tword.index(unknown)].split(' ')))]
				
				if guess.lower() in Dwordplus:
					print('h')
					RA +=1
					print("Right!\nThe complete solution is given by: ",Dword[Tword.index(unknown)].lower())
					Dword.remove(Dword[Tword.index(unknown)])
					Tword.remove(unknown)

				else:
					print('t')
					WA += 1
					print("Wrong!\nThe right translation was",Dword[Tword.index(unknown)])
					continue
		
		
		print('You guessed the '+ str(RA/N) + "% of the words of " + filename + "!")
	



	



