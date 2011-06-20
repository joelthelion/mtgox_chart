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

def make_graph(exchange_name, url):
    print "Downloading the data from %s ..." % exchange_name
    try:
        json = None
        json = urlopen(url).read()
        data = loads(json)
    except Exception as e:
        if json: 
            print json
        print e
        print "Connection problem, giving up for %s" % exchange_name
        return

    print "Parsing the data..."
    date,price,amount = [],[],[]
    for d in data:
        date.append(datetime.fromtimestamp(d["date"]))
        price.append(float(d["price"]))
        amount.append(float(d["amount"]))

    print "Plotting..."
    fig=Figure(figsize=(10,6))
    ax1=fig.add_subplot(111)

# Tweak the alpha setting to change the transparency of each circle
    ax1.scatter(date,price,s=amount,alpha=0.1)

    fig.autofmt_xdate()
    ax1.set_xlabel("Time (UTC)")
    ax1.set_ylabel("Price ($/BTC)")
    ax1.set_title("Latest transactions at %s" % exchange_name)
    canvas=FigureCanvasAgg(fig)
    print "Rasterizing..."
    canvas.print_figure("%s.png"%exchange_name,dpi=200)
    print "Done!"

# Change here to use the live data
#for exchange_name,url in [("local","getTrades.php")]:
for exchange_name,url in [("mtgox","https://mtgox.com/code/data/getTrades.php"),
        ("tradehill","https://api.tradehill.com/APIv1/USD/Trades")]:
    make_graph(exchange_name,url)

