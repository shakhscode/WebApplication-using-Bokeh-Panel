{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import panel as pn\n",
    "from bokeh import events\n",
    "from bokeh.models import Button, CustomJS\n",
    "\n",
    "\n",
    "\n",
    "def tpage():\n",
    "    if True:\n",
    "        with open('spage.py') as infile:\n",
    "            exec(infile.read())   \n",
    "\n",
    "b1 = Button(label= 'Finish Registration', button_type = 'primary')\n",
    "#b1.on_click(tpage)\n",
    "\n",
    "t1 = pn.widgets.TextInput(name='Name', placeholder='your name')\n",
    "t2 = pn.widgets.TextInput(name='Surname', placeholder='your surname')\n",
    "t3 = pn.widgets.TextInput(name='Date of Birth', placeholder='date-month-year')\n",
    "t4 = pn.widgets.TextInput(name='Document Id', placeholder='document number')\n",
    "\n",
    "firstpage = pn.template.FastListTemplate(\n",
    "    title = ' Registration',\n",
    "    main = [pn.Row(pn.Spacer(width =700),t1),\n",
    "            pn.Row(pn.Spacer(width =700),t2),\n",
    "            pn.Row(pn.Spacer(width =700),t3),\n",
    "            pn.Row(pn.Spacer(width =700),t4),\n",
    "            pn.Row(pn.Spacer(width =700),b1),\n",
    "           \n",
    "           ]\n",
    "                                       )\n",
    "firstpage.servable()\n",
    "firstpage.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
