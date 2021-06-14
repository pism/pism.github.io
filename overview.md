---
title: Overview
subtitle: What is PISM?
layout: page
hero_height: is-medium
hero_image: /pism_website_test/img/header_pism3d.png
hero_darken: false
show_sidebar: true
---

# What is PISM?

The Parallel Ice Sheet Model (PISM) is a computer program used in climate science to simulate the past and future of the Earth's two large ice sheets in Greenland and Antarctica.

# Why are Ice Sheets Important?

The ice sheets in Greenland and Antarctica are big, continent-sized glaciers and are more than two miles (more than four kilometers) thick. These ice sheets affect the rate at which global sea level rises. The question is how fast the changes can happen. Under global warming conditions, sea level may rise only a fraction of a meter or up to one or two meters in the next century. In the past, as the Earth went in and out of the ice ages, there were huge changes of tens of meters over several millenia. An ice-sheet flow model like PISM is part of understanding such possibilities.

# What Does an Ice-sheet Model do?

Ice sheets behave like very slow-moving fluids. PISM simulates the movement of this ice fluid, just like a weather forecasting model simulates the atmosphere. Ice moves slower than the atmosphere, so PISM can be used to simulate decades, centuries, or millenia of flow, while a weather model works over just days.

See this [excellent 5 minute movie](https://www.imaginary.org/film/the-future-of-glaciers) by Guillaume Jouvet, introducing what a glacier flow model does. PISM works similarly, but on the much larger scale of an ice sheet like Greenland or Antarctica.

# Why is PISM Special?

PISM is open source and capable of high resolution. It has been widely adopted as a tool for doing science.

Features include:

 * extensible atmospheric/ocean coupling
 * hybrid shallow stress balance
 * marine ice sheet physics
 * polythermal energy conservation
 * subglacial hydrology and till model
 * complete [documentation](https://pism-docs.org/sphinx/)
 * parallel simulations using [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) & [PETSc](http://www.mcs.anl.gov/petsc/)
 * reads and writes [CF-compliant](http://cfconventions.org/) [NetCDF](http://www.unidata.ucar.edu/software/netcdf/)
 * [inversion toolbox in Python](http://www.pism-docs.org/doxy/inverse/html/index.html)
 * verification and validation tools