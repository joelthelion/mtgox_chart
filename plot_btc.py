#!/usr/bin/env python2
# coding: utf-8
from json import loads,load
from urllib2 import urlopen
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from datetime import datetime

#data=load(urlopen("http://mtgox.com/code/data/getTrades.php"))
data=load(open("getTrades.php"))

date,price,amount = [],[],[]
for d in data:
    date.append(datetime.fromtimestamp(d["date"]))
    price.append(d["price"])
    amount.append(d["amount"])

fig=Figure(figsize=(10,6))
ax1=fig.add_subplot(111)
ax1.scatter(date,price,s=amount)
fig.autofmt_xdate()
ax1.set_xlabel("Time (UTC)")
ax1.set_ylabel("Price ($/BTC)")
ax1.set_title("Latest transactions at Mt. Gox")
canvas=FigureCanvasAgg(fig)
canvas.print_figure("mtgox.png",dpi=200)
