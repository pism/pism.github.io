##### Getting the dev source code

The PISM source code is hosted at
[github.com/pism/pism](http://github.com/pism/pism). The
default branch is *master*, which is the current stable version of PISM.

To get the *dev* branch you can either clone the repository and then
checkout the *dev* branch, or you can ask for the *dev* branch from the
start:

git clone -b dev [git://github.com/pism/pism.git](git://github.com/pism/pism.git) pism-dev

##### The dev manual

=

See <http://pism.github.io/pism/>, which follows the *dev* branch.
Meanwhile the [main documentation
page](https://pism-docs.org/wiki/doku.php?id=overview)
corresponds to the most recent release.

##### Installing tools and libraries

See the [Installation
Manual](http://pism-docs.org/sphinx/installation/index.html)
for the list of tools and libraries necessary to build PISM.

For the development version you need a recent version of
[PETSc](http://www.mcs.anl.gov/petsc/download/index.html).
Configuring and building PETSc might be as simple
as export PETSC_DIR=pwd  export PETSC_ARCH=linux-c-dbg
cd $PETSC_DIR ./configure make all make test

##### Building the dev version

See the *INSTALL.md* file in the source. Basically you do:

<code>{=html} cd pism-dev mkdir \'your build directory\' cd \'your
build directory\' ccmake .. \# type \'c\' as soon as it runs, then set
variables as needed,

              #   then 'g' to generate (you can toggle advanced mode with 't'
              #   to get lots of control)

make install </code>{=html}

If you see configuration-related issues (missing libraries, etc.) at
this stage then go back to ccmake .. and fix them.

After exiting \"ccmake\" (e.g. by re-generating the makefile), do

make install
pisms # very minimal test; should run and produce NetCDF (.nc) file
make test # will do thorough test if python tools and NCO are available

##### Tracking commits

The source code host site [allows you to browse the source and see
recent changes](https://github.com/pism/pism) and to post
[issues](https://github.com/pism/pism/issues?sort=created&direction=desc&state=open),
which you can tag as bugs, tasks or feature requests.

To get updates by e-mail, please go to
<http://groups.google.com/group/pism-commits> and join the group. (This
requires a Google Mail account.)

If you are using a different e-mail system, you can either

* create a Google Mail account just for this purpose and set up e-mail forwarding, or
* use a RSS feed provided by GitHub: [https://github.com/pism/pism/commits/dev.atom](https://github.com/pism/pism/commits/dev.atom)

Here are the latest five commits (from the RSS feed link above):

{=mediawiki}
{{rss>https://github.com/pism/pism/commits/dev.atom 5 author date 1h }}


##### Staying up to date

Get the latest features, bugs, and perhaps their fixes:

    cd pism-dev
    git pull
    cd 'your build directory'
    make install

See the [User\'s Manual (dev)](http://pism.github.io/pism/)
to get the user-level view of PISM even if you think you know
everything. See also the [Installation Manual
(dev)](http://pism.github.io/pism/installation/index.html)
for instructions on how build the documentation yourself.
