# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from PIL import Image
from iqoptionapi.stable_api import IQ_Option
import logging
from threading import Thread
import time
import tkinter
from datetime import datetime
import operator
import sys
import os
import requests
import json
import DbHelper
import datetime
from PIL import ImageTk, Image
# import MySQLdb
import mysql.connector
import configDigital
import configBinaria

###########################################################################
## Class Login
###########################################################################
Valor = []
Soros = []
# Faltando ajustar logs para o list
#Convert image
def scale_bitmap(bitmap, width, height):
	imgLblLogo = Image.open("img/iconBot.png")
	imgLblLogo = imgLblLogo.resize((width,height), Image.ANTIALIAS)
	imgLblLogo.save('iconBot.bmp')
	# result = imgLblLogo.tobitmap()
	return result

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,308 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.SetIcon(wx.Icon('img/faviiconBot.ico', wx.BITMAP_TYPE_ICO))
		
		# bitmap = wx.Bitmap(u"img/iconBot.png")
		# bitmap = "img/iconBot.png"
		# bitmap = scale_bitmap(bitmap, 130, 130)		
		bitmap = wx.Bitmap("img/LogoLogin.bmp")

		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY,bitmap, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer1.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lblLogin = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLogin.Wrap( -1 )

		self.lblLogin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.lblLogin.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer1.Add( self.lblLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.txtLogin = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer1.Add( self.txtLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lblSenha = wx.StaticText( self, wx.ID_ANY, u"Senha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblSenha.Wrap( -1 )

		self.lblSenha.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.lblSenha.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		bSizer1.Add( self.lblSenha, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.txtSenha = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_PASSWORD )
		bSizer1.Add( self.txtSenha, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.BtLogin = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )

		self.BtLogin.SetBitmap( wx.Bitmap( u"img/4_botao_entrar.png", wx.BITMAP_TYPE_ANY ) )
		self.BtLogin.SetBitmapPressed( wx.Bitmap( u"img/4_botao_entrarBefore.png", wx.BITMAP_TYPE_ANY ) )
		self.BtLogin.SetBitmapFocus( wx.Bitmap( u"img/4_botao_entrar.png", wx.BITMAP_TYPE_ANY ) )
		self.BtLogin.SetBitmapCurrent( wx.Bitmap( u"img/4_botao_entrar.png", wx.BITMAP_TYPE_ANY ) )
		bSizer1.Add( self.BtLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
		# Connect Events
		self.BtLogin.Bind( wx.EVT_BUTTON, self.loginUser )
	# Virtual event handlers, overide them in your derived class	
	def loginUser( self, event ):
		self.login = self.txtLogin.GetValue()
		self.senha = self.txtSenha.GetValue()
		self.retorno = self.LogarUser(self.login,self.senha)

		if self.retorno == 'ativo':
			self.Hide()
			loadSinais()
			home = Home(self,self.login,self.senha,self.Iq)
			home.Show()
		else:
		   print('Não Logou')
		   msgDialog = MsgDialog(self)
		   msgDialog.Show()
		   		   	
		event.Skip()

	def LogarUser(self,login,senha):
		# print(login, senha)
		self.login = login
		self.senha = senha
		self.retorno = self.Login(self.login,self.senha)
		print('Você está ', self.retorno)
		return self.retorno	
	
	def LoginVerify(self):
		verifyLogin = self.verificaArqVazio(self,'login.txt')
	
		if verifyLogin == False:
			window.deiconify()

		else:
			print('Aguarde Estamos validando seus dados....')
			arq = open('login.txt','r')
			arquivo = arq.read() 	
			data = json.loads(arquivo)		
			LoginUser(data['email'], data['senha'])

		return 'OK'
	
	def Login(self,email,senha):
		self.emailUser = email
		self.senhaUser = senha
		print('senha e email',email,senha)
		logging.disable(level=(logging.DEBUG))
		self.Iq = IQ_Option(email,senha)
		self.check, self.reason = self.Iq.connect()
		self.url = 'http://meubot.me/rest.php'
		self.varResult = 0
		self.resultRequest = requests.post(self.url, data={"class": "SystemUserRestService","method": "getUser","email": self.emailUser, "active": "Y" })
		self.dataRequest = json.loads(self.resultRequest.text)
		print(self.dataRequest)
		self.idUsuario = self.dataRequest['data']['id']

		if self.check == True:
			if self.dataRequest['data']['msg'] == 'ATIVO':
				print('Logou')
				self.varResult = 'ativo'
			else:
				self.varResult = 'desativo'

		time.sleep(0.1)
		return self.varResult	

	def verificaArqVazio(arq):  
	    return os.path.isfile(arq) and os.path.getsize(arq) > 0				



	def __del__( self ):
		pass


###########################################################################
## Class Home
###########################################################################

class Home ( wx.Frame ):

	def __init__( self, parent ,email,senha,Iq ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.email = email
		self.senha = senha
		self.Iq = Iq

		self.SetSizeHints( wx.Size( 596,500 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.SetIcon(wx.Icon('img/faviiconBot.ico', wx.BITMAP_TYPE_ICO))

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		gSizer2 = wx.GridSizer( 0, 4, 0, 0 )

		self.lblTypeAccount = wx.StaticText( self, wx.ID_ANY, u"Tipo de Conta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTypeAccount.Wrap( -1 )

		self.lblTypeAccount.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer2.Add( self.lblTypeAccount, 0, wx.ALL|wx.EXPAND, 5 )

		self.lblVrEntrada = wx.StaticText( self, wx.ID_ANY, u"Valor da Entrada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblVrEntrada.Wrap( -1 )

		self.lblVrEntrada.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer2.Add( self.lblVrEntrada, 0, wx.ALL|wx.EXPAND, 5 )

		self.lblStopW = wx.StaticText( self, wx.ID_ANY, u"Stop Win", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblStopW.Wrap( -1 )

		self.lblStopW.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer2.Add( self.lblStopW, 0, wx.ALL|wx.EXPAND, 5 )

		self.lblStopL = wx.StaticText( self, wx.ID_ANY, u"Stop Loss", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.lblStopL.Wrap( -1 )

		self.lblStopL.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer2.Add( self.lblStopL, 0, wx.EXPAND|wx.ALL, 5 )

		cbContaChoices = [ u"DEMO", u"REAL" ]
		self.cbConta = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbContaChoices, 0 )
		gSizer2.Add( self.cbConta, 0, wx.ALL|wx.EXPAND, 5 )

		self.txtVrEntrada = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 9999999999999, 0 )
		gSizer2.Add( self.txtVrEntrada, 0, wx.ALL|wx.EXPAND, 5 )

		self.txtStopW = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 9999999999999, 0 )
		gSizer2.Add( self.txtStopW, 0, wx.ALL|wx.EXPAND, 5 )

		self.txtStopL = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 9999999999999, 0 )
		gSizer2.Add( self.txtStopL, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( gSizer2, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		radConfigChoices = [ u"Valor Fixo", u"Gale", u"Soros" ]
		self.radConfig = wx.RadioBox( self, wx.ID_ANY, u"Configurações", wx.DefaultPosition, wx.DefaultSize, radConfigChoices, 3, wx.RA_SPECIFY_COLS )
		self.radConfig.SetSelection( 0 )
		self.radConfig.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4.Add( self.radConfig, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.txtOption = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Opções", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtOption.Wrap( -1 )

		self.txtOption.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.txtOption.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		sbSizer1.Add( self.txtOption, 0, wx.ALL, 5 )

		m_comboBox4Choices = [ u"Digital", u"Binária" ]
		self.m_comboBox4 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox4Choices, 0 )
		self.m_comboBox4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_comboBox4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		sbSizer1.Add( self.m_comboBox4, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( sbSizer1, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.btParam = wx.Button( self, wx.ID_ANY, u"Paramêtros", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btParam, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.lblGain = wx.StaticText( self, wx.ID_ANY, u"Ganhos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblGain.Wrap( -1 )

		self.lblGain.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer3.Add( self.lblGain, 0, wx.ALL|wx.EXPAND, 5 )

		self.lblPerda = wx.StaticText( self, wx.ID_ANY, u"Perdas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPerda.Wrap( -1 )

		self.lblPerda.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gSizer3.Add( self.lblPerda, 0, wx.ALL|wx.EXPAND, 5 )

		self.txtGain = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer3.Add( self.txtGain, 0, wx.ALL|wx.EXPAND, 5 )

		self.txtPerda = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		gSizer3.Add( self.txtPerda, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( gSizer3, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.btIniciar = wx.Button( self, wx.ID_ANY, u"Iniciar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btIniciar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btIniciar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer10.Add( self.btIniciar, 1, wx.ALL, 5 )

		self.btParar = wx.Button( self, wx.ID_ANY, u"Parar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btParar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btParar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer10.Add( self.btParar, 1, wx.ALL, 5 )


		bSizer3.Add( bSizer10, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		listChoices = []
		self.list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), listChoices, 0 )
		bSizer6.Add( self.list, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )
		# Connect Events
		self.btParam.Bind( wx.EVT_BUTTON, self.openParams )
		self.btIniciar.Bind( wx.EVT_BUTTON, self.Iniciar )
		self.btParar.Bind( wx.EVT_BUTTON, self.parar )

	def __del__( self ):
		pass

	def openParams(self, event):
		params = Params(self)
		params.Show()

	def Iniciar(self, event):		
		startSignals(self.email,self.senha,self.Iq,self.cbConta.GetValue(),self.txtVrEntrada.GetValue(),self.txtStopW.GetValue(),self.txtStopL.GetValue(),self.radConfig.GetSelection(),self.m_comboBox4.GetValue(),self.list,self.txtGain,self.txtPerda)

	def parar(self,event):
		configDigital.StopProcess(1)
		configBinaria.StopProcess(1)
		self.list.Append('Parando...')



###########################################################################
## Class Params
###########################################################################

class Params ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.SetIcon(wx.Icon('img/faviiconBot.ico', wx.BITMAP_TYPE_ICO))

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		gSizer10 = wx.GridSizer( 0, 4, 0, 0 )

		self.lblGale1 = wx.StaticText( self, wx.ID_ANY, u"Gale 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblGale1.Wrap( -1 )

		self.lblGale1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		gSizer10.Add( self.lblGale1, 1, wx.ALL|wx.EXPAND, 5 )

		self.lblGale2 = wx.StaticText( self, wx.ID_ANY, u"Gale 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblGale2.Wrap( -1 )

		self.lblGale2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		gSizer10.Add( self.lblGale2, 1, wx.ALL|wx.EXPAND, 5 )

		self.lblGale3 = wx.StaticText( self, wx.ID_ANY, u"Gale 3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblGale3.Wrap( -1 )

		self.lblGale3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		gSizer10.Add( self.lblGale3, 1, wx.ALL|wx.EXPAND, 5 )

		self.lblGale4 = wx.StaticText( self, wx.ID_ANY, u"Gale 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblGale4.Wrap( -1 )

		self.lblGale4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		gSizer10.Add( self.lblGale4, 1, wx.ALL|wx.EXPAND, 5 )

		self.txtGale1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0 )
		gSizer10.Add( self.txtGale1, 0, wx.ALL, 5 )

		self.txtGale2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0 )
		gSizer10.Add( self.txtGale2, 0, wx.ALL, 5 )

		self.txtGale3 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0 )
		gSizer10.Add( self.txtGale3, 0, wx.ALL, 5 )

		self.txtGale4 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0 )
		gSizer10.Add( self.txtGale4, 0, wx.ALL, 5 )


		bSizer8.Add( gSizer10, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )

		self.m_staticText33 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Nivel de Soros", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		sbSizer2.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.txtSoros = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0 )
		sbSizer2.Add( self.txtSoros, 0, wx.ALL, 5 )


		bSizer8.Add( sbSizer2, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.btVoltar = wx.Button( self, wx.ID_ANY, u"Voltar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btVoltar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )
		# Connect Events
		self.btVoltar.Bind( wx.EVT_BUTTON, self.saveParams )		

	def __del__( self ):
		pass

	def saveParams(self, event):
		self.Hide()
		print('Salvando:',self.txtGale1.GetValue(),self.txtGale2.GetValue(),self.txtGale3.GetValue(),self.txtGale4.GetValue())
		print('Soros:',self.txtSoros.GetValue())
		Valor.append(self.txtGale1.GetValue())
		Valor.append(self.txtGale2.GetValue())
		Valor.append(self.txtGale3.GetValue())
		Valor.append(self.txtGale4.GetValue())
		Soros.append(self.txtSoros.GetValue())

		return 'Sucess'


###########################################################################
## Class MyDialog3
###########################################################################

class MsgDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ERROR", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetIcon(wx.Icon('img/erroIco.ico', wx.BITMAP_TYPE_ICO))

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		# self.imgError = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"img/error.png", wx.BITMAP_TYPE_ANY), wx.DefaultPosition,wx.Size( 150,250 ), 0 )
		# bSizer14.Add( self.imgError, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.txtMsg = wx.StaticText( self, wx.ID_ANY, u"Ops usuário ou senha inválidas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtMsg.Wrap( -1 )

		self.txtMsg.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer14.Add( self.txtMsg, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

#########################  REGRA    ##########################################
#########################   DE      ##########################################
#########################  NEGOCIO  ##########################################

def loadSinais():
	from datetime import datetime
	dados= DbHelper.selectSinais()
	for x in dados:
		# print(x)
		horario = str(x[1])
		paridade= x[2].replace('/','')
		acao = x[3]
		execs = x[4]
		time = x[5].replace('M','')
		DbHelper.insert(horario,paridade,acao,time,execs)

	return 'OK'

def startSignals(login,senha,Iq,comboConta,vrEntrada,StopWin,StopLoss,btn0,btn1,Lb1,Gains,Perdas):
	Lb1.Append('Iniciando....')
	print('=================================================================================================')
	print(login,senha,comboConta,vrEntrada,StopWin,StopLoss,btn0,btn1)
	print('=================================================================================================')
	valor = Valor


	if comboConta == 'DEMO':
		typeAccount = 'PRACTICE'
	elif comboConta == 'REAL':
		typeAccount = 'REAL'


	if btn1 == 'Digital':
		print('ENTROU AQUI')
		print(btn0)
		Thread(target = configDigital.defineBalance, args=(btn0,Iq)).start()
		if btn0 == 0:
			print('Valor Fixo')

			try:
				Thread(target = MonitorEntradasDigital, args = (login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,Lb1,Gains,Perdas)).start()
			except:
				print('__________')

		elif btn0 == 1:
			print('Gale')		
			try:
				Thread(target = MonitorEntradasGaleDigital, args=(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,valor,Lb1,Gains,Perdas)).start()
			except:
				print('__________')		

		elif btn0 == 2:
			print('Soros')
			
			try:
				Thread(target = MonitorEntradasSoroDigital, args=(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,Soros,Lb1,Gains,Perdas)).start()
			except:
				print('__________')		
		
		else:
			print('Nenhuma das opções')


	if btn1 == 'Binária':
		if btn0 == 0:
			print('Valor Fixo')
			Thread(target = configBinaria.defineBalance, args=(btn0,Iq)).start()
			try:
				Thread(target = MonitorEntradasBinaria, args=(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,Lb1,Gains,Perdas)).start()
			except:
				print('__________')

		elif btn0 == 1:
			print('Gale')		
			try:
				Thread(target = MonitorEntradasGaleBinaria, args=(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,valor,Lb1,Gains,Perdas)).start()
			except:
				print('__________')		

		elif btn0 == 2:
			print('Soros')
			
			try:
				Thread(target = MonitorEntradasSoroBinaria, args=(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,Soros,Lb1,Gains,Perdas)).start()
			except:
				print('__________')		


# Regra Monitorar robo
def MonitorEntradasDigital(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,Lb1,Gains,Perdas):
	from datetime import datetime
	now = {'hor': 0}
	while True:
		now['hor'] = datetime.now().strftime('%H:%M:%S')
		data = DbHelper.selectSinal(now['hor'])
		print(now['hor'])
		print('=======================================')
		print(data)
		for i in data:
			print(i)
			if(i[4] == 'N'):
				# print("id"+str(i[0])+" par"+str(i[2])+" acao"+str(i[3]))
				id = i[0]
				par = i[2]
				acao = i[3].lower()
				timeFrame = i[5]
				x = Thread(target= configDigital.MaoFixa, args=(id,Iq,par,typeAccount,vrEntrada,acao,StopWin,StopLoss,timeFrame,Lb1,Gains,Perdas)).start()

		time.sleep(0.5)

def MonitorEntradasGaleDigital(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,valor,Lb1,Gains,Perdas):
	from datetime import datetime
	now = {'hor': 0}	
	while True:
		now['hor'] = datetime.now().strftime('%H:%M:%S')
		data = DbHelper.selectSinal(now['hor'])
		print(now['hor'])
		for i in data:
			print(i)
			if(i[4] == 'N'):
				# print("id"+str(i[0])+" par"+str(i[2])+" acao"+str(i[3]))
				id = i[0]
				par = i[2]
				acao = i[3].lower()
				timeFrame = i[5]
				x = Thread(target= configDigital.entradasGale, args=(id,Iq,par,typeAccount,vrEntrada,acao,StopWin,StopLoss,timeFrame,int(valor[0]),int(valor[1]),int(valor[2]),int(valor[3]),Lb1,Gains,Perdas)).start()
				()

		time.sleep(0.5)


def MonitorEntradasSoroDigital(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,soro,Lb1,Gains,Perdas):
	from datetime import datetime
	now = {'hor': 0}	
	while True:
		now['hor'] = datetime.now().strftime('%H:%M:%S')
		data = DbHelper.selectSinal(now['hor'])
		print(now['hor'])
		for i in data:
			print(i)
			if(i[4] == 'N'):
				# print("id"+str(i[0])+" par"+str(i[2])+" acao"+str(i[3]))
				id = i[0]
				par = i[2]
				acao = i[3].lower()
				timeFrame = i[5]
				x = Thread(target= configDigital.entradasSoro, args=(id,Iq,par,typeAccount,vrEntrada,acao,StopWin,StopLoss,timeFrame,soro,Lb1,Gains,Perdas)).start()

		time.sleep(0.5)


def MonitorEntradasBinaria(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,Lb1,Gains,Perdas):
	from datetime import datetime
	now = {'hor': 0}	
	while True:
		now['hor'] = datetime.now().strftime('%H:%M:%S')
		data = DbHelper.selectSinal(now['hor'])
		print(now['hor'])
		for i in data:
			print(i)
			if(i[4] == 'N'):
				# print("id"+str(i[0])+" par"+str(i[2])+" acao"+str(i[3]))
				id = i[0]
				par = i[2]
				acao = i[3].lower()
				timeFrame = i[5]
				x = Thread(target= configBinaria.MaoFixa, args=(id,Iq,par,typeAccount,vrEntrada,acao,StopWin,StopLoss,timeFrame,Lb1,Gains,Perdas)).start()

		time.sleep(0.5)
			

def MonitorEntradasGaleBinaria(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,valor,Lb1,Gains,Perdas):
	from datetime import datetime
	now = {'hor': 0}	
	while True:
		now['hor'] = datetime.now().strftime('%H:%M:%S')
		data = DbHelper.selectSinal(now['hor'])
		print(now['hor'])
		for i in data:
			print(i)
			if(i[4] == 'N'):
				# print("id"+str(i[0])+" par"+str(i[2])+" acao"+str(i[3]))
				id = i[0]
				par = i[2]
				acao = i[3].lower()
				timeFrame = i[5]
				x = Thread(target= configBinaria.entradasGale, args=(id,Iq,par,typeAccount,vrEntrada,acao,StopWin,StopLoss,timeFrame,int(valor[0]),int(valor[1]),int(valor[2]),int(valor[3]),Lb1,Gains,Perdas)).start()

		time.sleep(0.5)


def MonitorEntradasSoroBinaria(login,senha,Iq,typeAccount,vrEntrada,StopWin,StopLoss,btn0,soro,Lb1,Gains,Perdas):
	from datetime import datetime
	now = {'hor': 0}	
	while True:
		now['hor'] = datetime.now().strftime('%H:%M:%S')
		data = DbHelper.selectSinal(now['hor'])
		print(now['hor'])
		for i in data:
			print(i)
			if(i[4] == 'N'):
				# print("id"+str(i[0])+" par"+str(i[2])+" acao"+str(i[3]))
				id = i[0]
				par = i[2]
				acao = i[3].lower()
				timeFrame = i[5]
				x = Thread(target= configBinaria.entradasSoro, args=(id,Iq,par,typeAccount,vrEntrada,acao,StopWin,StopLoss,timeFrame,soro,Lb1,Gains,Perdas)).start()

		time.sleep(0.5)


def deleteOperators():

	DbHelper.deleteAll()
	DbHelper.deleteAllOperators()
	# os.system("taskkill /im Python.exe")
	# os.system("taskkill /im Bot.exe")

	return 'Sucess'

deleteOperators()