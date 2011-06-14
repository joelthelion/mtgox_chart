#!/usr/bin/env python2
# coding: utf-8
"""
This simple script parses the Mt. Gox trade data and displays it in a
nice chart. It needs Matplotlib to work. By default it works on a local
version of the code. Change the relevant line to enable live data.

The code is licensed under the GNU Affero GPL, version 3
(http://www.gnu.org/licenses/agpl.html), and copyright Joël Schaerer, 011
"""

from json import loads,load
from urllib2 import urlopen
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from datetime import datetime

# Change here to use the live data
#print "Downloading the data from Mt. Gox ..."
#data=load(urlopen("http://mtgox.com/code/data/getTrades.php"))
data=load(open("getTrades.php"))

print "Parsing the data..."
date,price,amount = [],[],[]
for d in data:
    date.append(datetime.fromtimestamp(d["date"]))
    price.append(d["price"])
    amount.append(d["amount"])

print "Plotting..."
fig=Figure(figsize=(10,6))
ax1=fig.add_subplot(111)

# Tweak the alpha setting to change the transparency of each circle
ax1.scatter(date,price,s=amount,alpha=0.1)

fig.autofmt_xdate()
ax1.set_xlabel("Time (UTC)")
ax1.set_ylabel("Price ($/BTC)")
ax1.set_title("Latest transactions at Mt. Gox")
canvas=FigureCanvasAgg(fig)
print "Rasterizing..."
canvas.print_figure("mtgox.png",dpi=200)
print "Done!"
