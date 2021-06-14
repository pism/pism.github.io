###### Frequently Asked Questions (FAQ)

### How do I visualize PISM results, like modeled surface velocity, using python scripts?

 * Answer 1: [A script which calls the "basemap" toolkit from Matplotlib in python](doc_misc)\
 * Answer 2: A more complete tool at [github.com/pism](https://github.com/pism): [PyPISMTools](https://github.com/pism/PyPISMTools)

### How do I prepare real data for input to PISM?

 * Answer 1: You can start with the SeaRISE data sets, which are already in the NetCDF format, and modify their metadata, as in the Greenland example, the Antarctica example, and the Jakobshavn regional model example in the PISM User's Manual.  The preprocessing scripts in question are part of the PISM release.\
 * Answer 2: Similarly, SeaRISE and MEaSURES data sets are combined in the Ross ice shelf example, documented in the PISM User's Manual, which is part of the PISM release.\
 * Answer 3: You can see several Greenland data set examples, using [data from NSIDC](http://nsidc.org/data/data-search.html) and other sources, in the collection [data-preprocessing](https://github.com/pism/data-preprocessing) at [github.com/pism](https://github.com/pism).\
 * Answer 4: Even if you cannot start with data in existing NetCDF files, you can at least quickly create a PISM-readable NetCDF file with the right dimensions for "bootstrapping", i.e. for the option *-boot_file*.  See [PISMNC.py](https://github.com/pism/pism/blob/stable0.6/util/PISMNC.py), which is in the PISM release in directory *util/*.

### How do I report a bug in PISM?

Answer: See [this page](reporting_bugs).

### How do I cite PISM in a publication that uses it?

Answer: See [this page](citing_pism).

### A stress balance solve failed. What do I do?

Answer: See [this page](kspdiverged).

### What options are best to give to PETSc for the SSA stress balances solve in PISM?

Answer: See [this page](petscoptions).

### PISM build issues:

How do I check which libraries were found by CMake?
---------------------------------------------------

++++ Answer \|

Run \"*ccmake .*\" in the build directory and press \"*t*\".\\\\ \\\\
Alternatively, the file *CMakeCache.txt* in the build directory contains
PISM\'s configuration.\\\\ \\\\ One can also run \"*VERBOSE=1 make*\"
instead of just \"*make*\" to see all the commands, their flags, etc
during the build process. ++++

I accidentally installed PISM in /usr/local/. How do I clean up the mess?
-------------------------------------------------------------------------

++++ Answer \| Run `xargs rm < install_manifest.txt` in the build
directory. (Add \"*sudo*\" if necessary.)\\\\ \\\\ This will delete all
the files installed by CMake but will not remove directories. (Note that
\"*make install*\" could have overwritten something and this damage
cannot be undone.) ++++

How do I tell CMake to use a particular MPI implementation?
-----------------------------------------------------------

++++ Answer \| From \"*man cmake*\":

The MPI compiler is stored in the cache variable *MPI\_COMPILER*, and
will attempt to look for commonly-named drivers \..., *mpicxx*, *mpiCC*,
or *mpicc*. If the compiler driver is found and recognized, it will be
used to set all of the module variables. To skip this auto-detection,
set *MPI\_LIBRARY* and *MPI\_INCLUDE\_PATH* in the CMake cache.

If no compiler driver is found or the compiler driver is not recognized,
this module will then search for common include paths and library names
to try to detect MPI.

If CMake initially finds a different MPI than was intended, and you want
to use the MPI compiler auto-detection for a different MPI
implementation, set *MPI\_COMPILER* to the MPI compiler driver you want
to use (e.g., *mpicxx*) and then set *MPI\_LIBRARY* to the string
*MPI\_LIBRARY-NOTFOUND*. When you re-configure, auto-detection of MPI
will run again with the newly-specified *MPI\_COMPILER*. ++++

### How do I \... write source code using PISM C++ classes?

Answer: See [this page in the
manual](http://pism-docs.org/sphinx/technical/index.html) and [the
source code browser](http://www.pism-docs.org/doxy/html/index.html).