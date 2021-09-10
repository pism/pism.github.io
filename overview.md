---
title: Overview
subtitle: What is PISM?
layout: page
hero_height: is-medium
hero_image: /img/header_torsten_2.JPG
hero_caption: "Photo: T. Albrecht"
hero_darken: false
show_sidebar: true
---

# What is PISM?

The Parallel Ice Sheet Model (PISM) is a computer program used in climate science to simulate the past and future of glaciers and ice sheets, including the Earth's two large ice sheets in Greenland and Antarctica.

# Why are ice sheets important?

The ice sheets in Greenland and Antarctica are big, continent-sized glaciers more than three kilometers thick. Mass loss from glaciers and ice sheets affects global sea level, making the task of estimating their future contribution to sea-level societally relevant. Depending on how much global temperatures rise, sea level may rise only a fraction of a meter or up to one or two meters in the next century. In the past, as the Earth went in and out of the ice ages, there were huge changes of tens of meters over several millennia. Ice flow models like PISM are important tools to assess the range of possibile sea level rise scenarios.

# What does an ice-sheet model do?

Ice sheets behave like very slow-moving fluids. PISM simulates the movement of this ice fluid, just like a weather forecasting model simulates the atmosphere. Ice moves slower than the atmosphere, so PISM can be used to simulate decades, centuries, or millenia of flow, while a weather model works over just days.

See this [excellent 5 minute movie](https://www.imaginary.org/film/the-future-of-glaciers) by Guillaume Jouvet, introducing what a glacier flow model does. PISM works similarly, but on the much larger scale of an ice sheet like Greenland or Antarctica.

# Why is PISM special?

PISM is open source, parallel, and capable of simulations at high resolution. It has been [widely adopted](/publications/) as a tool for doing science.

Features include:

 * extensible atmospheric/ocean coupling
 * shallow, hybrid, and higher-order stress balances
 * marine ice sheet physics
 * polythermal energy conservation
 * subglacial hydrology and till model
 * complete [documentation](https://pism.github.io/docs/)
 * parallel simulations using [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) & [PETSc](http://www.mcs.anl.gov/petsc/)
 * reads and writes [CF-compliant](http://cfconventions.org/) [NetCDF](http://www.unidata.ucar.edu/software/netcdf/)
 * verification and validation tools
