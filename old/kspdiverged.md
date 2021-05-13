###### Diagnosing and resolving stress balance solver failures from PISM

Suppose you get a report from PISM like this: `<code>`{=html} PISM
WARNING: Effective viscosity not converged after 300 outer iterations

` with nuH_regularization=1.00e+13.
` failed with nuH_regularization = 10000000000000.00.
` re-trying with nuH_regularization multiplied by     4.00...`

\... PISM WARNING: Effective viscosity not converged after 300 outer
iterations

` with nuH_regularization=1.02e+16.
` re-trying using the Additive Schwarz preconditioner...`

PISM WARNING: Effective viscosity not converged after 300 outer
iterations

` with nuH_regularization=1.00e+13.`

PISM ERROR: all SSAFD strategies failed. PISM ERROR: SSA solver failed.
PISM ERROR: Shallow stress balance solver failed. PISM ERROR: stress
balance computation failed. Saving model state to
\'out\_stressbalance\_failed.nc\'\... `</code>`{=html}

This message might also be like `<code>`{=html} PISM WARNING: KSPSolve()
reports \'diverged\'; reason = -3 = \'DIVERGED\_ITS\'

` writing linear system to PETSc binary file SSAFD_kspdivergederror.petsc ...`

`</code>`{=html}

These failures are signs that the problem seen by the elliptic stress
balance solver, the SSA solver, is for some reason too difficult.
Roughly speaking, for the first case the computed estimate of the
temperature-dependent strength of the shear-thinning ice is not behaving
well, while for the second case, the condition number of the system is
large, although it may be that your options for PISM have generated an
actually unsolvable system.

Why do these errors occur sporadically? As far as we understand, the
reason is that at some timestep and some location in the ice sheet there
is very thin ice (e.g. \< 10 m), or there is ice with very weak basal
resistance. At the same places we think there is high driving stress or
membrane stress gradients. That is, the problem is a local nastyness for
the stress balance, generating one or a few rows of the linear system
that have nearly-zero coefficients. (//If the reason were really clear
we would probably have already fixed it. Simple and quickly-reproducible
cases that generate these errors, on coarse grids, would be greatly
appreciated.//)

So, how do you resolve these errors in PISM runs?

- The failure may be resolved by adding options.  Specifically, an iceberg may have been created, for which the stress balance is ill-posed (i.e. not invertible even in theory).  You should use *-kill_icebergs*.  More general advice is to use *-pik*, which implies *-kill_icebergs*, for most runs.
- The problem occurs most often with steep bed topography.  The special problematic case may be nunataks, i.e. steep mountains poking up through the ice sheet.  Consider using a smoother interpolation scheme for the bed topography, if that is justified given the bed elevation data you have.
- In the "*KSPSolve() reports 'diverged*'" case you may observe that the system is solvable with stronger PETSc linear solver options.  Specifically, you can add these "direct subdomain solves" options to your PISM run:

-ssafd_ksp_type gmres -ssafd_ksp_norm_type unpreconditioned -ssafd_ksp_pc_side right -ssafd_pc_type asm -ssafd_sub_pc_type lu

The run will likely be about a factor of two slower but it will probably
not generate the errors. For more discussion of PETSc solver options
which may help with performance and robustness of PISM runs, see [the
page on PETSc solver options](petscoptions).

### Examining a saved linear system in a .petsc file

This comment applies in the \"*KSPSolve() reports \'diverged*\'\" case.

Jed Brown, [a PETSc
developer](http://www.mcs.anl.gov/petsc/petsc-2/miscellaneous/index.html)
and a PISM author, has the following diagnostic advice: //You can load
in the binary file and use solvers on that single linear system. This
scales to large problems (e.g. SSA solves on 10km Antarctica grids and
such), and is not just a toy. Here is testing using *ex10* which is the
compiled form of *src/ksp/ksp/examples/tutorials/ex10.c* from the PETSc
source code. We try direct subdomain solves, a robust starting point to
see that the system is not invertible in this case://
$ ./ex10 -f SSAFD_kspdivergederror.petsc -ksp_type gmres -ksp_norm_type unpreconditioned -ksp_pc_side right -pc_type asm -sub_pc_type lu
[0]PETSC ERROR: --------------------- Error Message ------------------------------------
[0]PETSC ERROR: Detected zero pivot in LU factorization
see [http://www.mcs.anl.gov/petsc/petsc-as/documentation/faq.html#ZeroPivot](http://www.mcs.anl.gov/petsc/petsc-as/documentation/faq.html#ZeroPivot)!
[0]PETSC ERROR: Zero pivot row 126954 value 0 tolerance 1e-12!
[0]PETSC ERROR: ------------------------------------------------------------------------
[0]PETSC ERROR: Petsc Release Version 3.2.0, Patch 5, Sat Oct 29 13:45:54 CDT 2011
...
