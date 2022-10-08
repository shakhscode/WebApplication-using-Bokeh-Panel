import panel as pn
from bokeh import events
from bokeh.models import Button, CustomJS



def visit():
        with open('plotsPanel.py') as infile:
            exec(infile.read())   


b4 = Button(label = 'View Reports', button_type = 'primary')
b4.on_click(visit)
fpage = firstpage = pn.template.FastListTemplate(
    title = ' ',
    main = [pn.Row(pn.Spacer(width =720),'#### GETTING DATA FROM THE DEVICES'),
           pn.Row( pn.Spacer(width =710),'#### DATA ANALYSED, REPORTS ARE READY'),
           pn.Row( pn.Spacer(width =700),b4),
           ]
                                       )
fpage.servable()
fpage.show()