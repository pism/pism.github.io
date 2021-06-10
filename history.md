---
title: History
subtitle: A Brief History of PISM
layout: page
hero_height: is-medium
hero_image: /pism_website_test/img/header_blackboard.jpg
hero_darken: false
show_sidebar: true
---

# A Brief History of PISM

**Before 2001:**

* First approach of a (nominally Antarctic) ice-sheet model by Craig Lingle
* Elena Suleimani (née Troshina) improves model based on Mahaffey’s equations and other numerical methods
* Accuracy test against the analytical solution for a circular ice cap on a flat bed with constant accumulation and for *CLIMAP* reconstruction of the Antarctic ice sheet (20 kyr BP)
* Model equations transformed to forms with a stretched vertical coordinate in Fortran 90 (3-D temperature equation not stable yet)
* First paper on *“Relative magnitudes of shear and longitudinal strain rates in the inland Antarctic ice sheet, and response to increasing accumulation”* by [Lingle and Troshina (1998)](https://doi.org/10.3189/1998AoG27-1-187-193)

**2001: A team forms**

* Lingle attends talk by Ed Bueler on heat equations on manifolds with potential application to glacier models
* Short course by Lingle on glaciological basics, with Bueler, Latrice Bowman, Jed Brown, and Dave Covey in attendance at various points
* Application for NASA model-development funding with Bueler and Covey as Co-Is, to build an Antarctic model which added thermo-mechanical coupling and ice-shelf dynamics to the existing Fortran model, as a modeling component (sub-grant) of the U Kansas *“Polar Radar for Ice Sheet Measurements” (PRISM)* project
* Paper on understanding numerical models by checking them against exact predictions (solutions) of the differential equations: [Bueler et al. (2005)](https://doi.org/10.3189/172756505781829449)
* Bowman first graduate student to work on ice flow with Bueler

**2003: PETSc and C++ ... and PISM**

* Brown (as undergraduate) reports about [PETSc](http://www.mcs.anl.gov/petsc/) library that allows to work in parallel at a higher conceptual level, requiring switch to C++
* Brown and Bueler define object classes and rebuild isothermal SIA model, with under-development thermomechanical coupling code
* Bueler adds thermocoupling to the SIA with Brown and Lingle assistance, and emphasizing exact solutions to check: [Bueler et al. (2007)](https://doi.org/10.3189/002214307783258396)
* Brown adds and tests a SSA solver in PISM, leading to successful [MS project defense](http://pism.github.io/uaf-iceflow/slidesJBrown.pdf) in August 2006
* [NetCDF](http://www.unidata.ucar.edu/software/netcdf/) is adopted as the input/output format (instead of PETSc binary files that lack included and standardized metadata)
* Bueler suggests model name *“the C-plus-plus Object-oriented Multi-Modal, Verifiable Numerical Ice Sheet Model”*, a.k.a. *COMMVNISM*
* Brown proposes new name *“Parallel Ice Sheet Model”*, short *PISM*

**2006: PISM goes public**

* In September 2006, PISM is for the first time hosted publicly on [Gna!](https://en.wikipedia.org/wiki/Gna) with a [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License) (later moved to [git](https://git-scm.com/) and [Github](https://github.com/))

**2007: PISM gets ice streams**

* Application of SSA solver also to ice streams in near-Coulomb basal drag regime in thermo-coupled context after Bueler reading [Schoof’s (2006) isothermal paper](https://doi.org/10.1017/S0022112006009591)
* Convex combination of two reasonable stress-balance solutions (i.e. SIA+SSA)
* Participation in [*ISMIP-HEINO*](https://doi.org/10.3189/002214310792447789) proves that SIA is not sufficient to balance transitions in boundary shear stress with “membrane stresses” within the ice, supporting SSA-everywhere approach and having [ice streams in the model for the right reasons](http://pism.github.io/uaf-iceflow/talkagu.pdf) as the core of PISM
* Most cited PISM-related paper by [Bueler and Brown (2009)](https://doi.org/10.1029/2008JF001179)

**2008: New team**

* New proposal to a NASA Modeling, Analysis, and Prediction call, based on a team of Bueler, Constantine Khroulev, mathematician David Maxwell, and glaciologists Martin Truffer and Regine Hock, is funded
* Khroulev starts in spring 2008 after finishing his MS Math, producing [startlingly-complete Antarctic results in Fall 2008 at the WAIS conference](http://pism.github.io/uaf-iceflow/khroulev_final.pdf)
* Nearly-untuned results for Greenland [match observations reasonably well](http://pism.github.io/uaf-iceflow/BKAJS_submit2_twocolumn.pdf)

**2008: PIK collaboration**

* Anders Levermann and students (Maria Martin and Ricarda Winkelmann) from PIK come to Fairbanks to propose a collaboration in which they would add what PISM needed for applications to the Antarctic Ice Sheet (ability to move the calving front and the grounding line)
* Model description paper by [Winkelmann et al. (2011)](https://doi.org/10.5194/tc-5-715-2011)
* Andy Aschwanden is hired as an *ARSC* PostDoc in Fall 2009, implementing an [enthalpy formulation](https://doi.org/10.3189/2012JoG11J088)

**2011: PISM goes viral**

* Torsten Albrecht from PIK visits UAF and merges code versions including calving parameterization ([Levermann et al., 2012](https://doi.org/10.5194/tc-6-273-2012)) and fracture formation processes ([Albrecht & Levermann, 2012](https://doi.org/10.3189/2012JoG11J191))

**2012: Community building**

* [European PISM ice sheet modeling workshop](http://www.mpimet.mpg.de/en/wissenschaft/ozean-im-erdsystem/euro-pism-workshop.html) in Hamburg, Germany
* [Nick Golledge et al. (2012)](https://doi.org/10.1073/pnas.1205385109) apply PISM to Last Glacial Antarctica
* PISM participates in [*MISMIP*](https://doi.org/10.5194/tc-6-573-2012)
* PISM participates in *SeaRISE* ([Antarctica](https://doi.org/10.1002/jgrf.20081) and [Greenland](https://doi.org/10.1002/jgrf.20076))
* PISM participates in [*LARMIP*](https://doi.org/10.1007/s00382-012-1471-4)
* PISM participates in *ice2sea* [*MISMIP3d*](https://doi.org/10.3189/2013JoG12J129)

**2014: More processes**

* Albrecht and Levermann implement [fracture density approach](https://doi.org/10.5194/tc-8-587-2014) based on continuum damage mechanics
* Florian Ziemen et al. use PISM [coupled to a climate model](https://doi.org/10.5194/cp-10-1817-2014)
* [Matthias Mengel and Levermann (2014)](https://doi.org/10.1038/nclimate2226) investigate threshold melting and tipping behavior in East Antarctica
* Bueler and W. van Pelt implement a [subglacial hydrology scheme](https://doi.org/10.5194/gmd-8-1613-2015)
* Johannes Feldmann et al. implement [subgrid grounding-line interpolation](https://doi.org/10.3189/2014JoG13J093)

**2015: Paleo and WAIS**

* PISM participates in [*PLISMIP-ANT*](https://doi.org/10.5194/tc-9-881-2015)
* WAIS destabilization study by [Feldmann and Levermann (2015)](https://doi.org/10.1073/pnas.1512482112)

**2016: High resolution**

* [Aschwanden et al. (2016)](https://doi.org/10.1038/ncomms10524) run high-resolution simulations for the Greenland Ice Sheet

**2017: Inversion**

* Marijke Habermann et al. implement [inversion scheme for basal yield stress](https://doi.org/10.1017/jog.2017.61)

**2018: MIPs and PICO**

* Ronja Reese et al. implement [PICO melt module](https://doi.org/10.5194/tc-12-1969-2018), which is applied during Antarctic deglaciation ([Kingslake, Scherer, Albrecht et al., 2018](https://doi.org/10.1038/s41586-018-0208-x))
* PISM participates in *initMIP* ([Greenland](https://doi.org/10.5194/tc-12-1433-2018) and [Antarctica](https://doi.org/10.5194/tc-13-1441-2019))
* PISM participates in [*SHMIP*](https://doi.org/10.1017/jog.2018.78)

**2019: Projections**

* Feedback of ice-shelf melt on global climate by [Golledge et al. (2019)](https://doi.org/10.1038/s41586-019-0889-9)
* Projections of sea-level contribution from Greenland by [Aschwanden et al. (2019)](https://doi.org/10.1126/sciadv.aav9396) 

**2020: MIPs and Antarctic thresholds**

* PISM participates in [*ABUMIP*](https://doi.org/10.1017/jog.2020.67)
* PISM participates in *ISMIP6* ([Antarctica](https://doi.org/10.5194/tc-14-3033-2020) and [Greenland](https://doi.org/10.5194/tc-14-3071-2020))
* PISM participates in [*LARMIP-2*](https://doi.org/10.5194/esd-11-35-2020)
* PISM participates in [*MISMIP+*](https://doi.org/10.5194/tc-14-2283-2020)
* Tipping points and hysteresis behavior in Antarctica in a warming climate by [Julius Garbe et al. (2020)](https://doi.org/10.1038/s41586-020-2727-5)
* Description of PISM (parameter sensitivities and boundary conditions) for paleo applications in Antarctica by [Albrecht et al. (2020)](https://doi.org/10.5194/tc-14-599-2020)

**2021: PISM-ocean coupling**

* Moritz Kreuzer et al. use PICO to [couple PISM with ocean model MOM5](https://doi.org/10.5194/gmd-2020-230)
