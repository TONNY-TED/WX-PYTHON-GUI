import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='BoxSizer Example')
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(wx.StaticText(panel, label='TONNY CHI:'), flag=wx.ALL, border=5)
        vbox.Add(wx.TextCtrl(panel, value='initial text'), flag=wx.EXPAND | wx.ALL, border=5)
        vbox.Add(wx.Button(panel, label='Press Me'), flag=wx.ALL, border=5)
        vbox.Add(wx.RadioButton(panel, label='Male', style=wx.RB_GROUP), flag=wx.ALL, border=5)
        vbox.Add(wx.RadioButton(panel, label='Female'), flag=wx.ALL, border=5)
        vbox.Add(wx.CheckBox(panel, label='I agree'), flag=wx.ALL, border=5)
        vbox.Add(wx.ComboBox(panel, choices=['tonny', 'charles', 'tama', 'zaithwa', 'bless']), flag=wx.ALL, border=5)
        vbox.Add(wx.Slider(panel, value=50, minValue=0, maxValue=100), flag=wx.EXPAND | wx.ALL, border=5)

        panel.SetSizer(vbox)
        self.Show()

app = wx.App()
frame = MyFrame()
app.MainLoop()
