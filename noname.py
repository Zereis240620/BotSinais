# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,308 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"img/iconBot.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
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

		self.txtSenha = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
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

	def __del__( self ):
		pass


###########################################################################
## Class Home
###########################################################################

class Home ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 596,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 596,500 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

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

	def __del__( self ):
		pass


###########################################################################
## Class Params
###########################################################################

class Params ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

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

		self.m_spinCtrl20 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 0 )
		sbSizer2.Add( self.m_spinCtrl20, 0, wx.ALL, 5 )


		bSizer8.Add( sbSizer2, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.btVoltar = wx.Button( self, wx.ID_ANY, u"Voltar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.btVoltar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


