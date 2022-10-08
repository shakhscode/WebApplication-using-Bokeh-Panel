import panel as pn
from bokeh import events
from bokeh.models import Button, CustomJS



def tpage():
    if True:
        with open('trpage.py') as infile:
            exec(infile.read())   

b1 = Button(label= 'Finish Registration', button_type = 'primary')
#b1.on_click(tpage)

t1 = pn.widgets.TextInput(name='Name', placeholder='your name')
t2 = pn.widgets.TextInput(name='Surname', placeholder='your surname')
t3 = pn.widgets.TextInput(name='Date of Birth', placeholder='date-month-year')
t4 = pn.widgets.TextInput(name='Document Id', placeholder='document number')

firstpage = pn.template.FastListTemplate(
    title = ' Registration',
    main = [pn.Row(pn.Spacer(width =700),t1),
            pn.Row(pn.Spacer(width =700),t2),
            pn.Row(pn.Spacer(width =700),t3),
            pn.Row(pn.Spacer(width =700),t4),
            pn.Row(pn.Spacer(width =700),b1),
           
           ]
                                       )
firstpage.servable()
firstpage.show()