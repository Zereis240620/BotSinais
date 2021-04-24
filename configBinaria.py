from iqoptionapi.stable_api import IQ_Option
import logging
import time
import datetime as dt
from time import gmtime, strftime
import operator
import sys
import json
from threading import Thread
import requests
import sqlite3
from datetime import datetime
import DbHelper

# ajustar stop igual o do MHi

def StopProcess(Lb1):
	config['status'] = False
	balanceDefined['exec'] = 'N'
	# Lb1.insert("end",f"Disconnect Magic")
	# # Lb1.itemconfig("end", {'bg':'green'},fg='white')
	# Lb1.yview("end")
	print('Stop')

balance = {'value': 0}
def getBalance(Iq):
	balance['value'] = Iq.get_balance()
	return float(balance['value'])


def defineBalance(par,Iq):
	balanceInicial['valor'] = getBalance(Iq)
	return 'OK'	

StopGain = {'value': 0}
StopLoss = {'value': 0}
config = {'status':True}
balanceInicial = {'valor': 0}
balanceDefined = {'exec': 'N'}
balanceAtual = {'valor': 0}

def MaoFixa(codigo,Iq,Paridade,typeAccount,valorEntrada,Direcao,stopWin,stopLoss,timeFrame,Lb1,Gains,Perdas):
	if config['status'] == True:
		Iq.change_balance(typeAccount)
		
		DbHelper.updateSinal(codigo)
		status, id = Iq.buy(valorEntrada, Paridade, Direcao, timeFrame)
		StopW = float(stopWin)
		StopL = float(stopLoss)

		if balanceDefined['exec'] == 'N':
			balanceDefined['exec'] = 'S'
			balanceInicial['valor'] = getBalance(Iq)

		time = strftime("%H:%M:%S", gmtime())

		Lb1.Append("end",f"{time} - {Paridade} - {'Compra' if Direcao == 'call' else 'Venda'} - M{timeFrame}")
		# Lb1.itemconfig("end", {'bg':'green'},fg='white')
		# Lb1.yview("end")
		#Arrumar Stop

		if status:
			print('Aguardando Resultado Da Entrada...')
			while True:
				status, lucro = Iq.check_win_v3(id)
				if status:
					if lucro > 0 :
						InsertOperators(Paridade,lucro,'WIN')
						# StopGain['value'] = selectOperators(Paridade,'WIN')
						balanceAtual['value'] = getBalance(Iq)
						StopGain['value'] = balanceInicial['valor'] - balanceAtual['value']

						print('Win: ',round(lucro,2))
						print(float(StopGain['value']),StopW)
						
						Lb1.Append(f"Win: {round(lucro,2)}")
						Gains.SetValue(selectOperators(Paridade,'WIN'))

						if float(abs(StopGain['value'])) >= StopW:
							config['status'] = False
							
							Lb1.Append(f"Bateu o limite de ganhos diarios: {float(StopGain['value'])}")
							# Lb1.itemconfig("end", {'bg':'green'},fg='white')
							# Lb1.yview("end")

							print('Bateu o limite de ganhos diarios', float(StopGain['value']))
						
						return lucro

					else:
						InsertOperators(Paridade,valorEntrada,'LOSS')
						# StopLoss['value'] = selectOperators(Paridade,'LOSS')

						balanceAtual['value'] = getBalance(Iq)
						StopLoss['value'] = balanceInicial['valor'] - balanceAtual['value']

						print('Loss: ',round(lucro,2))
						print(float(StopLoss['value']),StopL)

						Lb1.Append(f"Loss: {round(lucro,2)}")
						Perdas.SetValue(selectOperators(Paridade,'LOSS'))

						if float(StopLoss['value']) >= StopL:

							config['status'] = False

							Lb1.Append("end",f"Bateu o limite de perda diaria: {float(StopLoss['value'])}")
							# Lb1.itemconfig("end", {'bg':'red'},fg='white')
							# Lb1.yview("end")

							print('Bateu o limite de perda diaria',float(StopLoss['value']))
								
						return lucro

					break




