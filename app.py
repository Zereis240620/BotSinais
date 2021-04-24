import front
# import noname
import wx


class InitialApp(front.Login):
	def __init__(self,parent):
		front.Login.__init__(self, parent)


app = wx.App()
frame = InitialApp(None)

frame.Show()

app.MainLoop()
