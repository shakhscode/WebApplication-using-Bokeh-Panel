import panel as pn
from bokeh import events
from bokeh.models import Button, CustomJS



def visit():
        with open('frpage.py') as infile:
            exec(infile.read())   


b3 = Button(label = 'Connect to Spirometer & Oximeter', button_type = 'primary')
b3.on_click(visit)

im1 = pn.pane.JPG('im2.jpg', height = 450, width = 450)
im2 = pn.pane.JPG('im3.jpg', height = 450 , width = 450)

tpage = pn.template.FastListTemplate(
    title = ' ',
    main = [pn.Row( pn.Spacer(width =750),'### Registration Completed.'),
            pn.Row(pn.Spacer(width =400),im1,im2),
            pn.Row( pn.Spacer(width =700),b3)
           ]
                                       )
tpage.servable()
tpage.show()