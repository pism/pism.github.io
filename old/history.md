###### A brief history of PISM {#a_brief_history_of_pism}

### before 2001 {#before_2001}

This page on the history of PISM got its start when Craig Lingle wrote
the following in an October 2015 email to Ed Bueler:

\> \[PISM\] actually has a fairly long background, extending back into
the "deep glaciological past," prior to when Vera Veronina (a Russian
emigre who was working for me on analysis of Antarctic satellite radar
altimeter data) decided to leave Fairbanks and accept an offer at U.C.
Boulder (she was a warm weather woman), so she introduced me to Elena
Troshina (now Suleimani, Ph.D., also a Russian emigre, who had completed
her M.S. in marine sciences based on her tsunami modeling). Elena said
she wanted to work for me.

\> I looked at her thesis, immediately recognized her mathematical and
numerical modeling abilities, and put her to work on improving the
(nominally Antarctic) ice sheet model I had been carrying around under
one arm (so to speak), through 3 moves, ever since I developed it (based
on Mary-Ann (M.A.W.) Mahaffey's equations and numerical method that she
had published in the Journal of Geophysical Research a few years earlier
(with minimal detail). I tested it against the analytical solution for a
circular ice cap on a flat bed with constant accumulation, and satisfied
myself that it was accurate. Then, I applied it to the 20 K BP CLIMAP
reconstruction of the Antarctic ice sheet (with the idea of modeling
forward from there to the present), and satisfied myself that it was
stable. Then, I set it aside, because it was... well.. too complicated
to address the "grounding line dynamics" problem I had in mind for my
Ph.D. thesis.

\> Many years passed. When Elena began working for me, I dug it up ---
still carefully preserved, in an archeological sense --- and asked Elena
to transform it from Fortran 4 to Fortran 90. She did. Then, I gave her
the equations for transforming the model equations to forms with a
stretched vertical coordinate. She was properly skeptical, and checked
all my equation. Then, she did. Then, I gave her the 3-D temperature
equation expressed with a stretched vertical coordinate, and asked her
to incorporate it. She again checked the equations, and did so. But, it
wasn't stable, for the reason you quickly identified when I first
introduced you to Elena, and we talked about that.

\> Anyway --- all that work by Elena led to the version of the ice sheet
model that you saw when you first expressed interest in it, and the
published paper \[C. Lingle and E. Troshina, 1998. //Relative magnitudes
of shear and longitudinal strain rates in the inland Antarctic ice
sheet, and response to increasing accumulation//, Ann. Glaciol. 27,
pp.187-193\] that enabled us to apply \[in 2001\] to NASA for
model-development funding \[namely grant NAG5-11371\].

### 2001: team forms {#team_forms}

At this point, because of Craig\'s initiative to expand it, the project
started including a lot more people.

In 2001 Craig Lingle attended a talk on heat equations on manifolds
given by Ed Bueler. Lingle suggested that Bueler might want to work on
modeling heat flow in glaciers. This became a short course by Craig on
glaciological basics, with Bueler, Latrice Bowman, Jed Brown, and Dave
Covey in attendance at various points. Craig optimistically led a
proposal to NASA, with Bueler and Covey as Co-Is, which was funded as
NAG5-11371, as a modeling component (sub-grant) of the U Kansas \"Polar
Radar for Ice Sheet Measurements\" (PRISM) project and NASA grant, to
build an Antarctic model which added thermomechanical coupling and ice
shelf dynamics to the existing Fortran model.

Bueler was interested in understanding numerical models by checking them
against exact predictions (solutions) of the differential equations.
This became a paper \[E. Bueler, C. Lingle, J. Kallen-Brown, D. Covey,
L. Bowman, 2005. //Exact solutions and verification of numerical models
for isothermal ice sheets//, J. Glaciol. 51 (173), 291\--306\], but the
first submission in 2003 did not get accepted. This work used Matlab
scripts, instead of the Fortran code, but it provided tests which,
around the time of the re-submission, were used to check the code that
would become PISM. In this period, Latrice was the first of Bueler\'s
graduate students to work on ice flow, with MS Math based on this work
in 2002.

### 2003: PETSc and C \... and PISM {#petsc_and_c_..._and_pism}

In 2002 Jed Brown became involved with PISM as an undergraduate, working
for a while with the Fortran code from Craig and Elena. Around 2003/04
Brown came into Bueler\'s office and said, essentially, that there was
this nice library that would allow us to work in parallel at a higher
conceptual level, namely
[PETSc](http://www.mcs.anl.gov/petsc/). And that we should
switch to C-plus-plus so that the code could be more modular. This
suggestion was not fully appreciated by Bueler, but it was fully
accepted. The Fortran code was dropped, object classes were defined, and
the isothermal SIA model, with under-development
thermomechanical-coupling code, rebuilt based on collaboration between
Brown and Bueler.

Three goals for major additions then followed, in a period when Brown
became very familiar with PETSc and Bueler finally learned C:

- Bueler led the effort to add thermocoupling to the SIA, with Brown
  and Lingle assistance, and emphasizing exact solutions to check.
  This became E. Bueler, J. Brown, and C. Lingle, (2007). //Exact
  solutions to the thermomechanically coupled shallow-ice
  approximation: effective tools for verification//, J. Glaciol. 53
  (182), 499--516.\
- Because Brown was now an MS student in math, Bueler suggested that
  Brown's MS project be the addition of, and testing of, a SSA solver
  in PISM. This led to a successful [August 2006 MS project
  defense](http://pism.github.io/uaf-iceflow/slidesJBrown.pdf). At
  that time the model had this (Bueler's suggestion) name: the
  C-plus-plus Object-oriented Multi-Modal, Verifiable Numerical Ice
  Sheet Model, a.k.a. COMMVNISM.\
- [NetCDF](http://www.unidata.ucar.edu/software/netcdf/) was adopted
  as the input/output format. Before this, PETSc binary files were
  used. (This fast format lacks included and standardized metadata.)

As this work was finishing, three things became clear: the multi-modal
aspect was not actually working, Brown would be graduating and leaving
for a PhD in Zurich, and another proposal would soon need to be written.
Brown renamed the model one day around this time\-\--with no
opposition\-\--to the less cumbersome and better-suited-to-a-proposal
name of \"Parallel Ice Sheet Model\", PISM.

### 2006: PISM goes public {#pism_goes_public}

In September 2006 PISM was for the first time hosted publicly, [on
GNA](http://gna.org/projects/pism/) with a [GNU General Public
License](http://svn.gna.org/viewcvs/pism/trunk/COPYING?view=log). We
benefited greatly from using [SVN](https://subversion.apache.org/) and
having free GNA hosting, even though we eventually moved happily to
[git](https://git-scm.com/) and [github](https://github.com/).

### 2007: PISM gets ice streams {#pism_gets_ice_streams}

The next idea, circa mid-2007, that went into PISM was that the SSA
should be solved //everywhere//. This is because, in a Coulomb or
near-Coulomb basal drag regime, the solution simply returns zero sliding
where the base is sufficiently strong. Solving everywhere thus defines
the ice stream regions organically. This idea arose because Bueler
actually read C. Schoof\'s isothermal paper \[C. Schoof (2006). //A
variational approach to ice stream flow//, J. Fluid Mech. 556,
227\--251\], and realized this made just as much sense in a
thermocoupled context.

Solving the SIA everywhere would do no harm because in low-angle streams
and shelves the SIA produces low velocities. Furthermore, a convex
combination of two reasonable stress balance solutions (i.e. SIA+SSA)
was reasonable.

Almost as important, in driving the creation of the solve-SSA-everywhere
model, was the failure of PISM, and every other model, to produce
anything sensible from the [ISMIP-HEINO modeling
assumptions/requirements and boundary
conditions](http://www.ingentaconnect.com/content/igsoc/jog/2010/00000056/00000197/art00001).
The issue seen in that project is that, in essence, there is no way to
switch sliding on or off, in a physically-based
thermomechanically-coupled manner, entirely within the SIA paradigm. One
needs to balance transitions in boundary shear stress with //membrane
stresses// within the ice.

In other words, the SIA is a good model, but not of sliding (//or ice
shelves, for that matter//).

These ideas, and Jed\'s work on the PISM SSA implementation, led to
actually having [ice streams in the model for the right reasons by
2007](http://pism.github.io/uaf-iceflow/talkagu.pdf). The
paper E. Bueler and J. Brown, (2009). //Shallow shelf approximation as a
"sliding law" in a thermomechanically coupled ice sheet model//, J.
Geophys. Res. 114 (F3) was the result. This paper turned out to be the
core of PISM, and it is the most-cited of the PISM-related papers.

### 2008: new team {#new_team}

A new proposal to a NASA Modeling, Analysis, and Prediction call, based
on a team of Bueler, Khroulev, mathematician David Maxwell, and
glaciologists Martin Truffer and Regine Hock, was funded as NNX09AJ38C.
To be continued \...

The new proposal made sense because Constantine Khroulev was finishing
his MS Math in Fall 2007 (on unrelated math topics). That is, he became
recruitable to the project. Constantine started in spring 2008 and was
soon inside PISM. He produced [startlingly-complete Antarctic results in
poster form in Fall 2008 at the WAIS
conference](http://pism.github.io/uaf-iceflow/khroulev_final.pdf).
But PISM was distincly lacking in ability to move the calving front and
the grounding line.

Without needing excess tuning based on generally-unavailable data (i.e.
inversion of measured surface velocities) the results for surface
velocity have the right look. Indeed, by early 2009 we saw that
nearly-untuned results for Greenland [matched observations reasonably
well](http://pism.github.io/uaf-iceflow/BKAJS_submit2_twocolumn.pdf).

### 2008: PIK collaboration {#pik_collaboration}

Fall 2008 involved another big change: Anders Levermann and students
(Maria Martin and Ricarda Winkelmann) came to Fairbanks to propose a
collaboration in which they would add what PISM needed. To be continued
\...

And another: Andy Aschwanden was hired as an ARSC PostDoc in Fall 2009.
To be continued \...

### 2011: PISM goes viral {#pism_goes_viral}

FIXME

{=mediawiki}
{{:pism-uaf-publications.png?450|}}

