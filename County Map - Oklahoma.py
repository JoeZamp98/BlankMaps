import awips
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import awips
from awips.dataaccess import DataAccessLayer

from metpy.plots import USCOUNTIES

#Setting the Projection

proj = ccrs.LambertConformal(central_longitude=-95, central_latitude=35, standard_parallels=[35])

plt.rcParams['savefig.dpi']

#Creating the Internal Figure

fig = plt.figure(figsize = (20,10))
ax = fig.add_subplot(1,1,1, projection=proj)

#Adding County Boundaries

for scale, axis in zip(['5m'], ['ax']):
    ax.add_feature(USCOUNTIES.with_scale(scale), edgecolor="lightgray")

#Adding State Boundaries

ax.add_feature(cfeature.STATES)
ax.add_feature(cfeature.BORDERS)
ax.set_extent((-104, -93, 32.5, 37.4))
ax.set_title(str("***ADD HEADLINE HERE***"))

plt.show()