def Gale(codigo,Iq,par,valor_entrada,dir,time, stop_gain, stop_loss,Lb1,Gains,Perdas):
	if config['status'] == True:	

		DbHelper.updateSinal(codigo)
		status, id = Iq.buy(valor_entrada, par, dir, time)

		if balanceDefined['exec'] == 'N':
			balanceDefined['exec'] = 'S'
			balanceInicial['valor'] = getBalance(Iq)

		timeHr = strftime("%H:%M:%S", gmtime())

		Lb1.Append(f"{timeHr} - {par} - {'Compra' if dir == 'call' else 'Venda'} - M{time}")
		# Lb1.itemconfig("end", {'bg':'green'},fg='white')
		# Lb1.yview("end")

		if status:
			while config['status']:
				status,valor = Iq.check_win_v3(id)
				if status:
					print('Resultado operação: ', end='')
					# Lb1.insert("end",'Resultado operação')
					# Lb1.yview("end")
					# print('WIN /' if valor > 0 else 'LOSS /' , round(valor, 2))
					if valor > 0:
						InsertOperators(par,valor,'WIN')
						CountGale = 0
						# StopGain['value'] = selectOperators(par,'WIN')
						balanceAtual['value'] = getBalance(Iq)
						StopGain['value'] = balanceInicial['valor'] - balanceAtual['value']

						Lb1.Append(f"Win: {round(valor,2)}")

						Gains.SetValue(selectOperators(par,'WIN'))

						if float(abs(StopGain['value'])) >= stop_gain:
							config['status'] = False
							
							Lb1.Append(f"Você Bateu o Limite de Ganhos Diários: {float(StopGain['value'])}")

							print('Você Bateu o Limite de Ganhos Diários',float(StopGain['value']))

						return valor

					else:
						InsertOperators(par,valor_entrada,'LOSS')
						# StopLoss['value'] = selectOperators(par,'LOSS')
						balanceAtual['value'] = getBalance(Iq)
						StopLoss['value'] = balanceInicial['valor'] - balanceAtual['value']
						
						Lb1.Append(f"Loss: {round(valor,2)}")

						Perdas.SetValue(selectOperators(par,'LOSS'))

						if float(StopLoss['value']) >= stop_loss:
							config['status'] = False

							Lb1.Append(f"Você Atingiu Limite de Perdas Diárias: {float(StopLoss['value'])}")

							print('Você Atingiu Limite de Perdas Diárias',float(StopLoss['value']))
							
						return valor

					break


def entradasGale(id,Iq,Paridade,typeAccount,valorEntrada,Direcao,stopWin,stopLoss,timeFrame,valor1,valor2,valor3,valor4,Lb1,Gains,Perdas):
	if config['status'] == True:	
		Iq.change_balance(typeAccount)
		
		
		result = Gale(id,Iq,Paridade,valorEntrada,Direcao,timeFrame,float(stopWin), float(stopLoss),Lb1,Gains,Perdas)

		try:			
			if result > 0:
				# break
				return 'win'
				print('Win')

				Lb1.Append(f"Win")
				# Lb1.itemconfig("end", {'bg':'green'},fg='white')
				# Lb1.yview("end")	


			else:

				result = Gale(id,Iq,Paridade,valor1,Direcao,timeFrame,float(stopWin), float(stopLoss),Lb1,Gains,Perdas)
				Lb1.Append(f"Gale 1")
				# Lb1.itemconfig("end", {'bg':'red'},fg='white')
				# Lb1.yview("end")

				if result > 0:
					return 'win'
					print('Win')

					Lb1.Append(f"Win")
					# Lb1.itemconfig("end", {'bg':'green'},fg='white')
					# Lb1.yview("end")

				else:
					result = Gale(id,Iq,Paridade,valor2,Direcao,timeFrame,float(stopWin), float(stopLoss),Lb1,Gains,Perdas)
					
					Lb1.Append(f"Gale 2")
					# Lb1.itemconfig("end", {'bg':'red'},fg='white')
					# Lb1.yview("end")

					if result > 0:
						# break
						return 'win'
						print('Win')
						
						Lb1.Append(f"Win")
						# Lb1.itemconfig("end", {'bg':'green'},fg='white')
						# Lb1.yview("end")

					else:
						

						result = Gale(id,Iq,Paridade,valor3,Direcao,timeFrame,float(stopWin), float(stopLoss),Lb1,Gains,Perdas)

						Lb1.Append(f"Gale 3")
						# Lb1.itemconfig("end", {'bg':'red'},fg='white')
						# Lb1.yview("end")

						if result > 0:
							# break
							Lb1.Append(f"Win")
							# Lb1.itemconfig("end", {'bg':'green'},fg='white')
							# Lb1.yview("end")

							return 'win'
							print('Win')
						else:
							

							result = Gale(id,Iq,Paridade,valor4,Direcao,timeFrame,float(stopWin), float(stopLoss),Lb1,Gains,Perdas)

							Lb1.Append(f"Gale 4")
							# Lb1.itemconfig("end", {'bg':'red'},fg='white')
							# Lb1.yview("end")


							if result > 0:
								
								Lb1.Append(f"Win")
								# Lb1.itemconfig("end", {'bg':'green'},fg='white')
								# Lb1.yview("end")

								print('Win')

								return 'win'

							else:

								Lb1.Append(f"Loss")
								# Lb1.itemconfig("end", {'bg':'red'},fg='white')
								# Lb1.yview("end")

								print('Loss')
								return 'loss'

		except:
			print('')



