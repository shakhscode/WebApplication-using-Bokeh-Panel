import panel as pn
from bokeh import events
from bokeh.models import Button, CustomJS



def visit():
        with open('frpage.py') as infile:
            exec(infile.read())   


b3 = Button(label = 'Connect to the devices', button_type = 'primary')
b3.on_click(visit)
tpage = pn.template.FastListTemplate(
    title = ' ',
    main = [pn.Row( pn.Spacer(width =750),'### Registration Completed !')
            ,pn.Row( pn.Spacer(width =700),b3),
           ]
                                       )
tpage.servable()
tpage.show()