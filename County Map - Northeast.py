import awips
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import awips
from awips.dataaccess import DataAccessLayer

from metpy.plots import USCOUNTIES

#Setting the Projection

proj = ccrs.LambertConformal(central_longitude=-72.5, central_latitude=42, standard_parallels=[35])

plt.rcParams['savefig.dpi']

#Creating the Figure

fig = plt.figure(figsize = (20,10))
ax = fig.add_subplot(1,1,1, projection=proj)

#Adding County Boundaries

for scale, axis in zip(['5m'], ['ax']):
    ax.add_feature(USCOUNTIES.with_scale(scale), edgecolor="lightgray")

#Adding State Boundaries

ax.add_feature(cfeature.STATES)
ax.add_feature(cfeature.BORDERS)
ax.set_extent((-65, -80, 37, 47))
ax.set_title(str("***ADD HEADLINE HERE***"))

plt.show()