Soros = []
valorEntrada = {'valor': 0, 'statusCreate': True}

def entradasSoro(codigo,Iq,Paridade,typeAccount,valorentrada,Direcao,stopWin,stopLoss,timeFrame,soro,Lb1,Gains,Perdas):

	if config['status'] == True:
		Iq.change_balance(typeAccount)
		print('Entrou')
		DbHelper.updateSinal(codigo)
		
		if(valorEntrada['statusCreate']):
			valorEntrada['valor'] = valorentrada
			valorEntrada['statusCreate'] =  False

		StopW = float(stopWin)
		StopL = float(stopLoss)
		ValueSoros = soro
		valorEntradaOrig = valorentrada

		status, id = Iq.buy(int(valorEntrada['valor']), Paridade, Direcao, timeFrame)
		
		if balanceDefined['exec'] == 'N':
			balanceDefined['exec'] = 'S'
			balanceInicial['valor'] = getBalance(Iq)

		timeHr = strftime("%H:%M:%S", gmtime())		

		Lb1.Append(f"{timeHr} - {Paridade} - {'Compra' if Direcao == 'call' else 'Venda'} - M{timeFrame}")
		# Lb1.itemconfig("end", {'bg':'green'},fg='white')
		# Lb1.yview("end")

		if status:
			print('Aguardando resultado....')
			while config['status']:
				status,valor = Iq.check_win_v3(id)
				
				if status:
					# print('Resultado operação: ', end='')
					# Lb1.insert("end",'Resultado operação')
					# Lb1.yview("end")
					print('WIN /' if valor > 0 else 'LOSS /' , round(valor, 2))
					if valor > 0:
						InsertOperators(Paridade,valor,'WIN')

						if len(Soros) >= int(ValueSoros):
							valorEntrada['valor'] = valorEntradaOrig
							Soros.clear()

						else:
							Soros.append(1)
							valorEntrada['valor'] = float(valorEntrada['valor'])+float(round(valor,2))


						balanceAtual['value'] = getBalance(Iq)
						StopGain['value'] = balanceInicial['valor'] - balanceAtual['value']
						
						Lb1.Append(f"Win: {round(valor,2)}")
						
						Gains.SetValue(selectOperators(Paridade,'WIN'))

						if float(abs(StopGain['value'])) >= StopW:
							config['status'] = False

							Lb1.Append(f"Você Bateu o Limite de Ganhos Diários: {float(StopGain['value'])}")

							print('Você Bateu o Limite de Ganhos Diários',float(StopGain['value']))

						return 'x'						

					else:
						InsertOperators(Paridade,valorEntrada['valor'],'LOSS')
						valorEntrada['valor'] = valorEntradaOrig
						# StopLoss['value'] = selectOperators(Paridade,'LOSS')
						balanceAtual['value'] = getBalance(Iq)
						StopLoss['value'] = balanceInicial['valor'] - balanceAtual['value']

						Lb1.Append(f"Loss: {round(valor,2)}")

						Perdas.SetValue(selectOperators(Paridade,'LOSS'))

						if float(StopLoss['value']) >= StopL:
							config['status'] = False

							Lb1.Append(f"Você Atingiu Limite de Perdas Diárias: {float(StopLoss['value'])}")
							print('Você Atingiu Limite de Perdas Diárias',float(StopLoss['value']))							

						return 'x'
					break

def InsertOperators(paridade,valor,result):
	# conectando...
	conn = sqlite3.connect('dbConfig.db')
	cursor = conn.cursor()	
	
	now = datetime.now()
	date_create = f'{now.year}-{now.month}-{now.day}';

	query = """
	INSERT INTO operators(paridade,valor,result,criado_em)
	VALUES (?,?,?,?) """
	
	params =  [paridade, valor, result, date_create]

	cursor.execute(query, params)
	conn.commit()
	conn.close()
	return 'Sucess'


def selectOperators(paridade,result):
	# conectando...
	conn = sqlite3.connect('dbConfig.db')	
	cursor = conn.cursor()	

	query = """SELECT sum(t1.valor) as soma FROM operators t1 WHERE t1.result = ? ;"""
	params = [result]
	
	cursor.execute(query,params)

	rows = cursor.fetchall()
	
	result = str(json.dumps(rows[0]))
	result = result.replace('[','').replace(']','')

	conn.close()

	return result					