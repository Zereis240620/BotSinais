import sqlite3
from datetime import datetime
import logging
from time import gmtime, strftime
import mysql.connector
import time
import operator
import sys
import json
from threading import Thread
import requests
# import MySQLdb


def createDatabase():
	conn = sqlite3.connect('dbConfig.db')
	cursor = conn.cursor()
	cursor.execute("""
	CREATE TABLE sinais (
	        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	        horario     Time NOT NULL,
	        paridade    TEXT NOT NULL,
	        acao        Text NOT NULL,
	        exec        Text NOT NULL,
	        timeframe   Text NOT NULL,
	        data_insert DateTime NOT NULL);""")

	print('Tabela criada com sucesso Sinais')

	# criando a tabela (schema)
	cursor.execute("""
	CREATE TABLE operators (
	        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	        paridade TEXT NOT NULL,
	        valor    REAL,
	        result   VARCHAR(11) NOT NULL,        
	        criado_em DATE NOT NULL
	);
	""")

	print('Tabela criada com sucesso Operações')

	conn.close()


def insert(horario,paridade,acao,timeframe,exec):
	conn = sqlite3.connect('dbConfig.db')
	cursor = conn.cursor()

	sqlString = 'Insert into sinais(horario,paridade,acao,exec,timeframe,data_insert) values(?,?,?,?,?,?)'

	now = datetime.now()
	# date_insert = f'{now.year}-{now.month}-{now.day}';
	date_insert = datetime.now()

	params = [horario,paridade,acao,exec,timeframe,date_insert]

	cursor.execute(sqlString,params)

	conn.commit()
	conn.close()

	return 'Registro Inserido'

def selectAll():
	conn = sqlite3.connect('dbConfig.db')
	cursor = conn.cursor()
	
	sqlString = "Select * From sinais"

	cursor.execute(sqlString)

	rows = cursor.fetchall()

	# result = str(json.dumps(rows[0]))
	# result = result.replace('[','').replace(']','')

	conn.close()
	# print(rows)
	return rows

def selectSinal(horario):
	conn = sqlite3.connect('dbConfig.db')
	cursor = conn.cursor()
	
	sqlString = "Select * From sinais where horario = ? and exec = 'N'"

	params = [horario]
	cursor.execute(sqlString,params)

	rows = cursor.fetchall()

	# result = str(json.dumps(rows[0]))
	# result = result.replace('[','').replace(']','')

	conn.close()	
	
	return rows


def updateSinal(id):
	conn = sqlite3.connect('dbConfig.db')
	cursor = conn.cursor()
	
	sqlString = "Update sinais set exec = ? where id = ?"

	params = ['S',int(id)]
	cursor.execute(sqlString,params)

	# rows = cursor.fetchall()

	# result = str(json.dumps(rows[0]))
	# result = result.replace('[','').replace(']','')	
	conn.commit()
	print('Atualizado')
	conn.close()
	# print(rows)
	return 'OK'


def deleteAll():
	# conectando...
	conn = sqlite3.connect('dbConfig.db')	
	cursor = conn.cursor()

	cursor.execute("""DELETE FROM sinais;""")
	cursor.execute("""DELETE FROM sqlite_sequence where name='sinais';""")
	

	conn.commit()
	conn.close()

	return 'Sucess'


def deleteAllOperators():
	conn = sqlite3.connect('dbConfig.db')	
	cursor = conn.cursor()

	cursor.execute("""DELETE FROM sinais;""")
	cursor.execute("""DELETE FROM operators;""")

	conn.commit()
	conn.close()

	return 'OK'

def connectDatabase():
	arq = open('configDB.txt','r')
	arquivo = arq.read()
	data = json.loads(arquivo)
	mydb = mysql.connector.connect(
	  host=data['host'],
	  user=data['user'],
	  password=data['passwd'],
  	  database=data['db']
	)
	# mydb = MySQLdb.connect(host=data['host'], user=data['user'], passwd=data['passwd'], db=data['db'])

	return mydb

def selectSinais():
	conn = connectDatabase()
	cursor = conn.cursor()
	data = datetime.now()
	data = data.strftime("%Y-%m-%d")
	# data = time.strftime('%Y-%m-%d')	
	query = "SELECT * FROM sinais where data_sinal = %s"
	param = [data]
	
	cursor.execute(query,param)

	rows = cursor.fetchall()

	return rows	


# createDatabase()
# x = selectAll()
# for y in x:
# 	print(y[1])