import panel as pn
from bokeh import events
from bokeh.models import Button, CustomJS
import webbrowser


def visit():
        with open('snpage.py') as infile:
            exec(infile.read())
            
b1 = Button(label= 'REGISTER', button_type = 'primary')
b1.on_click(visit)

im1 = pn.pane.JPG('im1.jpg', width=500)

firstpage = pn.template.FastListTemplate(
    title = 'Welcome to my application',
    main = [pn.Row(pn.Spacer(width =600),im1),
            pn.Row(pn.Spacer(width =700),b1)
           
           ]
                                       )
firstpage.servable()
firstpage.show()