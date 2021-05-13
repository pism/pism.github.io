###### PISM stable0.6 is out {#pism_stable0.6_is_out}

See the stable version page to check out a copy of the **PISM
stable0.6** source code. If you have already checked out the
prerelease version, just do *git pull* and then *make install* in your
build directory. Send email to
[help\@pism-docs.org](help@pism-docs.org) for help with any
version of PISM.

Changes since **stable0.5** include

### Basal strength and basal hydrology {#basal_strength_and_basal_hydrology}

++++ Click here to see the list \|

` - A significant change to the model physics for computing yield stress of saturated till: effective pressure in till is now computed by empirically-based (and exponential) formula from **[Tulaczyketal2000]** relating amount of water in till to effective pressure.`\
` - New mass-conserving subglacial hydrology model.`

++++

### Marine ice sheet modeling {#marine_ice_sheet_modeling}

++++ Click here to see the list \|

` - Implement a parameterization of the melange back pressure as a part of the stress boundary condition at the ice shelf front.`\
` - Implement fracture density model and fracture-induced ice softening (see **[AlbrechtLevermann2012]**).`\
` - Parameterization of the sub-grid position of the grounding line and related improvements (see **[Feldmannetal2014,Gladstoneetal2012]**).`\
` - MISMIP3D example (see **[MISMIP3d2013]**). PISM shows grounding line reversibility on a fixed grid.`\
` - Use an implementation of a serial two-scan connected-component algorithm to identify icebergs.`\
` - Report cumulative discharge (calving) flux as a 2D field.`

++++

### Climate inputs and ocean inputs {#climate_inputs_and_ocean_inputs}

++++ Click here to see the list \|

` - **`*`PISMSurfaceModel`*`** returns climatic mass balance in **`*`[kg`` ``m-2`` ``s-1]`*`**`\
` - Remove **`*`pclimate`*`**; add the **`*`-test_climate_models`*`** option.`\
` - **`*`-part_grid`*`** extended to grounded marine termini. Allows advance of grounded marine termini.`\
` - Require time bounds in time-dependent climate forcing.`\
` - Improve the PDD scheme. (Keeps track of the snow depth during the year to choose PDD factors but does not model multi-year snow cover.)`\
` - Implement the 3-equation sub-shelf melt parameterization (see **[Hellmer1998]**).`\
` - Implement caching surface and ocean models **`*`-ocean`` ``...,cache`*`** and **`*`-surface`` ``...,cache`*`**. (Update boundary inputs every X years but include interannual variability.)`\
` - Remove code supporting the **`*`EISMINT-Greenland`*`** setup.`

++++

### Inverse modeling tools are a part of this release {#inverse_modeling_tools_are_a_part_of_this_release}

Please see the [PISM\'s Python
Documentation](http://www.pism-docs.org/doxy/inverse/html/index.html).

### Energy and mass model improvements {#energy_and_mass_model_improvements}

++++ Click here to see the list \|

` - Improve mass conservation and mass transport.`\
` - New bootstrapping heuristic filling ice temperature at depth using surface mass balance (if available).`\
` - Allow "regridding" enthalpy from files containing ice temperature and liquid water fraction.`\
` - Allow cold flow laws in the enthalpy mode and the GPBLD flow law in the cold mode (equivalent to the Paterson-Budd in this case).`\
` - Corrected basal boundary condition in the enthalpy system.`

++++

### Improved User\'s Manual examples {#improved_users_manual_examples}

++++ Click here to see the list \|

` - "Standard" Greenland model example includes grid refinement and parameter study demonstrations.`\
` - New validation example based on laboratory experiment with xanthan gum, with millimeter-scale grid spacing.  Shows extreme configurability of PISM.`\
` - "Prognostic" Ross ice shelf example demonstrates eigen-calving law.`\
` - Reproducible MISMIP and MISMIP3d examples documented in Manual.`

++++

### Usability

++++ Click here to see the list \|

` - Implement poor man's parallel I/O, with compression`\
` - Ensure "continuity" in time of reported cumulative diagnostic fields.`\
` - Let the user precisely specify the dates corresponding to the run (**`*`-time_file`*`**).`\
` - PISM supports real-world calendars.`\
` - Many more diagnostic quantities; use **`*`-list_diagnostics`*`** to see.`\
` - PISM keeps track of options and parameters that were set but were not used.`\
` - Use projection info to compute latitude and longitude bounds. (Reduces post-processing needed to work with PISM's output.)`

++++

### Under the hood {#under_the_hood}

++++ Click here to see the list \|

` - Improve the build system.`\
` - Switch to `[`PETSC`` ``3.3`` ``or`` ``3.4`](http://www.mcs.anl.gov/petsc/)`. PETSc version 3.2 and earlier are no longer supported.`\
` - Switch to `[`UDUNITS-2`](http://www.unidata.ucar.edu/software/udunits/)`.`\
` - Require `[`FFTW-3`](http://www.fftw.org)` to build PISM.`\
` - Use `[`CalCalcs`](http://meteora.ucsd.edu/~pierce/calcalcs/)` for proper calendar support.`\
` - Remove the Debian "meta-" package.`\
` - Clean up command-line options selecting sub-models (calving, stress balance, energy, basal yield stress).`\
` - Implement a "constant 2D velocity" stress balance object (for testing and prescribing sliding)`\
` - Better **`*`SSAFD`*`** recovery logic; save model state on failure.`\
` - Use non-zero initial guess in the SSAFD KSP solver.`

++++
