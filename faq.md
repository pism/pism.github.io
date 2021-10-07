---
title: Frequently asked questions
subtitle: FAQs and PISM life hacks
layout: page
hero_height: is-medium
hero_image: /img/header_torsten_1.JPG
hero_caption: "Photo: T. Albrecht"
hero_darken: false
show_sidebar: true
---

# How to visualize PISM results?

## Ncview

For a quick view into PISM's netCDF output files, `Ncview` is a useful tool. For more information, see [http://cirrus.ucsd.edu/ncview/](http://cirrus.ucsd.edu/ncview/).

## Python

- examples using the `xarray` package:
    - [Visualisation of PISM output](https://mybinder.org/v2/gh/m-kreuzer/pism.github.io/HEAD?filepath=faq%2Fjupyter%2Fpism_output_visualisation_example.ipynb)
    - [Antarctic paleo ensemble](https://gallery.pangeo.io/repos/ldeo-glaciology/pangeo-glaciology-examples/04_paleo_PISM.html)
- [pypismtools](https://github.com/pism/pypismtools) is a collection of python classes and functions to evaluate studies made with PISM
- [Cartopy](https://scitools.org.uk/cartopy/) is another useful python package (based on [matplotlib](https://matplotlib.org/)), especially for plotting data on maps. For a list of useful Python plotting tools, see [here](http://www.marknagelberg.com/overview-python-and-non-python-mapping-tools-for-data-scientists/).
# QGIS 
- see [repos](https://github.com/pism/pism-qgis) and [resources](https://github.com/pism/QGIS-Resources)


# How do I install PISM on a High Performance Computer?
Scripts that help to build PISM and its prerequisites (such as PETSc) on some HPC system are provided [here](https://github.com/pism/pism-builds).


# How do I prepare real data for input to PISM?

- You can start with the [SeaRISE data sets](http://websrv.cs.umt.edu/isis/index.php/Data), which are already in the NetCDF format, and modify their metadata, as in the [Greenland example](https://pism-docs.org/sphinx/manual/std-greenland/input-data.html), the [Antarctica example](https://github.com/pism/pism/tree/master/examples/searise-antarctica), and the [Jakobshavn regional model example](https://pism-docs.org/sphinx/manual/jakobshavn/index.html) in the PISM User's Manual. The preprocessing scripts in question are part of the PISM release.

- Similarly, SeaRISE and MEaSURES data sets are combined in the [Ross ice shelf example](https://pism-docs.org/sphinx/manual/validation/ross.html), documented in the PISM User's Manual, which is part of the PISM release.
- You can see several Greenland data set examples, using data from NSIDC and other sources, in the collection [data-preprocessing](https://github.com/pism/data-preprocessing)
- Even if you cannot start with data in existing NetCDF files, you can at least quickly create a PISM-readable NetCDF file (using [PISMNC.py](https://github.com/pism/pism/blob/master/examples/preprocessing/PISMNC.py)) with the right dimensions for “bootstrapping” (using PISM's option `-bootstrap`).
- Some useful command line tools to edit and modify NetCDF data are [Climate Data Operators (CDO](https://code.mpimet.mpg.de/projects/cdo) and [netCDF Operator (NCO)](http://nco.sourceforge.net/). A good compilation for regridding is found [here](https://www.climate-cryosphere.org/wiki/index.php?title=Regridding_with_CDO).

# How do I report a bug in PISM?
Please see the [Issue tracking at github](https://github.com/pism/pism/issues) to check if someone already found a similar bug. You can post an issue there, and label it as a bug, if it is new. For more information, see [here](https://pism-docs.org/sphinx/contributing/bug-reporting.html). 

# How do I cite PISM in a publication that uses it?
See the information given [here](http://www.pism.io/citing/).

# A stress balance solve failed. What do I do?
See [this page](/faq_stress_balance_error/)


# How do I create a parameter ensemble of PISM simulations?
For an example for Antarctica, see [here](https://github.com/pism/pism-emulator)




