###### Installing PISM on systems with unusual PETSc installations

PISM uses the CMake script *FindPETSc.cmake* to learn about your PETSc
installation. This page describes a way to build PISM using a PETSc
installation that heuristics in *FindPETSc.cmake* fail on.

We need to set the following CMake variables:

* *PETSC_FOUND*        - system has PETSc
* *PETSC_INCLUDES*     - the PETSc include directories
* *PETSC_LIBRARIES*    - Link these to use PETSc
* *PETSC_COMPILER*     - Compiler used by PETSc, helpful to find a compatible MPI
* *PETSC_DEFINITIONS*  - Compiler switches for using PETSc
* *PETSC_MPIEXEC*      - Executable for running MPI programs
* *PETSC_VERSION*      - Version string (MAJOR.MINOR.SUBMINOR)

In addition to this, setting *PETSC\_EXECUTABLE\_RUNS* to *YES* disables
checks in *FindPETSc.cmake*.

Below is a CMake script that can be used as a template:

\<file cmake petsc\_manual\_config.cmake\> set (PETSC\_EXECUTABLE\_RUNS
YES CACHE BOOL \"Disable checking if this setup works\" FORCE)

set (PETSC\_FOUND YES CACHE BOOL \"PETSc was found (manually)\" FORCE)

set (PETSC\_INCLUDES \"EDIT THIS\" CACHE STRING

` "Semicolon-delimited list of PETSc include directories" FORCE)`

set (PETSC\_LIBRARIES \"EDIT THIS\" CACHE STRING

` "Semicolon-delimited list of PETSc libraries" FORCE)`

set (PETSC\_COMPILER \"EDIT THIS\" CACHE FILEPATH

` "PETSc compiler; helpful to find a compatible MPI" FORCE)`

set (PETSC\_DEFINITIONS \"EDIT THIS\" CACHE STRING

` "PETSc definitions" FORCE)`

set (PETSC\_MPIEXEC \"EDIT THIS\" CACHE FILEPATH

` "Executable for running PETSc MPI programs" FORCE)`

set (PETSC\_VERSION \"EDIT THIS\" CACHE STRING

` "PETSc version: MAJOR.MINOR.SUBMINOR" FORCE)`

mark\_as\_advanced (PETSC\_INCLUDES PETSC\_LIBRARIES

` PETSC_COMPILER PETSC_DEFINITIONS
` PETSC_MPIEXEC PETSC_EXECUTABLE_RUNS PETSC_VERSION)`

`</file>`{=html}

###### How do I use this?

- Download the script quoted above.
- Edit to match your PETSc installation.
- Run *cmake -C path/to/petsc_manual_config.cmake path/to/pism-source* in your build directory.
- Follow the rest of PISM's [build instructions](installation).
