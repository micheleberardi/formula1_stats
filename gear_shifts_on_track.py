"""Gear shifts on track
=======================

Plot which gear is being used at which point of the track
"""

##############################################################################
# Import FastF1 and load the data

import fastf1

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import numpy as np

from modules import defines
import os

# SETTING SESSION
ENV = (os.path.dirname(os.path.realpath(__file__)))
year = 2022
gp = "Austria Grand Prix"


fastf1.Cache.enable_cache(ENV+str('/cache'))  # replace with your cache directory

session = fastf1.get_session(year, gp, 'Q')
session.load()

lap = session.laps.pick_fastest()
tel = lap.get_telemetry()
# sphinx_gallery_defer_figures

##############################################################################
# Prepare the data for plotting by converting it to the appropriate numpy
# data types

x = np.array(tel['X'].values)
y = np.array(tel['Y'].values)

points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
gear = tel['nGear'].to_numpy().astype(float)
# sphinx_gallery_defer_figures

##############################################################################
# Create a line collection. Set a segmented colormap and normalize the plot
# to full integer values of the colormap

cmap = cm.get_cmap('Paired')
lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N+1), cmap=cmap)
lc_comp.set_array(gear)
lc_comp.set_linewidth(4)
# sphinx_gallery_defer_figures

##############################################################################
# Create the plot

plt.gca().add_collection(lc_comp)
plt.axis('equal')
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

title = plt.suptitle(
    f"Fastest Lap Gear Shift Visualization\n"
    f"{lap['Driver']} - {session.event['EventName']} {session.event.year}"
)
# sphinx_gallery_defer_figures


##############################################################################
# Add a colorbar to the plot. Shift the colorbar ticks by +0.5 so that they
# are centered for each color segment.

cbar = plt.colorbar(mappable=lc_comp, label="Gear", boundaries=np.arange(1, 10))
cbar.set_ticks(np.arange(1.5, 9.5))
cbar.set_ticklabels(np.arange(1, 9))


# match the driver name to the color


plt.show()
#plt.savefig(ENV+str('images/gear_'+str(year)+'_'+str(gp)+'.png'))
#media_ids = ENV+str('images/gear_'+str(year)+'_'+str(gp)+'.png')
#tr = (f"️️️🏎️ Fastest Lap Gear Shift Visualization\n 🏁" f"{lap['Driver']} - {session.event['EventName']} {session.event.year}")
#twitterpost = (str(tr))
#twitterpost += "\n \n Stats create with FastF1 project \n but for better stats and info follow @F1DataAnalysis on Twitter \n  #formula1 #f1 #formula1data"
#twitterpost = twitterpost
#defines.twitter(twitterpost,media_ids)
