"""Overlaying speed traces of two laps
======================================

Compare two fastest laps by overlaying their speed traces.
"""

import matplotlib.pyplot as plt
import fastf1.plotting
from modules import defines
import os



# SETTING SESSION
ENV = (os.path.dirname(os.path.realpath(__file__)))
year = 2022
gp = "Austria Grand Prix"

fastf1.Cache.enable_cache('cache')  # replace with your cache directory

# enable some matplotlib patches for plotting timedelta values and load
# FastF1's default color scheme
fastf1.plotting.setup_mpl()

# load a session and its telemetry data
session = fastf1.get_session(year, gp, 'Q')
session.load()

##############################################################################
# First, we select the two laps that we want to compare

ver_lap = session.laps.pick_driver('VER').pick_fastest()
ham_lap = session.laps.pick_driver('LEC').pick_fastest()

##############################################################################
# Next we get the telemetry data for each lap. We also add a 'Distance' column
# to the telemetry dataframe as this makes it easier to compare the laps.

ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()

##############################################################################
# Finally, we create a plot and plot both speed traces.
# We color the individual lines with the driver's team colors.

rbr_color = fastf1.plotting.team_color('RBR')
mer_color = fastf1.plotting.team_color('MER')

fig, ax = plt.subplots()
ax.plot(ver_tel['Distance'], ver_tel['Speed'], color=rbr_color, label='VER')
ax.plot(ham_tel['Distance'], ham_tel['Speed'], color=mer_color, label='LEC')

ax.set_xlabel('Distance in m')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Fastest Lap Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")

plt.savefig(ENV+str('images/'+str(year)+'_'+str(gp)+'.png'))

#plt.show()
plt.savefig(ENV+str('images/'+str(year)+'_'+str(gp)+'.png'))
media_ids = ENV+str('images/'+str(year)+'_'+str(gp)+'.png')
tr = (f"🏎️ Fastest Lap Comparison \n 🏁 {session.event['EventName']} {session.event.year} Qualifying")
twitterpost = (str(tr))
twitterpost += "\n \n Stats create with FastF1 project \n but for better stats and info follow @F1DataAnalysis on Twitter \n  #formula1 #f1 #formula1data"
twitterpost = twitterpost
defines.twitter(twitterpost,media_ids)