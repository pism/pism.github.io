---
title: Frequently asked questions
subtitle: FAQs and PISM life hacks
layout: page
hero_height: is-medium
hero_image: https://cdn.imaggeo.egu.eu/media/uploads/2015/02/28/c7551d79e7f144911384c731d08cdedd.jpg
hero_caption: "Photo: <a href='https://imaggeo.egu.eu/view/3171/'>J.-M. Nasse / imaggeo </a>"
hero_darken: false
toc: true
show_sidebar: true
---

## How do I visualize PISM results?

### Ncview

For a quick view into PISM's NetCDF output files, [Ncview](http://meteora.ucsd.edu/~pierce/ncview_home_page.html) is a useful
tool.

### Python

Some recommendations for Python packages that allow easy plotting of NetCDF datasets are listed below:
- [xarray](http://xarray.pydata.org/) is simple and efficient, see the examples below:
    - [Example 1: Visualisation of PISM output](https://nbviewer.org/github/pism/pism.github.io/blob/main/jupyter/pism_visualisation_python.ipynb)
    - [Example 2: Antarctic paleo ensemble](https://gallery.pangeo.io/repos/ldeo-glaciology/pangeo-glaciology-examples/04_paleo_PISM.html)
- [<i class="fab fa-github fa-lg"></i> pypismtools](https://github.com/pism/pypismtools) is a collection of Python classes and functions to evaluate studies made with PISM
- [Cartopy](https://scitools.org.uk/cartopy/docs/latest/) and [GeoPandas](https://geopandas.org) (or the earlier but deprecated [Basemap](https://matplotlib.org/basemap/index.html)) are useful Python packages (based on [matplotlib](https://matplotlib.org/)), especially for plotting data on maps
- [PyGMT](https://www.pygmt.org/) is a Python interface for the [Generic Mapping Tools (GMT)](https://www.generic-mapping-tools.org/)
- [Hyoga](https://hyoga.readthedocs.io) is a thin wrapper around xarray to read and plot PISM output, written by Julien Seguinot

For a list of more useful Python plotting tools, see [here](http://www.marknagelberg.com/overview-python-and-non-python-mapping-tools-for-data-scientists/).

### QGIS 

See [<i class="fab fa-github fa-lg"></i> repos](https://github.com/pism/pism-qgis) and [<i class="fab fa-github fa-lg"></i> resources](https://github.com/pism/QGIS-Resources) for more information.

### Panoply
[Panoply](https://www.giss.nasa.gov/tools/panoply/) is a cross-platform NetCDF data viewer actively developed by NASA and more comprehensive than Ncview (requires Java).

> ### Color tables
> Here's a link collection to some nice color maps:
> - [Scientific colour maps](https://www.fabiocrameri.ch/colourmaps/) by Fabio Crameri: perceptually uniform, readable both by colour-vision deficient and colour-blind people, citable & reproducible
> - [cmocean](https://matplotlib.org/cmocean/): Perceptually uniform beautiful color maps for oceanography
> - [ColorBrewer](https://colorbrewer2.org/): Color advice for cartography
>
> For even more scale color tables, J.J. Green's [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/) website includes countless color palettes in various file formats.


## How do I install PISM on a High Performance Computer?

Scripts that help build PISM and its prerequisites (such as PETSc) on some HPC system are provided [<i class="fab fa-github fa-lg"></i> here](https://github.com/pism/pism-builds).

## How do I prepare real data for input to PISM?

[This page](/data/) lists resources that can help you prepare input data for Antarctic, Greenland and Arctic PISM applications.

Furthermore, command line tools

- [Climate Data Operators (CDO)](https://code.mpimet.mpg.de/projects/cdo)
- [NetCDF Operators (NCO)](http://nco.sourceforge.net/)

are useful for manipulating data in the NetCDF format.

See [Regridding with CDO](https://www.climate-cryosphere.org/wiki/index.php?title=Regridding_with_CDO)
for a good overview of regridding (interpolation between different grids) using CDO.

## How do I report a bug in PISM?

Please see the [<i class="fab fa-github fa-lg"></i> Issue tracking at github](https://github.com/pism/pism/issues) to check if someone already found a similar bug. You can post an issue there, and label it as a bug, if it is new. For more information, see [here](https://www.pism.io/docs/contributing/bug-reporting.html). 

## How do I cite PISM in a publication that uses it?

See the information given [here](/citing/).

## PISM's stress balance solver failed. What do I do?

[This page](/faq_stress_balance_error/) gives more information on this.

## How do I create a parameter ensemble of PISM simulations?

For an example for Antarctica, see the [<i class="fab fa-github fa-lg"></i> pism-ensemble](https://github.com/pism/pism-ensemble).




