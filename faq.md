---
title: Frequently asked questions
subtitle: FAQs and PISM life hacks
layout: page
hero_height: is-medium
hero_image: https://cdn.imaggeo.egu.eu/media/uploads/2015/02/28/c7551d79e7f144911384c731d08cdedd.jpg
hero_caption: "Photo: <a href='https://imaggeo.egu.eu/view/3171/'>J.-M. Nasse / imaggeo </a>"
hero_darken: false
show_sidebar: true
---

# How to visualize PISM results?

## - Ncview

For a quick view into PISM's netCDF output files, `Ncview` is a useful tool. For more information, see [here](http://cirrus.ucsd.edu/ncview/).

## - Python

- examples using the `xarray` package:
    - [Visualisation of PISM output (interactive online jupyter notebook)](https://mybinder.org/v2/gh/m-kreuzer/pism.github.io/HEAD?filepath=jupyter%2Fpism_output_visualisation_example.ipynb)
    - [Antarctic paleo ensemble](https://gallery.pangeo.io/repos/ldeo-glaciology/pangeo-glaciology-examples/04_paleo_PISM.html)
- [<i class="fab fa-github fa-lg"></i> pypismtools](https://github.com/pism/pypismtools) is a collection of python classes and functions to evaluate studies made with PISM
- [Cartopy](https://scitools.org.uk/cartopy/) is another useful python package (based on [matplotlib](https://matplotlib.org/)), especially for plotting data on maps. For a list of useful Python plotting tools, see [here](http://www.marknagelberg.com/overview-python-and-non-python-mapping-tools-for-data-scientists/).

## - QGIS 
- See [<i class="fab fa-github fa-lg"></i> repos](https://github.com/pism/pism-qgis) and [<i class="fab fa-github fa-lg"></i> resources](https://github.com/pism/QGIS-Resources) for more information.


# How do I install PISM on a High Performance Computer?
Scripts that help to build PISM and its prerequisites (such as PETSc) on some HPC system are provided [here](https://github.com/pism/pism-builds).


# How do I prepare real data for input to PISM?

[This page](/data/) collects resources to make prepare input data for Antarctic, Greenland and Arctic PISM applications.

Furthermore, useful command line tools to edit and modify NetCDF data are [Climate Data Operators (CDO](https://code.mpimet.mpg.de/projects/cdo) and [netCDF Operator (NCO)](http://nco.sourceforge.net/). A good compilation for regridding is found [here](https://www.climate-cryosphere.org/wiki/index.php?title=Regridding_with_CDO).



# How do I report a bug in PISM?
Please see the [Issue tracking at github](https://github.com/pism/pism/issues) to check if someone already found a similar bug. You can post an issue there, and label it as a bug, if it is new. For more information, see [here](https://pism-docs.org/sphinx/contributing/bug-reporting.html). 

# How do I cite PISM in a publication that uses it?
See the information given [here](http://www.pism.io/citing/).

# A stress balance solve failed. What do I do?
[This page](/faq_stress_balance_error/) gives more information on this.


# How do I create a parameter ensemble of PISM simulations?
For an example for Antarctica, see the [<i class="fab fa-github fa-lg"></i> pism-emulator](https://github.com/pism/pism-emulator)




