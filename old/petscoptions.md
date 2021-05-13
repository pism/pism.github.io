###### PETSc options appropriate to SSA solves in PISM {#petsc_options_appropriate_to_ssa_solves_in_pism}

Jed Brown, [a PETSc
developer](http://www.mcs.anl.gov/petsc/petsc-2/miscellaneous/index.html)
and an original PISM author, gave this example of comparing which were
the efficient solvers for a saved, invertible linear system that came
from an SSA solve. This example, which uses 8 MPI processes, mostly
shows that no method of these is outstandingly better than another. See
also the page on [diagnosing and resolving \"KSP diverged\"
errors](kspdiverged).

`<code>`{=html}

1.  Additive Schwarz with overlap 1

\$ time mpiexec -n 8 ./ex10 -f SSAFD\_ksperror.petsc -ksp\_type gmres
-ksp\_norm\_type unpreconditioned -ksp\_pc\_side right -pc\_type asm
-sub\_pc\_type lu Number of iterations = 19 Residual norm 92.3905

real 0m3.142s user 0m22.881s sys 0m1.012s

1.  Umfpack instead of PETSc subdomain solves, slightly faster

\$ time mpiexec -n 8 ./ex10 -f SSAFD\_ksperror.petsc -ksp\_type gmres
-ksp\_norm\_type unpreconditioned -ksp\_pc\_side right -pc\_type asm
-sub\_pc\_type lu -sub\_pc\_factor\_mat\_solver\_package umfpack Number
of iterations = 19 Residual norm 92.3905

real 0m2.436s user 0m18.369s sys 0m0.728s

1.  More overlap, a little better

\$ time mpiexec -n 8 ./ex10 -f SSAFD\_ksperror.petsc -ksp\_type gmres
-ksp\_norm\_type unpreconditioned -ksp\_pc\_side right -pc\_type asm
-sub\_pc\_type lu -sub\_pc\_factor\_mat\_solver\_package umfpack
-pc\_asm\_overlap 2 Number of iterations = 14 Residual norm 139.529

real 0m2.357s user 0m17.329s sys 0m0.792s

1.  No overlap, slower and less robust

\$ time mpiexec -n 8 ./ex10 -f SSAFD\_ksperror.petsc -ksp\_type gmres
-ksp\_norm\_type unpreconditioned -ksp\_pc\_side right -pc\_type bjacobi
-sub\_pc\_type lu -sub\_pc\_factor\_mat\_solver\_package umfpack Number
of iterations = 32 Residual norm 153.677

real 0m2.997s user 0m22.681s sys 0m0.916s

1.  preconditioned norm, less accurate

\$ time mpiexec -n 8 ./ex10 -f SSAFD\_ksperror.petsc -ksp\_type gmres
-ksp\_norm\_type preconditioned -ksp\_pc\_side left -pc\_type bjacobi
-sub\_pc\_type lu -sub\_pc\_factor\_mat\_solver\_package umfpack Number
of iterations = 18 Residual norm 30777.5

real 0m2.441s user 0m17.865s sys 0m0.840s

`</code>`{=html}
