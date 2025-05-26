import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='FlexGridSizer Example')
        panel = wx.Panel(self)

        flex = wx.FlexGridSizer(rows=4, cols=2, vgap=10, hgap=10)

        flex.AddGrowableCol(1, 1)  # Allow column 2 to expand

        flex.Add(wx.StaticText(panel, label='TONNY CHI:'), 0, wx.ALL, 5)
        flex.Add(wx.TextCtrl(panel, value='initial text'), 1, wx.EXPAND | wx.ALL, 5)
        flex.Add(wx.Button(panel, label='Press Me'), 0, wx.ALL, 5)
        flex.Add(wx.RadioButton(panel, label='Male', style=wx.RB_GROUP), 0, wx.ALL, 5)
        flex.Add(wx.RadioButton(panel, label='Female'), 0, wx.ALL, 5)
        flex.Add(wx.CheckBox(panel, label='I agree'), 0, wx.ALL, 5)
        flex.Add(wx.ComboBox(panel, choices=['tonny', 'charles', 'tama', 'zaithwa', 'bless']), 0, wx.ALL, 5)
        flex.Add(wx.Slider(panel, value=50, minValue=0, maxValue=100), 1, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(flex)
        self.Show()

app = wx.App()
frame = MyFrame()
app.MainLoop()
