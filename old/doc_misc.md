###### Some visualization advice

##### Using Matplotlib Basemap toolkit to plot over a map

To install Basemap, see
<http://matplotlib.sourceforge.net/basemap/doc/html/>.

To use a Blue Marble background, you will also need the [Python Imaging
Library](http://www.pythonware.com/products/pil/).

Below is an example plotting csurf (the magnitude of the horizontal ice
velocity at the ice surface) using a logarithmic color scale and marking
the 100 ^m^/~year~ contour in black:

++++ Click here to see the source of basemap\_ex1.py \| \<code python
basemap\_ex1.py\>

1.  !/usr/bin/env python

from mpl\_toolkits.basemap import Basemap, NetCDFFile import numpy as np
import matplotlib.pyplot as plt from matplotlib import colors

nc = NetCDFFile(\"g10km\_0.nc\", \'r\')

1.  we need to know longitudes and latitudes corresponding to out grid

lon = nc.variables\[\'lon\'\]\[:\] lat = nc.variables\[\'lat\'\]\[:\]

1.  x and y *in the dataset* are only used to determine plotting
    domain
2.  dimensions

x = nc.variables\[\'x\'\]\[:\] y = nc.variables\[\'y\'\]\[:\] width =
x.max() - x.min() height = y.max() - y.min()

1.  load data and mask out ice-free areas

fill = nc.variables\[\'csurf\'\].\_FillValue csurf =
np.squeeze(nc.variables\[\'csurf\'\]\[:\]) csurf = np.ma.array(csurf,
mask = csurf == fill)

m = Basemap(width=2*width, \# width in projection coordinates, in
meters

`           height=height,      # height
`           resolution='l',     # coastline resolution, can be 'l' (low), 'h'
`                               # (high) and 'f' (full)
`           projection='stere', # stereographic projection
`           lat_ts=71,          # latitude of true scale
`           lon_0=-41,          # longitude of the plotting domain center
`           lat_0=72)           # latitude of the plotting domain center`

1.  m.drawcoastlines()

```{=html}
<!-- -->
```
1.  draw the Blue Marble background (requires PIL, the Python Imaging
    Library)

m.bluemarble()

1.  convert longitudes and latitudes to x and y:

xx,yy = m(lon, lat)

1.  mark 100 m/a contours in black:

m.contour(xx, yy, csurf, \[100\], colors=\"black\")

1.  plot csurf using log color scale

m.pcolormesh(xx,yy,csurf,

`            norm=colors.LogNorm(vmin=1, vmax=5e3)) # use log color scale,
`                                                    # omit this to use linear
`                                                    # color scale`

1.  add a colorbar:

plt.colorbar(extend=\'both\',

`            ticks=[2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 3000],
`            format="%d")`

1.  draw parallels and meridians. The labels argument specifies where to
    draw
2.  ticks: \[left, right, top, bottom\]

m.drawparallels(np.arange(-55.,90.,5.), labels = \[1, 0, 0, 0\])
m.drawmeridians(np.arange(-120.,30.,10.), labels = \[0, 0, 0, 1\])

plt.title(r\"Modeled ice surface velocity, m/year\")
plt.savefig(\'g10km\_0\_csurf.png\') `</code>`{=html} ++++

The following alternative python code does nearly the same thing but
uses
[netcdf4-python](https://code.google.com/p/netcdf4-python/)
to read NetCDF:

++++ Click here to see the source of basemap\_ex2.py \| \<code python
basemap\_ex2.py\>

1.  !/usr/bin/env python

from mpl\_toolkits.basemap import Basemap

from netCDF4 import Dataset as NC

import numpy as np import matplotlib.pyplot as plt from matplotlib
import colors import sys

rootname=\'g10km\_0\'

try:

`   nc = NC(rootname+'.nc', 'r')`

except:

`   print "ERROR: can't read from file ..."
`   sys.exit(1)`

1.  we need to know longitudes and latitudes corresponding to out grid

lon = nc.variables\[\'lon\'\]\[:\] lat = nc.variables\[\'lat\'\]\[:\]

1.  x and y *in the dataset* are only used to determine plotting
    domain
2.  dimensions

x = nc.variables\[\'x\'\]\[:\] y = nc.variables\[\'y\'\]\[:\] width =
x.max() - x.min() height = y.max() - y.min()

1.  load data and mask out ice-free areas

fill = nc.variables\[\'csurf\'\].\_FillValue csurf =
np.squeeze(nc.variables\[\'csurf\'\]\[:\]) csurf = np.ma.array(csurf,
mask = csurf == fill)

m = Basemap(width=1.2*width, \# width in projection coordinates, in
meters

`           height=height,      # height
`           resolution='l',     # coastline resolution, can be 'l' (low), 'h'
`                               # (high) and 'f' (full)
`           projection='stere', # stereographic projection
`           lat_ts=71,          # latitude of true scale
`           lon_0=-41,          # longitude of the plotting domain center
`           lat_0=72)           # latitude of the plotting domain center`

1.  m.drawcoastlines()

```{=html}
<!-- -->
```
1.  draw the Blue Marble background (requires PIL, the Python Imaging
    Library)

m.bluemarble()

1.  convert longitudes and latitudes to x and y:

xx,yy = m(lon, lat)

1.  mark 100 m/a contour in black:

m.contour(xx, yy, csurf, \[100\], colors=\"black\")

1.  plot csurf using log color scale

m.pcolormesh(xx,yy,csurf,

`            norm=colors.LogNorm(vmin=1, vmax=6e3)) # use log color scale,
`                                                    # omit this to use linear
`                                                    # color scale`

1.  add a colorbar:

plt.colorbar(extend=\'both\',

`            ticks=[2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000],
`            format="%d")`

1.  draw parallels and meridians. The labels argument specifies where to
    draw
2.  ticks: \[left, right, top, bottom\]

m.drawparallels(np.arange(-55.,90.,5.), labels = \[1, 0, 0, 0\])
m.drawmeridians(np.arange(-120.,30.,10.), labels = \[0, 0, 0, 1\])

plt.title(r\"modeled surface velocity, m/year\")
plt.savefig(rootname+\'\_csurf.png\') `</code>`{=html} ++++

This is the output of basemap\_ex1.py: {{ g10km\_0\_csurf.png?500 }}
