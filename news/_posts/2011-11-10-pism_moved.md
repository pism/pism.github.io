---
title: We have moved (and switched to PETSc 3.2)
date: 2011-11-10 12:00
---

As promised in an *earlier news item*, we have moved source code hosting from [gna.org](http://web.archive.org/web/20170505010209/https://mail.gna.org/public/project/2016-11/msg00001.html) to [github.com](https://github.com/pism/pism).

PISM now requires [PETSc 3.2](https://www.mcs.anl.gov/petsc/index.html).
For now, this change affects the development version, but the Spring
2012 `stable0.5` release will be available at
[github.com](https://github.com/pism/pism) only and will not support
PETSc 3.1 and earlier.

You can find the new repository at <https://github.com/pism/pism>.

We now use Git <http://git-scm.com/> to manage the source code. Use the
following command if you already have Git and want the stable version:

    git clone git://github.com/pism/pism.git pism0.4

In the current setup this `master` branch contains the latest stable
release (i.e. 0.4 these days). Please do not commit to `master`,
because stable releases are managed by PISM developers at UAF.
Contributed code should go into the `dev` branch; this is the
equivalent of `trunk` in the old Subversion repository. The
following will put you on the `dev` branch

    cd pism0.4
    git checkout dev

Also, you can still use Subversion to get the code-- no need to install
Git on a supercomputer, just run

    svn co https://github.com/pism/pism pism0.4

Please use <https://github.com/pism/pism/issues> to report bugs, submit
tasks, or request features. (You will need to create a
<http://github.com> account.) If you would like to contribute to PISM
then see *committing*.

Switching from Subversion to Git may take some getting used to; below
are two links to resources we recommend:

* ["Pro Git"](https://git-scm.com/book/en/v2) by Scott Chacon
* a [video](http://www.youtube.com/watch?v=ZDR433b0HJY) about Git (also by Scott Chacon)

The repository at <http://web.archive.org/web/20170331083829/https://gna.org/projects/pism/> will still be there,
but will not be updated. In other words, you have to use the new one to
get bug-fixes.
