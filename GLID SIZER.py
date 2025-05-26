import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='GridSizer Example')
        panel = wx.Panel(self)

        # 4 rows, 2 columns
        grid = wx.GridSizer(4, 2, 10, 10)

        grid.Add(wx.StaticText(panel, label='TONNY CHI:'))
        grid.Add(wx.TextCtrl(panel, value='initial text'))
        grid.Add(wx.Button(panel, label='Press Me'))
        grid.Add(wx.RadioButton(panel, label='Male', style=wx.RB_GROUP))
        grid.Add(wx.RadioButton(panel, label='Female'))
        grid.Add(wx.CheckBox(panel, label='I agree'))
        grid.Add(wx.ComboBox(panel, choices=['tonny', 'charles', 'tama', 'zaithwa', 'bless']))
        grid.Add(wx.Slider(panel, value=50, minValue=0, maxValue=100))

        panel.SetSizer(grid)
        self.Show()


app = wx.App()
frame = MyFrame()
app.MainLoop()
